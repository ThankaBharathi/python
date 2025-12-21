'''  
1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given an integer array nums and an integer target.

Your task is to return the indices of the two numbers such that:

They add up to target

Each element can be used only once

Exactly one valid answer exists



'''

'''
2️⃣ Pattern Identification – How to Recognize This Problem
🔹 Pattern: Array + HashMap (Complement Lookup)
🔍 How to detect from problem statement:

Look for these signals:

“Find two numbers”

“Sum equals target”

“Return indices”

“One pass / optimize”

👉 This immediately hints:

“Can I remember previously seen numbers and check if the complement exists?”

🧠 Key Insight:

For every number x, you need to find
target - x

This is a lookup problem → HashMap
'''


'''
3️⃣ Brute Force Approach
💡 Idea

Try every pair (i, j)

Check if nums[i] + nums[j] == target

Return their indices
'''

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

'''
📝 Brute Force Notes (Interview Explanation)

“I check all possible pairs of numbers using two loops.
If any pair sums to the target, I return their indices.
This guarantees correctness but is inefficient because it checks unnecessary pairs.”

📌 Why it works:

Exhaustive checking → no missed case

📌 Why it’s bad:

Repeated comparisons

'''

'''
4️⃣ Optimized Approach (Best Interview Answer)
💡 Core Idea

Use a HashMap to store:

{number : index}

For each number:

Compute complement = target - current_number

Check if complement already exists

'''


def twoSum(nums, target):
    seen = {}  # number -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

'''
📝 Optimized Notes (Interview Explanation)

“I iterate through the array once.
For each number, I calculate the complement needed to reach the target.
If the complement exists in the hash map, I immediately return both indices.
Otherwise, I store the current number and its index for future lookups.”

📌 Why it’s efficient:

Constant-time lookup using HashMap

Single pass

📌 Key Interview Highlight:

Store after checking (prevents using same element twice)

5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n²)

Optimized: O(n)

💾 Space Complexity

Brute Force: O(1)

Optimized: O(n) (HashMap)

🔑 One-Line Memory Hook (For Revision)

“Two Sum = Complement + HashMap + One Pass”

🔥 Interview Tip

If interviewer asks:

“Can you do better than O(n²)?”

👉 Immediately say:

“Yes, using a HashMap to track complements in O(n) time.”

'''