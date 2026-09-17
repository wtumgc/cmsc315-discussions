"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    #   Search the array list, if necessary to find the provided target value
    for x in range(len(lst)):

    #   If found, return the index
        if lst[x] == target:
            return x

    #   If not found, the method will end here and return a -1 value

    return -1

    #   The Big-O complexity is O(n) sine the worse case is that
    #       every element in the array might be traversed.

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    #   Create a reference variable for the first and last array list elements
    first = 0
    last = len(lst) -1

    #   In a loop, search the right or left (depending on whether the target is
    #       more or less than the middle element value
    while first <= last:
        #   Locate the middle of the array list
        #   // in division returns the floor integer value
        middle = (first + last) // 2

        #   If the middle index element value happens to be the target...
        if lst[middle] == target:
            return middle

        #   If the requested target value is less than the middle value,
        #       exclude the right side portion of the array list
        elif target < lst[middle]:
            last = middle - 1

        #   If the requested target value is more than the middle value,
        #       exclude the left side portion of the array list
        elif target > lst[middle]:
            first = middle + 1

        #   Each time the array list is split in 2 (i.e., binary), the list
        #       is cut in half. This makes the search complexity O(log2 n).

        #   Return -1 if no match is found and the only remaining element is
        #       not a match
    return -1

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset. X
    # 2. Test both linear search and binary search. X
    # 3. Search for:
    #    - a value that exists X
    #    - a value that does not exist X
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    #   Create an array list to be used for both linear
    #       and binary searching
    search_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    #   Perform a LINEAR search for a KNOWN VALUE
    print("linear search for a KNOWN VALUE of 55. Result should be index 4:", linear_search(search_list,55))

    #   Perform a BINARY search for a KNOWN VALUE
    print("Binary search for a KNOWN VALUE of 55. Result should be index 4:", binary_search(search_list,55))

    #   Perform a LINEAR search for an UNKNOWN VALUE
    print("linear search for a KNOWN VALUE of 52. Result should be -1:", linear_search(search_list,52))

    #   Perform a BINARY search for an UNKNOWN VALUE
    print("Binary search for a KNOWN VALUE of 52. Result should be -1:", binary_search(search_list,52))


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset. X
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    #   Create a much larger list to demonstrate the efficiency of a binary search
    #       List will be five hundred thousand elements.
    big_list = list(range(5000000))
    print("Created a large data set of 5,000,000 elements")

    #   Perform a LINEAR search for a KNOWN VALUE
    print("linear search for a KNOWN VALUE of 4,500,000 using a large data set:", linear_search(big_list,4500000))

    #   Perform a BINARY search for a KNOWN VALUE
    print("Binary search for a KNOWN VALUE of 4,500,000 using a large data set:", binary_search(big_list,4500000))

    #   

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position x
    # - Value at the last position x
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #   Edge case - Value at the first position
    elist1 = [11, 22, 33, 44, 55, 66, 77]
    target = 11
    f_result = linear_search(elist1, target)
    f_result = binary_search(elist1, target)
    print("Edge case 1 results")
    print("Target:", target)
    print("Linear search result:", f_result)
    print("Binary search result:", f_result)

    #   Edge case - Value at last position
    target = 77

    l_result = linear_search(elist1, target)
    l_result = binary_search(elist1, target)

    print("Edge Case 2 results")
    print("Target:", target)
    print("Linear search result:", l_result)
    print("Binary search result:", l_result)

#   The above first and last target results return the first
#   and last element of the string array.
#
#   The linear search searches each element in the
#   array if necessary while the binary search reduced
#   the size by approximately half of the array each time.

if __name__ == "__main__":
    main()