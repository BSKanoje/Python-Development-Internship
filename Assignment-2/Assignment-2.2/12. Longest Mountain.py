#Problem 845

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        increase = 0
        decrease = 0
        for i in range(1, len(arr)):
         
            if (decrease and arr[i - 1] < arr[i]) or arr[i - 1] == arr[i]:
                increase = decrease = 0

          
            if arr[i - 1] < arr[i]:
                increase += 1
            elif arr[i - 1] > arr[i]:
                decrease += 1

          
            if increase != 0 and decrease != 0:
                longest = max(longest, increase + decrease + 1)
        return longest