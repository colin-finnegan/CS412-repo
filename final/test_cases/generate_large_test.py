# generate_large_test.py
import random

def generate_test(filename, num_vertices):
    vertices = [f"v{i}" for i in range(num_vertices)]
    edges = []
    
    # Generate random edges (dense graph)
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if random.random() > 0.7:  # 30% density
                edges.append((vertices[i], vertices[j]))

    # Write to file
    with open(filename, 'w') as f:
        f.write(f"{len(edges)}\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")
    
    print(f"Generated {filename} with {num_vertices} vertices and {len(edges)} edges")

# Generate test cases
generate_test("large_test.txt", 20)
generate_test("very_large_test.txt", 31)