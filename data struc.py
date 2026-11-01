"""
arrays_and_strings.py
Collection of foundational algorithms and patterns for arrays and strings in Python.
Topics: Manipulation, Searching, Sliding Window Pattern, and String Parsing.
"""

# 1. MANIPULATION: Rotate an array to the right by k steps
def rotate_array(nums: list, k: int) -> list:
    """Rotates an array to the right by k steps."""
    if not nums: # Check for empty array #this checks if the input list nums is empty. If it is, the function returns the original list without any modifications.
        return nums #this returns the original list nums if it is empty, as there are no elements to rotate.
    k = k % len(nums) #this calculates the effective number of rotations needed by taking the modulus of k with the length of the list nums. This ensures that if k is greater than the length of the list, it wraps around and only performs the necessary rotations.
    return nums[-k:] + nums[:-k] #this returns a new list that is the result of rotating the original list nums to the right by k steps. It does this by slicing the last k elements (nums[-k:]) and concatenating them with the elements before the last k elements (nums[:-k]). This effectively shifts the elements to the right by k positions.


# 2. SEARCHING: Binary Search (assumes a sorted array)
def binary_search(nums: list, target: int) -> int:  #this defines a function named binary_search that takes a list of numbers (nums) and a target number (target) as input. It returns the index of the target in the sorted array if found, or -1 if not found.
    """Finds the index of a target in a sorted array using binary search.""" #string that describes the purpose of the function. It indicates that the function performs a binary search to find the index of the target in a sorted array.
                                                     # Initialize pointers for the search range
    left, right = 0, len(nums) - 1 #this initializes two pointers, left and right, to define the current search range within the sorted array nums. left starts at the beginning of the array (index 0), and right starts at the end of the array (index len(nums) - 1). These pointers will be used to narrow down the search space during the binary search process.
    while left <= right:  #while loop that continues as long as the left pointer is less than or equal to the right pointer. This condition ensures that there are still elements to search within the defined range.
        mid = (left + right) // 2 #this calculates the middle index (mid) of the current search range by taking the average of the left and right pointers. The double slash (//) operator performs integer division, ensuring that mid is an integer index. This mid index is used to check if the target is located at this position or to determine which half of the array to continue searching in.
        if nums[mid] == target: #if statement that checks if the element at the mid index is equal to the target value. If this condition is true, it means the target has been found in the array.
            return mid #this returns the index mid where the target is found in the sorted array. The function exits at this point, providing the result of the search.
        elif nums[mid] < target: #elif statement that checks if the element at the mid index is less than the target value. If this condition is true, it means the target must be located in the right half of the current search range.
            left = mid + 1 #this updates the left pointer to mid + 1, effectively narrowing the search range to the right half of the array. The next iteration of the while loop will continue searching in this new range.
        else:   #else statement that handles the case where the element at the mid index is greater than the target value. If this condition is true, it means the target must be located in the left half of the current search range.
            right = mid - 1 #this updates the right pointer to mid - 1, effectively narrowing the search range to the left half of the array. The next iteration of the while loop will continue searching in this new range.
    return -1  # Target not found 


# 3. SLIDING WINDOW PATTERN: Maximum Subarray Sum of Size K
def max_subarray_sum(nums: list, k: int) -> int: 1
    """Finds the maximum sum of any contiguous subarray of size k using a sliding window."""
    if not nums or k <= 0 or k > len(nums): #this checks if the input list nums is empty, if k is less than or equal to 0, or if k is greater than the length of the list. If any of these conditions are true, the function returns 0, indicating that it's not possible to find a valid subarray sum under these circumstances.
        return 0 #this returns 0 if the input list nums is empty, if k is less than or equal to 0, or if k is greater than the length of the list. This serves as a safeguard against invalid input parameters, ensuring that the function only proceeds with valid conditions for calculating the maximum subarray sum.
    
    # Compute sum of the first window
    window_sum = sum(nums[:k]) #this calculates the sum of the first k elements in the list nums, which represents the initial "window" of size k. The sum function is used to compute the total of these elements, and this value is stored in the variable window_sum. This initial sum serves as a starting point for comparing subsequent sums as the window slides through the array.
    max_sum = window_sum #this initializes the variable max_sum with the value of window_sum. This variable will keep track of the maximum sum encountered as the sliding window moves through the array. Initially, it is set to the sum of the first window, and it will be updated if a larger sum is found in subsequent windows.
    
    # Slide the window across the rest of the array efficiently O(n)
    for i in range(len(nums) - k): #this starts a for loop that iterates over the indices of the list nums, allowing the sliding window to move across the array. The range is set to len(nums) - k, which ensures that the loop only runs for valid starting indices of windows of size k. This loop will efficiently update the window sum by adding the next element and removing the first element of the current window.
        window_sum = window_sum - nums[i] + nums[i + k] #this updates the window_sum by subtracting the element that is leaving the window (nums[i]) and adding the new element that is entering the window (nums[i + k]). This efficient update allows the function to maintain the sum of the current window without having to recalculate it from scratch, thus optimizing performance to O(n) time complexity.
        max_sum = max(max_sum, window_sum) #this updates the max_sum variable by comparing the current max_sum with the updated window_sum. The max function is used to determine which value is larger, and max_sum is set to that value. This ensures that max_sum always holds the maximum sum encountered as the sliding window moves through the array.
    return max_sum #this returns the maximum sum of any contiguous subarray of size k found during the sliding window process. After the loop has completed, max_sum contains the largest sum encountered, and this value is returned as the final result of the function.


# 4. STRING PARSING: Clean and check if a string is a valid palindrome
def is_palindrome(s: str) -> bool: #this defines a function named is_palindrome that takes a string s as input and returns a boolean value indicating whether the string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.   
    """Checks if a string is a palindrome, considering only alphanumeric characters and ignoring case."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


# Example usage and testing
if __name__ == "__main__":
    print("--- 1. Array Manipulation ---")
    original = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original: {original}")
    print(f"Rotated by 3: {rotate_array(original, 3)}")
    
    print("\n--- 2. Searching ---")
    sorted_nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    print(f"Sorted array: {sorted_nums}")
    print(f"Index of {target}: {binary_search(sorted_nums, target)}")
    
    print("\n--- 3. Sliding Window ---")
    nums_sw = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Array: {nums_sw}, k: {k}")
    print(f"Max sum of size {k}: {max_subarray_sum(nums_sw, k)}")
    
    print("\n--- 4. String Parsing ---")
    test_str = "A man, a plan, a canal: Panama"
    print(f"String: '{test_str}'")
    print(f"Is palindrome?: {is_palindrome(test_str)}")
    