'''
Docstring for Blind-75.best_time_to_buy_and_sell_stocks
'''
'''

1️⃣ Problem Statement (Clear & Simple)

Problem:
You are given an array prices where prices[i] is the stock price on the iᵗʰ day.

You want to maximize profit by choosing:

One day to buy

One later day to sell

If no profit is possible, return 0.

Input:

prices = [7,1,5,3,6,4]


Output:

5


Explanation:
Buy at price 1 (day 2) and sell at price 6 (day 5).
Profit = 6 - 1 = 5
'''

'''
2️⃣ Pattern Identification – How to Detect This
🔹 Pattern: Greedy + One Pass (Tracking Minimum)
🔍 How to identify from the problem statement:

Look for these signals:

“Buy before sell”

“Maximize profit”

“Only one transaction”

Sequential days → array traversal

👉 This tells us:

“For every day, I need the lowest price so far to buy.”

🧠 Key Insight:

Profit on day i =

prices[i] - minimum_price_before_i


So we track:

Minimum price so far

Maximum profit so far

'''

'''
3️⃣ Brute Force Approach
💡 Idea

Try every possible buy day

Try every possible sell day after buy

Calculate profit and track max

'''

def maxProfit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit

'''
📝 Brute Force Notes (Interview Explanation)

“I check all possible buy–sell pairs where the sell day is after the buy day.
For each pair, I calculate the profit and track the maximum.
This guarantees the correct answer but is inefficient due to nested loops.”

📌 Why it works:

Exhaustively checks all valid transactions

📌 Why it’s bad:

Repeated calculations → slow for large inputs
'''

'''
4️⃣ Optimized Approach (Best Interview Answer)
💡 Core Idea

Track the minimum price so far

For each day:

Calculate profit if sold today

Update max profit

Update minimum price if current price is lower
'''
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

'''
📝 Optimized Notes (Interview Explanation)

“I traverse the array once while keeping track of the lowest price seen so far.
At each step, I calculate the profit if I sell on that day.
I update the maximum profit accordingly.
This ensures buying always happens before selling.”

📌 Why it’s efficient:

One pass

No extra data structures

📌 Key Interview Highlight:

Greedy decision: always buy at the lowest price before today
'''

'''


5️⃣ Time & Space Complexity
⏱ Time Complexity

Brute Force: O(n²)

Optimized: O(n)

💾 Space Complexity

Brute Force: O(1)

Optimized: O(1)

🔑 One-Line Memory Hook (For Revision)

“Track minimum price → compute profit → update max profit”

❗ Common Interview Mistakes

❌ Selling before buying

❌ Trying multiple transactions (this problem allows only one)

❌ Overthinking with DP (greedy is enough)

🔥 Interview Follow-up Questions

If interviewer asks:

Multiple transactions allowed? → Different problem

Cooldown / fee? → DP-based variant
'''

# optimized little bit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
    