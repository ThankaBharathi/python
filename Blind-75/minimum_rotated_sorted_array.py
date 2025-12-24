'''
Docstring for Blind-75.minimum_rotated_sorted_array
'''

'''
1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given a rotated sorted array nums of unique elements.

Find and return the minimum element in the array.

The array was originally sorted in ascending order and then rotated.

Input:

nums = [4,5,6,7,0,1,2]


Output:

0

2️⃣ Pattern Identification – How to Detect This
🔹 Pattern: Binary Search on Rotated Sorted Array
🔍 How to identify from the problem statement:

Look for these signals:

“Sorted array”

“Rotated”

“Find minimum / search”

“O(log n) expected”

👉 This directly hints:

“Normal binary search won’t work directly → need modified binary search.”

🧠 Key Insight:

One half of the array is always sorted

The minimum lies in the unsorted half

3️⃣ Brute Force Approach
💡 Idea

Scan the array

Track the minimum element

🧪 Brute Force Code (Python)
'''

# Use Linear search with min Function 
def findMin(nums):
    minimum = nums[0]
    for num in nums:
        minimum = min(minimum, num)
    return minimum



'''
📝 Brute Force Notes (Interview Explanation)

“I scan the entire array and keep track of the smallest element.
This works correctly but does not use the sorted nature of the array.”

📌 Drawback:

Linear time

4️⃣ Optimized Approach (Best Interview Answer)
💡 Core Idea

Use binary search:

Compare nums[mid] with nums[right]

If nums[mid] > nums[right]
→ Minimum is in right half

Else
→ Minimum is in left half (including mid)

⚡ Optimized Code (Python)
'''

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


'''
📝 Optimized Notes (Interview Explanation)

“I apply binary search by comparing the middle element with the rightmost element.
If the middle is greater, the minimum must be on the right side.
Otherwise, it lies on the left including mid.
This reduces the search space by half each time.”

📌 Why this works:

Right side comparison guarantees correctness

Handles all rotation cases

5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n)

Optimized: O(log n)

💾 Space Complexity

Both: O(1)

🔑 One-Line Memory Hook (For Revision)

“nums[mid] > nums[right] → go right, else go left”

❗ Common Interview Mistakes

❌ Comparing with left instead of right

❌ Using linear scan in final answer

❌ Forgetting that array has no duplicates

🔥 Interview Follow-Up Questions

Be ready for:

Search in Rotated Sorted Array

Find minimum with duplicates

Rotation count of array
'''


# if the mid element is greater than right means left to mid array is aldready sorted so that eleminate that other wise right is mid include mid also 