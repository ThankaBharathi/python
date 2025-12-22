'''
Docstring for Blind-75.product_array_except_self
'''

'''
1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given an integer array nums.

Return an array answer such that:

answer[i] = product of all elements of nums except nums[i]

❗ Important Constraints

Do NOT use division

Must run in O(n) time

Input:

nums = [1,2,3,4]


Output:

[24,12,8,6]


Explanation:

Index 0 → 2×3×4 = 24

Index 1 → 1×3×4 = 12

Index 2 → 1×2×4 = 8

Index 3 → 1×2×3 = 6

2️⃣ Pattern Identification – How to Detect This
🔹 Pattern: Prefix Product + Suffix Product
🔍 How to identify from the problem statement:

Look for these clues:

“Product of all elements except itself”

“No division allowed”

“Return an array”

👉 This tells us:

“Each index depends on values to the left and right.”

🧠 Key Insight:

For each index i:

answer[i] = (product of left elements) × (product of right elements)

3️⃣ Brute Force Approach
💡 Idea

For every index i

Multiply all elements except nums[i]

🧪 Brute Force Code (Python)
'''

def productExceptSelf(nums):
    n = len(nums)
    result = []

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)

    return result

'''
📝 Brute Force Notes (Interview Explanation)

“For each index, I iterate through the array and multiply all elements except the current one.
This ensures correctness but repeats a lot of multiplications.”

📌 Why it works:

Direct interpretation of the problem

📌 Why it’s bad:

Recomputes products again and again

4️⃣ Optimized Approach (Best Interview Answer)
💡 Core Idea

We do this in two passes:

1️⃣ Prefix pass

Store product of all elements before index i

2️⃣ Suffix pass

Multiply product of all elements after index i

No division, O(n) time.
'''

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

'''
📝 Optimized Notes (Interview Explanation)

“I compute prefix products in the first pass so each index stores the product of elements to its left.
In the second pass, I multiply suffix products representing elements to the right.
This gives the product of all elements except itself in O(n) time without division.”

📌 Why it’s efficient:

No nested loops

No division

Only one result array

📌 Key Interview Highlight:

Uses output array as extra space, allowed by problem

5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n²)

Optimized: O(n)

💾 Space Complexity

Brute Force: O(1) (excluding output)

Optimized: O(1) extra space (output array not counted)

🔑 One-Line Memory Hook (For Revision)

“Answer[i] = left product × right product”

❗ Common Interview Mistakes

❌ Using division

❌ Forgetting zeros case

❌ Creating extra prefix & suffix arrays unnecessarily

🔥 Interview Follow-Up Questions

What if array contains zeros?
→ This approach handles it naturally

Can you do it in one pass?
→ Two passes is optimal & clean
'''