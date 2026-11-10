# Introduction to problem
Given a linked list, reverse nodes in k groups as long as the group has k elements. If not, do nothing. Afterwards, chain everything together.

# Logical Steps Taken to Understand Question
1. Getting items in reverse order correlates with popping items off a stack after adding them in forward order. (i.e. stack reverses order)
2. k can be however big, but being 0 makes no sense. "In K groups" mean divided into groups of k units.
3. Okay, so if k cannot be 0, the smallest value must be 1, right? that would mean each group has 1 element, where reverse = foward.
4. k = 2 breaks this. Reverse swaps the order, but hey, we also need to somehow connect the tail of the reversed order to the next sets' head.
5. It feels recursive. Reverse the first group, then link to the next group after we reverse it.

# Logical Steps Taken to Comprehend Reversing First k Nodes
1. Assume k is smaller than the list, and is greater than 1.
2. we want (head + k - 1) -> (head + k - 2) -> ... -> (head) -> (head + k)
3. we have (head) -> (head + 1) -> (head + 2) -> ... -> (head + k - 1) -> (head + k)
4. given 1 indexing from head, we want to pop from the kth node, and compute (k-1th node, kth node) in a function.
5. is that enough information?
6. firstly, once we get to (k-2th node, k-1th node), kth node's original .next is not pointed to, and the reference is no longer in stack mem.
7. therefore we need to propagate this information down the call stack, done via... (parameters or return value)?
8. parameters are set when ADDING to a call stack, return values are set when POPPING from a call stack.
9. therefore we propagate kth node's original .next by returning it along with the node in a tuple.
10. we would also have to do this for the kth node! when we get to the final stack frame, (1st node, kth original .next) we have lost the reference to the new head which is the kth node!
11. so return tuple will be (node, next_seq, new_head), which when paired with the parameters of the stack frame below: node-1, we have enough information to recursively build a reversed linked_list while maintaining the order of the remaining nodes as well as pointer linkage.

# First Solution
1. Written to intermediate variable run BEFORE we stored a reference to the 'tail' node, leaving the original 'tail' node pointing to the original .next of the head, which is now reversed to the last node of the next sequence.
2. Fixed this by storing reference to the tail node BEFORE reversing next group of k nodes, linking it to the new_head AFTER running recursive function.
3. Main errors pertained to mixing up which nodes from before and after states do we need to track during processing; either between recursive calls, or between reverses of groups of k nodes.
