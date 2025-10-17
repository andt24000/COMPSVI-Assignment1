"""
Visualization tools for algorithm analysis.
This file contains functions to visualize  
performance across different input sizes.
"""
import matplotlib.pyplot as plt
from measure import run_performance_tests as run_performance_tests

def visualize_results(results):
    """
    Create a line graph showing runtime vs input size for all implementations.
    
    Args:
        results: Dictionary mapping implementation names to lists of (size, runtime) tuples
    """
    plt.figure(figsize=(12, 8))
    
    for name, data in results.items():
        sizes = [point[0] for point in data]
        runtimes = [point[1] for point in data]
        plt.plot(sizes, runtimes, marker='o', label=name, linewidth=2)
    
    plt.xlabel('Input Size (number of elements)', fontsize=12)
    plt.ylabel('Runtime (seconds)', fontsize=12)
    plt.title('Algorithm Performance Comparison: Finding Duplicates', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    print("\nVisualization saved as 'performance_comparison.png'")
    
    # Display the figure
    plt.show()

if __name__ == "__main__":
    # Run tests and create visualization
    results = run_performance_tests()
    visualize_results(results)