'''
1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given an integer array nums.

Return True if any value appears at least twice in the array.
Return False if all elements are distinct.

Input:

nums = [1,2,3,1]


Output:

True


Explanation:
The number 1 appears more than once.

'''

'''
2️⃣ Pattern Identification – How to Detect This
🔹 Pattern: Array + HashSet (Frequency / Seen Tracking)
🔍 How to identify from the problem statement:

Look for these keywords:

“Duplicate”

“Appears more than once”

“All elements distinct”

👉 This directly hints:

“I need to remember what I’ve already seen.”

🧠 Key Insight:

Fast membership checking is required

Set / HashMap gives O(1) lookup
'''

'''
3️⃣ Brute Force Approach
💡 Idea

Compare every element with every other element

If any pair is equal → duplicate found

'''

def containsDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

'''
📝 Brute Force Notes (Interview Explanation)

“I compare each element with all elements that come after it.
If any two elements are equal, I immediately return true.
This approach guarantees correctness but is inefficient for large inputs.”

📌 Why it works:

Checks all possible pairs

📌 Why it’s bad:

Unnecessary comparisons
'''

'''
4️⃣ Optimized Approach (Best Interview Answer)
💡 Core Idea

Use a set to store seen elements

While iterating:

If element already exists → duplicate found

Else → add to set
'''

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

'''
📝 Optimized Notes (Interview Explanation)

“I traverse the array once while maintaining a set of seen elements.
Before inserting a number, I check if it already exists in the set.
If it does, I return true immediately.
This avoids unnecessary comparisons and improves performance.”

📌 Why it’s efficient:

Constant-time lookups

Early exit on first duplicate

📌 Key Interview Highlight:

Set membership check is O(1) average
'''

'''
5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n²)

Optimized: O(n)

💾 Space Complexity

Brute Force: O(1)

Optimized: O(n) (Set)

🔑 One-Line Memory Hook (For Revision)

“Duplicate check = Seen set + early return”

❗ Common Interview Mistakes

❌ Sorting first (adds O(n log n) unnecessarily)

❌ Using nested loops in final answer

❌ Forgetting early exit

🔥 Interview Follow-Up

If interviewer asks:

Can you do it without extra space?
→ Yes, by sorting (O(n log n) time, O(1) space)
'''

