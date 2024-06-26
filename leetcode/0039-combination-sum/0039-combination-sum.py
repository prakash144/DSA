class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, currComb, total):
            if total == target:
                result.append(currComb.copy())
                return 
            if i >= len(candidates) or total > target:
                return
            
            currComb.append(candidates[i])
            backtrack(i, currComb, total + candidates[i])
            currComb.pop()
            backtrack(i+1, currComb, total)
        
        backtrack(0, [], 0)
        
        return result
