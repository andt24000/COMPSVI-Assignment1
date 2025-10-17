"""
Implementation C: Set Approach
Find all duplicate values using a set for fast lookups.
"""

def find_duplicates(data):
    """
    Find duplicate values using a set to track seen elements.
    
    Args:
        data: List of integers
        
    Returns:
        List of duplicate values (each duplicate appears once in result)
    """
    seen = set()
    duplicates = set()
    
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)


if __name__ == "__main__":
    # Test with a small dataset
    test_data = [1, 2, 3, 2, 4, 5, 3, 6, 7, 4]
    result = find_duplicates(test_data)
    print(f"Duplicates found: {result}")