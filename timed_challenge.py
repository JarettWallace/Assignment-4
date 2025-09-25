# Pick one question from timed_challenge.txt
# Paste the question as a comment below
#1. Rotate Right
#Rotate the values in a collection to the right by k steps.
#Input: [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
# Set a timer for 30 minutes and complete the question! 



def rotate_right(nums, k):

    if not nums:
        return []
    
    n = len(nums)
    k = k % n 

    return nums[-k:] + nums[:-k] 
input_list = [34, 5, 23, 1999]
k = 2 
output = rotate_right(input_list, k)
print("output:", output) 
