'''
Docstring for Blind-75.maximum_product_subarray
'''

'''
1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given an integer array nums.

Find the contiguous subarray (containing at least one number) which has the largest product, and return that product.

Input:

nums = [2,3,-2,4]


Output:

6


Explanation:
The subarray [2,3] has the maximum product = 6.

2️⃣ Pattern Identification – How to Detect This
🔹 Pattern: Dynamic Programming (Tracking Max & Min)
🔍 How to identify from the problem statement:

Look for these keywords:

“Contiguous subarray”

“Maximum product”

Presence of negative numbers / zeros

👉 This tells us:

“Product can flip sign → I must track both maximum and minimum.”

🧠 Key Insight:

A negative number can turn:

max → min

min → max

So we track:

current_max

current_min

3️⃣ Brute Force Approach
💡 Idea

Generate all subarrays

Compute product for each

Track the maximum

🧪 Brute Force Code (Python)
'''

def maxProduct(nums):
    n = len(nums)
    max_product = nums[0]

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            max_product = max(max_product, product)

    return max_product


'''
📝 Brute Force Notes (Interview Explanation)

“I generate all possible contiguous subarrays and calculate their products.
I keep updating the maximum product found.
This approach is correct but inefficient due to repeated multiplications.”

📌 Why it works:

Checks every possible subarray

📌 Why it’s bad:

High time complexity

4️⃣ Optimized Approach (Best Interview Answer)
💡 Core Idea

Maintain two values at each step:

max product ending here

min product ending here

When current number is negative → swap them

⚡ Optimized Code (Python)
'''

def maxProduct(nums):
    current_max = current_min = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        result = max(result, current_max)

    return result

'''
📝 Optimized Notes (Interview Explanation)

“At each index, I track both the maximum and minimum product ending at that position.
When a negative number appears, the roles of max and min swap.
This allows me to correctly handle sign changes and compute the global maximum product.”

📌 Why it’s efficient:

Single pass

Handles negatives and zeros naturally

📌 Key Interview Highlight:

Tracking minimum product is crucial

5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n²)

Optimized: O(n)

💾 Space Complexity

Brute Force: O(1)

Optimized: O(1)

🔑 One-Line Memory Hook (For Revision)

“Negative flips product → track both max & min”

❗ Common Interview Mistakes

❌ Using Kadane’s sum logic directly

❌ Tracking only maximum

❌ Forgetting to swap on negative numbers

🔥 Interview Follow-Up Questions

Why do we need min?
→ Negative × negative = positive

What about zeros?
→ Logic resets naturally
'''