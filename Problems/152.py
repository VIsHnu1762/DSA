#Maximum product Subarray
"""
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def mpa(nums):
    n=len(nums)
    cmx,cmi,res=nums[0],nums[0],nums[0]
    for i in range(1,n):
        num=nums[i]
        mx,mi=cmx*nums[i],cmi*nums[i]
        cmx=max(num,mx,mi)
        cmi=min(num,mx,mi)
        res=max(cmx,res,cmi)
    return res



nums = [2,3,-2,4]
print(mpa(nums))
print(nums)



