#classes examples 

class MyClass:
    #Constructor
    def __init__(self,nums) -> None:
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size
    
    def getdoublelength(self):
        return 2 * self.getLength()
    

