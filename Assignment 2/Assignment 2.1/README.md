# 10 Problems in Python

## Overview
This repository contains solutions to 10 common algorithmic problems implemented in Python. Each problem is solved using multiple approaches to highlight different strategies and optimizations.

## Problems and Solutions

### 1. Valid Anagram
**Problem:** Check if two strings are anagrams.
- **Approach 1:** Using `Counter` from `collections`.
- **Approach 2:** Sorting both strings and comparing them.

### 2. First and Last Index
**Problem:** Find the first and last occurrence of a target in a sorted array.
- **Approach 1:** Iterative method with linear search.
- **Approach 2:** Binary search for optimized performance.

### 3. Kth Largest Element
**Problem:** Find the kth largest element in an array.
- **Approach 1:** Iterative removal of maximum elements.
- **Approach 2:** Sorting the array.
- **Approach 3:** Using a min-heap (`heapq`).

### 4. Symmetric Tree
**Problem:** Check if a binary tree is symmetric.
- **Approach:** Recursive traversal of left and right subtrees.

### 5. Generate Parentheses
**Problem:** Generate all valid combinations of n pairs of parentheses.
- **Approach:** Recursive backtracking.

### 6. Gas Station
**Problem:** Find the starting gas station to complete a circular route.
- **Approach 1:** Brute-force approach.
- **Approach 2:** Optimized greedy method.

### 7. Course Schedule
**Problem:** Determine if all courses can be completed given prerequisites.
- **Approach 1:** Depth-first search (DFS).
- **Approach 2:** Kahn's algorithm (topological sorting with BFS).

### 8. Kth Permutation
**Problem:** Find the kth lexicographic permutation of numbers 1 to n.
- **Approach 1:** Using `itertools.permutations`.
- **Approach 2:** Factorial-based index calculations.

### 9. Minimum Window Substring
**Problem:** Find the smallest substring in s that contains all characters of t.
- **Approach 1:** Brute-force method.
- **Approach 2:** Sliding window technique.

### 10. Largest Rectangle in Histogram
**Problem:** Find the largest rectangular area in a histogram.
- **Approach 1:** Brute-force method.
- **Approach 2:** Divide and conquer.
- **Approach 3:** Using a monotonic stack.
