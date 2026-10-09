class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            max = arr[i+1]
            for j in range(i+1,n):
                if arr[j] >= max :
                    max = arr[j]
            arr[i] = max
        arr[-1] = -1

        return arr
              


