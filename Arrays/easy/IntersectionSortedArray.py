def intersection_sorted_array(num1, num2):
    """
    Returns the intersection (with duplicates) of two sorted lists.
    Assumes num1 and num2 are sorted in ascending order.
    """
    i, j = 0, 0
    n1, n2 = len(num1), len(num2)
    intersection = []
    while i < n1 and j < n2:
        if num1[i] == num2[j]:
            intersection.append(num1[i])
            i += 1
            j += 1
        elif num1[i] < num2[j]:
            i += 1
        else:
            j += 1
    return intersection
print(intersection_sorted_array([1,2,3,9,11,11,12],[1,2,8,9,11]))

    
