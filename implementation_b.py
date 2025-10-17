"""
Implementation B: Sorting Approach
Find all duplicate values by first sorting the list.
"""

def find_duplicates(data):
    """
    Find duplicate values by sorting first, then checking adjacent elements.
    
    Args:
        data: List of integers
        
    Returns:
        List of duplicate values (each duplicate appears once in result)
    """
    if not data:
        return []
    
    # Sort the data first
    sorted_data = sorted(data)
    duplicates = []
    
    # Check adjacent elements
    for i in range(len(sorted_data) - 1):
        if sorted_data[i] == sorted_data[i + 1] and sorted_data[i] not in duplicates:
            duplicates.append(sorted_data[i])
    
    return duplicates


if __name__ == "__main__":
    # Test with a small dataset
    test_data = [1, 2, 3, 2, 4, 5, 3, 6, 7, 4]
    result = find_duplicates(test_data)
    print(f"Duplicates found: {result}")