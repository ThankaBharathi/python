'''
Docstring for Blind-75.search_in_rotated_sorted_array
'''

'''
1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given a rotated sorted array nums of unique integers and an integer target.

Return the index of target if it exists in the array.
Otherwise, return -1.

Input:

nums = [4,5,6,7,0,1,2]
target = 0


Output:

4

2️⃣ Pattern Identification – How to Detect This
🔹 Pattern: Modified Binary Search
🔍 How to identify from the problem statement:

Look for:

“Sorted array”

“Rotated”

“Search element”

Expected O(log n)

👉 This signals:

“Binary search still applies, but with extra conditions.”

🧠 Core Insight:

One half of the array is always sorted

Check which half is sorted

Decide whether the target lies inside that half

3️⃣ Brute Force Approach
💡 Idea

Traverse the array

Compare each element with the target

🧪 Brute Force Code (Python)
'''

# Linear search
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


'''
📝 Brute Force Notes (Interview Explanation)

“I scan through the array and return the index if the target is found.
This guarantees correctness but does not use the sorted property.”

📌 Drawback:

Linear time

4️⃣ Optimized Approach (Best Interview Answer)
💡 Core Idea

Use binary search:

At each step:

Find mid

Determine which half is sorted

Check if target lies in that sorted half

Discard the other half

⚡ Optimized Code (Python)
'''

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


'''
📝 Optimized Notes (Interview Explanation)

“At each step, I identify which half of the array is sorted.
If the target lies within that sorted half, I continue searching there.
Otherwise, I discard it and search the other half.
This ensures logarithmic time complexity.”

📌 Why this works:

Sorted half gives clear boundary conditions

Always reduces search space by half

5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n)

Optimized: O(log n)

💾 Space Complexity

Both: O(1)

🔑 One-Line Memory Hook (For Revision)

“One half is sorted → check target range → discard other half”

❗ Common Interview Mistakes

❌ Forgetting equality (<=) in comparisons

❌ Not checking which half is sorted

❌ Mixing up boundary conditions

🔥 Interview Follow-Up Questions

They may ask:

What if duplicates exist?

Find rotation count

Search range instead of index
'''

# Very simple first find out the sorted area 
# then apply the logic target inbetween the soreted area left to mid or mid to right 
