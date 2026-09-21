"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary. X
    # 2. Add at least 5 key-value pairs. X
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table. X
    # 4. Display the contents of the dictionary. X

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    #   Create an empty hash table
    pets = {}

    #   Add key pair elements to the hash table.

    pets["Cat"] = 1
    pets["Dog"] = 2
    pets["Rabbit"] = 3
    pets["Pig"] = 4
    pets["Tigger"] = 5

    #   This above hash table in Python acts like a dictionary which
    #   stores a key pair which allows values of elements to be
    #   quickly looked up by each elements keys value.

    #   Print the newly create hash table .ie., dictionary

    print("Pet Hash Table Elements")
    print(pets)


    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys. X
    # 2. Clearly display the lookup results. X
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    pet1 = pets["Cat"]
    print("The lookup value for cat preference is", pet1)

    pet2 = pets["Pig"]
    print("The lookup value for pig preference is", pet2)

    #   In the above lookup calls, the key is used from the key pair
    #   to lookup the hash table element in O(1) time to find the
    #   element via a hash without performing a linear iteration,
    #   which would be less efficient.

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key. X
    # 2. Display the dictionary before and after the update. X
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    
    print("Here is the hash table BEFORE the update")
    print(pets)

    print("Now let's make the key value for a cat lower priority than the other pets")
    pets["Cat"] = 6

    print("Here is the hash table AFTER the update")
    print(pets)

    #   When the hash table element for cats is updated with a new value,
    #   the existing table element is update rather than a new hash table
    #   element being created.

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Here is the hash table BEFORE the deletion")
    print(pets)

    #   Delete an element from the pets hash table
    del pets["Rabbit"]

    print("Here is the hash table AFTER the deletion")
    print(pets)

    #   When the Rabbit hash table element is deleted,
    #   the entire hash table entry is removed and no
    #   longer exists. No other has table element is
    #   effected.


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key X
    # - Delete a missing key safely X
    # - Update a missing key X
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    #   1st edge case - lookup a missing or non-existing key. If the key exists,
    #   the value is printed, if not an exception message is printed
    try:
        print("Edge Case 1: Try to delete a hash table element that does not exists")
        print(pets["Lizard"])   #print key value if it exists
    except KeyError:
        print("    This pet is not in the desired pet hash table")


    #   2nd edge case - similar to edge case 1, check first for the
    #   existence of the key and respond accordingly instead of throwing
    #   an exception. Once the provided key is attempted to be deleted,
    #   the user will be told the deletion was successful. Otherwise, the
    #   user will be told the table entry does not exist and no change was made.
    if "Lizard" in pets:
        del pets["Lizard"]
        print("Edge Case 2: The hash table entry for Lizard was deleted")
    else:
        print("Edge Case 2: Lizard does not exist in the pets hash table, no change was made to the hash table")


    #   3rd edge case - update a missing/non-existant key. If the key exists, the
    #   value will be updated. If not, a new table element will be created.
    print("Edge case 3: Here is the hash table BEFORE the update for a non-existing table entry for Lizard")
    print("   ", pets)
    pets["Lizard"] = 99 #does not exist
    print("    " + "Here is the hash table AFTER the update for a non-existing table entry for Lizard")
    print("   ", pets)


    #   4th edge case - lookup for an emtpy hash table
    pets2 = {}
    print("Edge case 4: Lookup an empty hash table")
    print("   ", pets2)


if __name__ == "__main__":
    main()