from nose.tools import assert_true

class Solution:
    
    def countingSort(self, arr, exp1):
     
        n = len(arr)
     
        # The output array elements that will have sorted arr
        output = [0] * (n)
     
        # initialize count array as 0
        count = [0] * (10)
     
        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (arr[i]/exp1)
            count[ (index)%10 ] += 1
     
        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1,10):
            count[i] += count[i-1]
     
        # Build the output array
        i = n-1
        #import pdb;pdb.set_trace()
        while i>=0:
            index = (arr[i]/exp1)
            output[ count[ (index)%10 ] - 1] = arr[i]
            count[ (index)%10 ] -= 1
            i -= 1
     
        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0,len(arr)):
            arr[i] = output[i]
        return arr
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        max1 = max(A)
        min1 = min(A)
        
        exp1 = 1
        while min1/exp1 > 0:
            exp1 *= 10

        exp = 1
        while max1/exp > exp1 :
            A = self.countingSort(A, exp)
            exp *= 10
        
        s = ''
        for i in range(0, len(A)):
            s = str(A[i]) + s
        return s
    def compare(self,A, i, j):
        x,y = A[i],A[j]
        xy = int(str(x)+str(y))
        yx = int(str(y)+str(x))
        if xy > yx:
            return i
        elif xy == yx:
            return i if x > y else j
        else:
            return j


    def largestNumber1(self, A):
        if not len(A):
            return '0'
        arr = list(A)
        
        for i in range(0,len(A)):
            largest = i
            for j in range(i+1, len(A)):
                largest = self.compare(arr, largest, j)
            arr[i],arr[largest] = arr[largest], arr[i]

        if arr[0] == 0:
            return 0
        s = ''
        #import pdb;pdb.set_trace()
        for i in range(0, len(A)):
            s += str(arr[i])
        return s

if __name__ == "__main__":
    soln = Solution()
    A = [3,30,34,5,9]
    A  = [9,99,999,9999,9998]
    A = [8,89]
    print soln.largestNumber1(A)



