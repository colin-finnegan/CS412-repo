#!/bin/bash

echo "Computing wallclock times for approximation algorithm"
echo "===================================================="

# Array of test files
test_files=(
    "test_cases/small.txt"
    "test_cases/medium.txt"
    "test_cases/large.txt"
    "test_cases/very_large.txt"
    "test_cases/non_optimal.txt"
)

# Run each test 5 times and average
for test_file in "${test_files[@]}"; do
    echo ""
    echo "Testing: $test_file"
    echo "------------------------"
    
    total_time=0
    for i in {1..5}; do
        start_time=$(date +%s.%N)
        python cs412_minvertexcover_approx.py "$test_file" > /dev/null
        end_time=$(date +%s.%N)
        elapsed=$(echo "$end_time - $start_time" | bc)
        total_time=$(echo "$total_time + $elapsed" | bc)
        echo "Run $i: $elapsed seconds"
    done
    
    avg_time=$(echo "scale=6; $total_time / 5" | bc)
    echo "Average time: $avg_time seconds"
done