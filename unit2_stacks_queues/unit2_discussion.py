"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        self.stackItems = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # The "append" method creates a new array element at the end of the array
        # effectively behaving as top of the stack for this LIFO ADT
        self.stackItems.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # Remove the last item added to the stack using the built-in
        # pop method for arrays. Also check for empty stack
        if not self.stackItems:
            return None
            #return "The stack is empty"

        return self.stackItems.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Peek looks for the value of the item at the top of the stack
        # without removing it (and returns the value). Again, check for
        # an empty stack.
        if not self.stackItems:
            return None
            #return "The stack is empty"

        return self.stackItems[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        if len(self.stackItems) == 0:
            return True

        return False


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # Using the "collections" deque method, create an empty deque
        self.queueItems = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # Using the dequeue method, create an empty deque for queue entries
        self.queueItems.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Return the value of the first item in the queue and make sure (same as above
        # with Stack) the queue is not empty.
        if len(self.queueItems) == 0:
            return None

        return self.queueItems.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Return the value of the first item in the queue by referencing
        # the fist item in the queue array i.e., [0]
        if len(self.queueItems) == 0:
            return None

        return self.queueItems[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        if len(self.queueItems) == 0:
            return None

        return True


# TEST ABOVE CLASSES AND FUNCTIONS AND CONSTRUCTORS

def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object. X
    # 2. Add at least 4 values to the stack. X
    # 3. Improve the print statements so they clearly explain what is happening. X
    # 4. Demonstrate LIFO behavior. X
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack. X
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward. X


    print("\n=== STACK DEMO ===")
    print("      TODO: Create a Stack object, demonstrate LIFO behavior")

    # Create a stack object
    s1 = Stack()
    print("\n      Stack 's1' object created")

    # Try to POP an empty stack
    print("\n      test popping from an empty stack. ")
    s1.pop()
    print("      Testing a pop of an empty stack. Return value is", s1.stackItems)


    # DEMO PEEK behavior on an empty stack
    print("\n      Test peeking at an empty stack,")
    s1.peek()
    print("      The current stack contains:", s1.stackItems)

    # Add 4 values to the new stack
    print("\n      Push values to the new stack,")
    s1.push(33)
    s1.push(44)
    s1.push(55)
    s1.push(66)
    print("      values 33, 44, 55 & 66 'pushed' to the new s1 queue")

    # DEMO LIFO and POP behavior
    print("\n      Demonstrate LIFO and POP behavior. The current stack contains:", s1.stackItems)
    print("      Removing the last stack entry...")
    #print("      Popped last/top entry with value of:", s1.stackItems[0])
    print("      Popped last/top entry with value of:", s1.stackItems.pop())
    print("      New stack contains: ", s1.stackItems)


    # DEMO a new stack with only one item is empty after the one item is removed
    print("\n      Verify a single-item stack becomes empty after removal.")
    s2 = Stack()
    s2.push(67)
    print("      New stack with single item before pop", s2.stackItems)
    s2.pop()
    print("      After pop:", s2.stackItems)
    print("      Call the is_empty method and it returns:", s2.is_empty())


    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object. X
    # 2. Add at least 4 values to the queue. X
    # 3. Improve the print statements so they clearly explain what is happening. X
    # 4. Demonstrate FIFO behavior. X
    # 5. Show what happens when dequeue() is used on an empty queue. X
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue. X
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("      TODO: Create a Queue object, demonstrate FIFO behavior")

    # Create queue object
    q1 = Queue()
    print("\n      Queue 'q1' object created")

    # DEMO the deque method on an empty queue
    print("\n      Test dequeuing from an empty queue")
    print("      Trying to dequeue from an empty queue...")
    q1.dequeue()
    print("      Result of 'q1.dequeue()' is:", q1.queueItems)

    # DEMO front() on an empty queue
    print("\n      Test viewing the front of an empty queue")
    q1.front()
    print("      Resulting queue values are:", q1.queueItems)

    # ADD 4 items to new queue
    print("\n      Adding 4 items to new queue")
    q1.enqueue(22)
    q1.enqueue(33)
    q1.enqueue(44)
    q1.enqueue(55)
    print("      New queue 'q1' contents are:", q1.queueItems)

    # DEMO FIFO behavior
    print("\n      DEMO removing values adheres to FIFO behavior")
    q1.dequeue()
    print("      Dequeued first value, q1 queue values are now:", q1.queueItems)
    q1.dequeue()
    print("      Dequeued second value, q1 queue values are now:", q1.queueItems)
    q1.dequeue()
    print("      Dequeued third value,  q1 queue values are now:", q1.queueItems)
    q1.dequeue()
    print("      Dequeued fourth value,  q1 queue values are now:", q1.queueItems)



    # Test a single-item queue.
    print("\n    === SINGLE-ITEM QUEUE TEST ===")
    print("      Test viewing the front of an empty queue and")
    print("      verify a single-item queue becomes empty after removal.")
    q2 = Queue()
    q2.enqueue(99)
    print("      Queue before removal:", q2.queueItems)
    q2.dequeue()
    print("      Queue after removal:", q2.queueItems)
    print("      Test the 'is_empty method, the value is", q2.is_empty())


if __name__ == "__main__":
    main()
