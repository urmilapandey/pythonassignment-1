#Given an array of integers nums and an integer target return indices of the two numbers such 
#that they add up to target. You may assume that each input would have exactly one solution, 
#and you may not use the same element twice. You can return the answer in any order. 
#(LeetCode: Two Sum)

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    return []

input_nums = input("Enter numbers separated by spaces: ").split()
nums = list(map(int, input_nums))
target = int(input("Enter the target sum: "))
result = two_sum(nums, target)
if result:
    print(f"Indices of the two numbers that add up to {target}: {result}")
else:
    print("No solution found.")

