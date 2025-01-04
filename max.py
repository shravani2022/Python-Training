#madef find_max(nums):
def find_max(nums):
   if not nums:  
      return None
   else:
    max_num = nums[0] 
    for num in nums: 
      if num > max_num:  
        max_num = num  
      return max_num  

nums = [1, 7, 3, 5, 6]
max_number = find_max(nums)
print(max_number)

nums = []
max_number = find_max(nums)
print(max_number)