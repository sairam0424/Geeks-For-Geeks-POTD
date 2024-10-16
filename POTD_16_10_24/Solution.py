

class Solution:
    def checkSorted(self, arr):
        #code her
        ct = 0
        i = 0
        while i < len(arr):
            if arr[i] == i + 1:
                i += 1
                continue
            else:
                arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
                ct += 1
        return ct == 0 or ct == 2
            
            