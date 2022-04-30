class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final_output = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                final_output.append("FizzBuzz")
            elif i%3 == 0:
                final_output.append("Fizz")
            elif i%5 == 0:
                final_output.append("Buzz")
            else:
                final_output.append(str(i))
        return final_output
                
