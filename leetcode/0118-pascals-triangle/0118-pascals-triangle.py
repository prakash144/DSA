import math 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def nCr(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
        
        result = []
        for row in range(1, numRows+1):
            #nCr = n! / (r! * (n-r)!)
            tempList = []
            for col in range(1, row+1):
                tempList.append(nCr(row-1, col-1))
            result.append(tempList)
                
        return result
                
            
            
            
        