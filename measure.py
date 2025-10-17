"""
Measurement tools for algorithm analysis.
This file contains helper functions to time algorithm execution
across different input sizes.
"""

import time
import random
from implementation_a import find_duplicates as find_duplicates_a
from implementation_b import find_duplicates as find_duplicates_b
from implementation_c import find_duplicates as find_duplicates_c
from implementation_d import find_duplicates as find_duplicates_d


def generate_test_data(size, duplicate_rate=0.3):
    """
    Generate test data with a specified percentage of duplicates.
    
    Args:
        size: Number of elements in the dataset
        duplicate_rate: Percentage of elements that should be duplicates (0.0 to 1.0)
        
    Returns:
        List of integers with duplicates
    """
    unique_count = int(size * (1 - duplicate_rate))
    data = list(range(unique_count))
    
    # Add duplicates by randomly selecting from existing elements
    duplicates_needed = size - unique_count
    for _ in range(duplicates_needed):
        data.append(random.choice(data))
    
    # Shuffle to mix duplicates throughout
    random.shuffle(data)
    return data


def measure_time(func, data):
    """
    Measure the execution time of a function with given data.
    
    Args:
        func: Function to measure
        data: Input data to pass to the function
        
    Returns:
        Execution time in seconds
    """
    start = time.perf_counter() # Start timer
    func(data) # Run function
    end = time.perf_counter() # End timer
    return end - start # Calculate elapsed time


def run_performance_tests():
    """
    Run performance tests on all implementations across different input sizes.
    
    Returns:
        Dictionary mapping implementation names to lists of (size, runtime) tuples
    """
    implementations = {
        'Implementation A (Nested Loops)': find_duplicates_a,
        'Implementation B (Sorting)': find_duplicates_b,
        'Implementation C (Set)': find_duplicates_c,
        'Implementation D (Counting)': find_duplicates_d
    }
    
    sizes = [100, 500, 1000, 5000, 10000]
    results = {name: [] for name in implementations.keys()}
    
    print("Running performance tests...")
    print("-" * 60)
    
    for size in sizes:
        print(f"\nTesting with dataset size: {size}")
        test_data = generate_test_data(size)
        
        for name, func in implementations.items():
            runtime = measure_time(func, test_data)
            results[name].append((size, runtime))
            print(f"  {name}: {runtime:.6f} seconds")
    
    print("\n" + "-" * 60)
    print("Performance tests complete!")
    return results

if __name__ == "__main__":
    # Run tests and output time values
    results = run_performance_tests()