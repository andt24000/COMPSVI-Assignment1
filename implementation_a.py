"""
Implementation A: Nested Loop Approach
Find all duplicate values in a list using nested loops.
"""

def find_duplicates(data):
    """
    Find duplicate values using nested loops.
    
    Args:
        data: List of integers
        
    Returns:
        List of duplicate values (each duplicate appears once in result)
    """
    duplicates = []
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    
    return duplicates


if __name__ == "__main__":
    # Test with a small dataset
    test_data = [1, 2, 3, 2, 4, 5, 3, 6, 7, 4]
    result = find_duplicates(test_data)
    print(f"Duplicates found: {result}")