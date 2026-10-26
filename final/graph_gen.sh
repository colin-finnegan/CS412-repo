# generate_all_tests.py
import random

def generate_test_case(filename, num_vertices, edge_probability):
    """Generate a test case with specified parameters"""
    vertices = [f"v{i}" for i in range(num_vertices)]
    edges = []
    
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if random.random() < edge_probability:
                edges.append((vertices[i], vertices[j]))
    
    with open(filename, 'w') as f:
        f.write(f"{len(edges)}\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")
    
    return len(edges)

# Generate test suite
test_cases = [
    ("test_cases/small.txt", 10, 0.3),
    ("test_cases/medium.txt", 50, 0.2),
    ("test_cases/large.txt", 1000, 0.1),
    ("test_cases/very_large.txt", 10000, 0.01),
]

for filename, n, p in test_cases:
    m = generate_test_case(filename, n, p)
    print(f"Generated {filename}: {n} vertices, {m} edges")