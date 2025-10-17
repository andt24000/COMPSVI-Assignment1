"""
Implementation D: Triple Loop Approach
Find all duplicate values by checking each pair and verifying with a third loop.
"""

def find_duplicates(data):
    """
    Find duplicate values using three nested loops - an intentionally inefficient approach.
    
    Args:
        data: List of integers
        
    Returns:
        List of duplicate values (each duplicate appears once in result)
    """
    duplicates = []
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                # Use a third loop to check if we've already added this duplicate
                already_added = False
                for dup in duplicates:
                    if dup == data[i]:
                        already_added = True
                        break
                
                if not already_added:
                    duplicates.append(data[i])
    
    return duplicates


if __name__ == "__main__":
    # Test with a small dataset
    test_data = [1, 2, 3, 2, 4, 5, 3, 6, 7, 4]
    result = find_duplicates(test_data)
    print(f"Duplicates found: {result}")