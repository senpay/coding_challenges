# Coding interview preps
## Data structures and common approaches
| **Category**               | **Approach / Data Structure**      | **Common Use Cases / Notes**                                         |
|----------------------------|------------------------------------|----------------------------------------------------------------------|
| **Arrays & Strings**       | **Sliding Window**                 | Subarrays with sum/k distinct items/patterns; use two pointers; O(n) |
|                            | **Two Pointers**                   | Sorted arrays, merging, palindromes, duplicates, etc.                |
|                            | **Prefix Sum / Difference Array**  | Range sum queries, subarrays with target sum                         |
| **Greedy & Sorting**       | **Greedy Algorithm**               | Interval scheduling, minimizing/maximizing problems                  |
|                            | **Custom Sort / Comparator**       | Sorting by conditions: tuples, strings, priorities                   |
| **Graphs**                 | **DFS / BFS**                      | Traversals, connectivity, shortest path in unweighted graphs         |
| **Trees**                  | **DFS Inorder/Preorder/Postorder** | Tree traversal, path sums, LCA, BST validation                       |
| **DP & Recursion**         | **Memoization / Tabulation**       | Fibonacci, knapsack, edit distance, LIS, climbing stairs             |
| **Backtracking**           | **DFS with Pruning**               | Permutations, combinations, N-Queens, Sudoku                         |
|                            | **GCD / LCM / Primes (Sieve)**     | Coprime checks, factorization                                        |
|                            | **Bit Manipulation**               | Set/clear/test bits, XOR tricks (missing nums, single num in array)  |
| **Useful Data Structures** | **Stacks**                         | Nested structures detection                                          |
|                            | **Heaps & Queues**                 | K largest/smallest, median, merging sorted arrays                    |
|                            | **Hash Map (Frequency Count)**     | Counting, grouping, detecting anagrams, most frequent items          |

## Common data structures time complexity
| **Structure** | **Common Ops**               | **Time Complexity (avg)**   | **Use For**                                        |
|---------------|------------------------------|-----------------------------|----------------------------------------------------|
| Array         | Access, Search, Modify       | O(1), O(n), O(1)            | Contiguous data, binary search, prefix sums        |
| HashMap/Set   | Insert, Delete, Lookup       | O(1)                        | Frequency counts, memoization, uniqueness, mapping |
| Stack / Queue | Push, Pop / Enqueue, Dequeue | O(1)                        | Recursion simulation, BFS/DFS                      |
| Linked List   | Insert, Delete, Traverse     | O(1) for ends, O(n) overall | Reversal, cycle detection                          |
| Heap (PQ)     | Insert, Peek, Pop            | O(log n)                    | Scheduling, top-k problems, greedy optimization    |

## **High-Level Strategy for Solving Problems**

1. **Clarify the problem.** Ask edge cases, size constraints.
2. **Identify type.** Array, graph, tree, etc. Recognize patterns (e.g., "subarray with sum" => sliding window).
3. **Choose the right approach.** Based on input size and operations.
4. **Start brute force.** Then optimize using hash map, sorting, DP, etc.
5. **Write clean code.** Modular, handle edge cases, and add comments.