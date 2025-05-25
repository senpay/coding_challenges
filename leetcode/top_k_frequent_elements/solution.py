# cool challenge with dicts and heaps

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]

from heapq import heapify, heappop

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # special case: k == number of unique elements
        unique_elements = dict()

        for number in nums:
           element_frequency = unique_elements.get(number, 0) + 1
           unique_elements[number] = element_frequency

        if k == len(unique_elements):
            return list(unique_elements.keys())
        
        # identify unit frequency for elements (still O(N))
        elements_frequency = dict()
        for element, frequency in unique_elements.items():
            elements_with_this_frequency = elements_frequency.get(frequency, [])
            elements_with_this_frequency.append(element) 
            elements_frequency[frequency] = elements_with_this_frequency

        # make a heap from frequencies
        # python only has min heap, so negate number
        frequencies_heap = [-number for number in elements_frequency.keys()]

        # O(N)
        heapify(frequencies_heap)

        # now O(n log n)
        k_elements = []

        # get k elements
        while len(k_elements) < k:
            n_max_frequency = -heappop(frequencies_heap)
            # need to check in case several elements with the same frequency
            elements_to_add = elements_frequency[n_max_frequency]
            if len(elements_to_add) + len(k_elements) <= k:
                k_elements += elements_to_add
            else:
                k_elements += elements_to_add[:k - len(k_elements)]

        return k_elements