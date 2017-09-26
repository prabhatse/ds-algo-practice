class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        
        start_index = 0
        last_index = 0
        sum = 0
        temp_start = 0
        temp_sum = 0

        #import pdb;pdb.set_trace()

        for i in range(0, len(A)):
            if A[i] >= 0:
                temp_sum += A[i]
            else:
                if temp_sum > sum:
                    start_index = temp_start
                    last_index = i - 1
                    sum = temp_sum
                elif temp_sum == sum:
                    if i - 1 - temp_start > last_index - start_index:
                        start_index = temp_start
                        last_index = i
                temp_start = i + 1
                temp_sum = 0
        if temp_sum > sum or (temp_sum == sum and len(A) - 1 - temp_start > last_index - start_index):
            start_index = temp_start
            last_index = len(A)

        return A[start_index:last_index]


if __name__ == "__main__":
    soln = Solution()
    A = [1, 2, 5, -7, 2, 3]
    print soln.maxset(A)
