#Given an integer array nums, return true if any value appears at least twice in the array, and 
#return false if every element is distinct. (LeetCode: Contains Duplicate)

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

input_nums = input("Enter numbers separated by spaces: ").split()
nums = list(map(int, input_nums))
if contains_duplicate(nums):
    print("True.")
else:
    print("False.")

