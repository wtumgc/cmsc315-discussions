"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""

""" TESTING """

def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value. X
    - Add comments explaining what happens to existing elements
        after an insertion occurs. X
    - Use comments to explain how insertion performance may vary depending on
        where the insertion occurs. X
    """
    # Insert a value for list "lst" at index "index" with value "value"
    # Performance is O(n) unless the insert occurs at or near the end of the list
    #   in which case it would be O(1). This is due to the fact that most or all of
    #   the list elements need to shifted to the "right"
    lst.insert(index,value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists. X
    - Return the removed value. X
    - Return None if the index is invalid. X
    - Add comments explaining why index validation and safe deletion are important. X
    """
    # Remove a list item at a specific index and return its value but first make
    #   sure the index is valid to prevent the module from throwing an exception
    #   and aborting.
    if index < 0 or index >= len(lst):
        return None

    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found. X
    - Return -1 if the value is not found. X
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Search list beginning at the beginning of the list until the provided value is found
    #   or return -1 if not found.
    # This is a linear i.e., O(n) complexity search because the search will never have to do
    #   more work other than look at each list item.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values. X
    # 2. Display the original list. X
    # 3. Test insertion at:
    #    - the beginning X
    #    - the middle X
    #    - the end X
    # 4. Display the list after each insertion. X
    # 5. Use comments to explain each step in the implementation. X

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Create a list of integers and display the list
    num_list = [1,2,3,4,5,6,]
    print("The new list of integers is as follows:", num_list)

    # Insert a list item at the beginning of the list
    print("Inserting 99 at the beginning of the list...")
    #num_list.insert(0,99)
    insert_at(num_list,0,99)
    print("The new list of integers is now as follows:", num_list)

    # Insert a list item in the middle of the list
    print("Inserting 88 in the middle of the list...")
    #num_list.insert(4,88)
    insert_at(num_list,4,88)
    print("The new list of integers is now as follows:", num_list)

    # Insert a list item at end of the list
    print("Inserting 77 at the end of the list...")
    #num_list.insert(9,77)
    insert_at(num_list,9,77)
    print("The new list of integers is now as follows:", num_list)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning X
    #    - the middle X
    #    - the end X
    # 2. Display the removed value. X
    # 3. Display the updated list after each deletion. X
    # 4. Use comments to clearly explain what is happening in the output. X

    # Delete the same items added above starting with the beginning of ths list
    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Delete items from the beginning, middle and end of this list
    print("The current list of integers is as follows:", num_list)

    # Delete a list item at the beginning of the list
    print("Delete 99 at the beginning of the list...")
    #num_list.remove(99)
    delete_at(num_list,0)
    print("The new list of integers is now as follows:", num_list)

    # Delete a list item in the middle of the list
    print("Delete 88 in the middle of the list...")
    #num_list.remove(88)
    delete_at(num_list,3)
    print("The new list of integers is now as follows:", num_list)

    # Delete a list item at end of the list
    print("Delete 77 at the end of the list...")
    #num_list.remove(77)
    delete_at(num_list,6)
    print("The new list of integers is now as follows:", num_list)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists. X
    # 2. Search for a value that does not exist. X
    # 3. Display the search results with clear explanations. X
    # 4. Use comments to explain each step. X

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Search items from this list. One that we know exists and one we know does not (which should return -1)
    print("The current list of integers is as follows:", num_list)
    print("Search for existing item with value of 3 and the result is (i.e., index value) is:", search_value(num_list,3))
    print("Search for non-existing item with value of 9 and the result is (i.e., index value) is:", search_value(num_list,9))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index X
    # - Search for a missing value X
    # - Insert into an empty list X
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Edge case testing starting with deleting a list item with an invalid index
    print("The current list of integers is as follows:", num_list)
    print("Attempting to delete list item at index 20 which DOES NOT EXIST. The result is (should be 'None'):", delete_at(num_list,20))
    print("Attempting to search list for a value of 67 which DOES NOT EXIST. The result is (should be -1)", search_value(num_list,67))

    num_list2 = []
    print("Created new list with no items i.e., EMPTY. List 'num_list2' created and the output of it is:", num_list2)
    insert_at(num_list2,0,9)
    print("...added an item with value of 9 to newly created empty list 'num_list2' and the new output of the list is:",num_list2)

    num_list3 = []
    print("Created new list with no items i.e., EMPTY. List 'num_list3' created and the output of it is:", num_list3)
    #delete_at(num_list3,3)
    print("...attempting to delete item at index 3 from 'num_list3' (which does not exist) and the result is (should be 'None'):",delete_at(num_list3,3))

if __name__ == "__main__":
    main()