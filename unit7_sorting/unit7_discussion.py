"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    #   Check for the base case of an empty list of a list
    #   with only one element.
    if len(lst) <= 1:
        return lst

    #   Create a copy of the list so to keep the original list intact.
    slist = lst.copy()

    #   Cycle through the list to compare and change the order as
    #       each list element if reviewed.
    for x in range(len(slist) - 1):

        #   Compare list elements next to each other.
        for y in range(len(slist) - x -1):

            #   Rotate elements if they are not in order.
            if slist[y] > slist[y + 1]:
                slist[y], slist[y + 1] = (slist[y + 1], slist[y])

    #   Return the newly sorted copy of the list.
    return slist


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    #   Check for the base case of an empty list of a list
    #   with only one element.
    if len(lst) <= 1:
        return lst

    #   Determine the middle point and device the list in two.
    middle = len(lst) // 2
    left_list = lst[:middle]
    right_list = lst[middle:]

    #   Search each half-list recursively
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    #   Merge the two halves and return the newly merged list.
    return merge(left_list, right_list)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    #   Create a new list to which will be the sorted and merged list
    new_list = []

    #   Initialize a variable for the position in each half
    l_pos = 0
    r_pos = 0

    #   Loop through each half-list and update with the smaller value.
    while l_pos < len(left) and r_pos < len(right):

        if left[l_pos] <= right[r_pos]:
            new_list.append(left[l_pos])
            l_pos += 1
        else:
            new_list.append(right[r_pos])
            r_pos += 1

    #   If there are value remaining from the left list, append them.
    new_list.extend(left[l_pos:])

    #   If there are value remaining from the right list, append them.
    new_list.extend(right[r_pos:])

    return new_list



def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    #   Create a list that is not sorted
    r_list = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]

    #   Display the new unsorted list
    print("Original list:", r_list)

    #   Sort the list using the bubble_sort method.
    bubble_list = bubble_sort(r_list)

    #   Display the bubble_sort list.
    print("Bubble Sort:", bubble_list)

    #   Sort the list using the merge_sort method.
    merge_list = merge_sort(r_list)

    #   Display the merge_sort list.
    print("Merge Sort:", merge_list)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    #   Create a new data set of unsorted list items
    r_list2 = [100, 91, 99, 92, 98, 93, 97, 94, 96, 95]

    #   Display the new unsorted list
    print("Original list:", r_list2)

    #   Sort the list using the bubble_sort method.
    bubble_list2 = bubble_sort(r_list2)

    #   Display the bubble_sort list.
    print("Bubble Sort:", bubble_list2)

    #   Sort the list using the merge_sort method.
    merge_list2 = merge_sort(r_list2)

    #   Display the merge_sort list.
    print("Merge Sort:", merge_list2)

    print("Dataset 2 results should behave the same as dataset 1.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    #   Edge Case 1: Empty list
    empty_list = []

    print("\nEdge Case 1 (Empty List)")
    print("Original Empty List:", empty_list)
    print("Bubble Sorted:", bubble_sort(empty_list))
    print("Merge Sorted:", merge_sort(empty_list))

    #   Since an empty list in terms of sorting is irrelevant,
    #   each sorting method returns back the empty list.

    #   Edge Case 2: Single-Item List
    single_list = [67]

    print("\nEdge Case 2 (Single-Item List)")
    print("Original Single-Item Empty List:", single_list)
    print("Bubble Sorted:", bubble_sort(single_list))
    print("Merge Sorted:", merge_sort(single_list))

    #   Since a single item list in terms of sorting is irrelevant,
    #   each sorting method returns back the single-item list.


if __name__ == "__main__":
    main()

""" OUTPUT

=== UNIT 7: SORTING ALGORITHMS ===

=== DATASET #1 ===
TODO: Create an unsorted dataset and test both sorting algorithms.
Original list: [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
Bubble Sort: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Merge Sort: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

=== DATASET #2 ===
TODO: Create a second dataset and compare sorting results.
Original list: [100, 91, 99, 92, 98, 93, 97, 94, 96, 95]
Bubble Sort: [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
Merge Sort: [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
Dataset 2 results should behave the same as dataset 1.

=== EDGE CASE TESTS ===
TODO: Demonstrate and explain edge cases.

Edge Case 1 (Empty List)
Original Empty List: []
Bubble Sorted: []
Merge Sorted: []

Edge Case 2 (Single-Item List)
Original Single-Item Empty List: [67]
Bubble Sorted: [67]
Merge Sorted: [67]

Process finished with exit code 0

"""