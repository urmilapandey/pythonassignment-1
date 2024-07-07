#Given a non-empty array of integers nums, every element appears twice except for one. Find 
#that single one. (LeetCode: Single Number) 

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
single_number = 0
for num in nums:
    single_number ^= num
print(f"The single number in the array is: {single_number}")





