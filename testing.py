def containsDuplicate(nums):
    hmap = {}
    for i in nums:
        hmap[i]=hmap[i]+1
        if hmap[i]>=1:
            return False 
        return True
    
num = [1,2,3,1]    
print(containsDuplicate(num))