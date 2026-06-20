def msa(nums):
    cursum=nums[0]
    maxsum=nums[0]
    n=len(nums)
    for i in range(1,n):
        cursum=max(nums[i],cursum+nums[i])
        maxsum=max(cursum,maxsum)
    return maxsum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(msa(nums))

# the kandal algorithm 
# 