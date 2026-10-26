import sys

def build_residual(orig_caps, flows):
    """
    Build residual capacities dict:
    residual[u][v] = capacity available from u to v in residual graph.
    """
    residual = {}
    for (u, v), cap in orig_caps.items():
        # forward residual (original edge)
        res = cap - flows.get((u, v), 0)
        if res > 0:
            residual.setdefault(u, {})[v] = residual.setdefault(u, {}).get(v, 0) + res
        # reverse residual from any existing flow on (u,v)
        rev = flows.get((u, v), 0)
        if rev > 0:
            residual.setdefault(v, {})[u] = residual.setdefault(v, {}).get(u, 0) + rev
    return residual

def dfs_find_path(residual, s, t):
    """
    DFS to find any path from s to t in residual graph (edges with positive residual).
    Returns parent dict mapping node -> parent on path, or None if unreachable.
    """
    stack = [s]
    parent = {s: None}
    while stack:
        u = stack.pop()
        if u == t:
            break
        for v, cap in residual.get(u, {}).items():
            if cap > 0 and v not in parent:
                parent[v] = u
                stack.append(v)
    return parent if t in parent else None

def augment_flow_along_path(parent, orig_caps, flows, s, t, residual):
    """
    Determine bottleneck and update flows along the path according to original edges.
    """
    # reconstruct path
    path = []
    cur = t
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()  # from s to t

    # find bottleneck
    bottleneck = float('inf')
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        cap = residual[u][v]
        if cap < bottleneck:
            bottleneck = cap

    # apply augment: for each edge u->v on path
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        # if original edge exists u->v, increase flow
        if (u, v) in orig_caps:
            flows[(u, v)] = flows.get((u, v), 0) + bottleneck
        else:
            # otherwise we must be using reverse residual for an original edge v->u,
            # so decrease flow on (v,u)
            flows[(v, u)] = flows.get((v, u), 0) - bottleneck

    return bottleneck

def max_flow_and_min_cut(vertex_count, edge_list):
    """
    edge_list: list of tuples (u, v, cap)
    returns: (max_flow_value, sorted_list_of_min_cut_edges_as_(u,v) )
    """
    s = 0
    t = vertex_count - 1

    # store original capacities in dict (u,v) -> cap
    orig_caps = {}
    for u, v, cap in edge_list:
        # if multiple edges between same u,v, we sum capacities (common simple approach)
        orig_caps[(u, v)] = orig_caps.get((u, v), 0) + cap

    # flows dict (u,v) -> current flow (only for original directed edges)
    flows = {}

    # Ford-Fulkerson: repeat until no augmenting path
    while True:
        residual = build_residual(orig_caps, flows)
        parent = dfs_find_path(residual, s, t)
        if parent is None:
            break  # no augmenting path
        bottleneck = augment_flow_along_path(parent, orig_caps, flows, s, t, residual)
        # continue until no path

    # total flow is sum of flows leaving source s
    total_flow = 0
    for (u, v), f in flows.items():
        if u == s:
            total_flow += f

    # compute reachable set in residual graph (edges with positive residual)
    residual = build_residual(orig_caps, flows)
    # simple DFS/BFS from s using residual edges > 0
    stack = [s]
    reachable = {s}
    while stack:
        u = stack.pop()
        for v, cap in residual.get(u, {}).items():
            if cap > 0 and v not in reachable:
                reachable.add(v)
                stack.append(v)

    # min-cut edges are original edges (u,v) where u is reachable and v is not
    min_cut_edges = []
    for (u, v), cap in orig_caps.items():
        if u in reachable and v not in reachable and cap > 0:
            min_cut_edges.append((u, v))

    min_cut_edges.sort()  # sort by u then v
    return total_flow, min_cut_edges

def main():
    # read input
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    vertex_count = int(next(it))
    edge_count = int(next(it))
    edge_list = []
    for _ in range(edge_count):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        edge_list.append((u, v, c))

    total_flow, cut_edges = max_flow_and_min_cut(vertex_count, edge_list)

    # print total flow
    # capacities are integers in this course, so flow will be integer
    print(int(total_flow))
    # print cut edges one per line "u v"
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == "__main__":
    main()
