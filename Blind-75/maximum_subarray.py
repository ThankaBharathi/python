'''
Docstring for Blind-75.maximum_subarray
'''

'''
1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given an integer array nums.

Find the contiguous subarray (containing at least one number) which has the largest sum, and return that sum.

Input:

nums = [-2,1,-3,4,-1,2,1,-5,4]


Output:

6


Explanation:
The subarray [4,-1,2,1] has the maximum sum = 6.

2️⃣ Pattern Identification – How to Detect This
🔹 Pattern: Dynamic Programming / Greedy (Kadane’s Algorithm)
🔍 How to identify from the problem statement:

Look for these signals:

“Contiguous subarray”

“Maximum sum”

Negative and positive numbers

👉 This tells us:

“At each index, decide whether to extend the current subarray or start a new one.”

🧠 Key Insight:

If the running sum becomes negative, it hurts future sums, so reset it.

3️⃣ Brute Force Approach
💡 Idea

Generate all possible subarrays

Calculate sum for each

Track the maximum

🧪 Brute Force Code (Python)
'''

def maxSubArray(nums):
    n = len(nums)
    max_sum = nums[0]

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

'''
📝 Brute Force Notes (Interview Explanation)

“I consider every possible contiguous subarray and compute its sum.
I track the maximum sum encountered.
This guarantees correctness but is inefficient due to repeated summations.”

📌 Why it works:

Checks all subarrays

📌 Why it’s bad:

Recalculates sums multiple times

4️⃣ Optimized Approach (Best Interview Answer – Kadane’s Algorithm)
💡 Core Idea

Maintain:

current_sum → best sum ending at current index

max_sum → global maximum

At each index:

Either extend the previous subarray

Or start a new subarray

⚡ Optimized Code (Python)
'''

def maxSubArray(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

'''
📝 Optimized Notes (Interview Explanation)

“I use Kadane’s Algorithm where at each index I decide whether to extend the current subarray or start a new one.
If the running sum becomes negative, I reset it.
This gives the maximum subarray sum in a single pass.”

📌 Why it’s efficient:

One pass

Constant space

📌 Key Interview Highlight:

Greedy decision at every step

5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n²)

Optimized: O(n)

💾 Space Complexity

Brute Force: O(1)

Optimized: O(1)

🔑 One-Line Memory Hook (For Revision)

“If running sum < current element → restart subarray”

❗ Common Interview Mistakes

❌ Resetting sum blindly to 0 (fails all-negative case)

❌ Using extra arrays unnecessarily

❌ Confusing with maximum product subarray

🔥 Interview Follow-Up Questions

All numbers negative?
→ Works correctly because we initialize with nums[0]

Return subarray itself?
→ Track start/end indices
'''


# Suppose they said to print the one sub array means 

def maxSubArrayWithSubarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, nums[start:end + 1]
