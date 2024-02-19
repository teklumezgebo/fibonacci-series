class Solution(object):

    def fibonacci(self, index):

        # initialize list with first 3 values in sequence
        sequence = [0, 1, 1]

        # check if the index exists in the sequence
        while len(sequence) <= index:

            # it it doesn't exist add the next value in the sequence
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)

        # if it does exist return the value at that index 
        else:
            return sequence[index]
        
            

solution = Solution()

print(solution.fibonacci(0))
print(solution.fibonacci(2))
print(solution.fibonacci(10))

print(solution.fibonacci(15))
print(solution.fibonacci(100))
