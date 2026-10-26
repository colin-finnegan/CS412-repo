Minimum Vertex Cover - Exact Solution
=====================================

Description:
This program finds the exact minimum vertex cover for an undirected graph.
The algorithm uses a brute-force branch and bound approach.

Input Format:
-------------
First line: m (number of edges)
Next m lines: u v (edge between vertices u and v)

Example:
2
a b
b c

Running the Program:
-------------------
python cs412_minvertexcover_exact.py <input_file>

Test Cases:
-----------
test_cases/small_test.txt: 5 vertices, runs in <1 second
test_cases/medium_test.txt: 15 vertices, runs in ~30 seconds
test_cases/large_test.txt: 20 vertices, runs in ~10 minutes
test_cases/very_large_test.txt: 25 vertices, runs for >20 minutes

Notes:
- The algorithm has exponential time complexity O(2^n)
- For graphs with >25 vertices, runtime becomes impractical
- Output is written to stdout in space-separated format
- Debug info is written to stderr