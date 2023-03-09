"""
Qn:
SleepWalking
Alex has a bizarre issue where she sleepwalks at night due to stress at work. To monitor this issue, her mom bought a smart tracking device with advanced technology. This device is able to detect the amount of time in minutes, S, Alex sleepwalks each day. Her mom will monitor for X number of days. If the total amount of time Alex sleepwalks is equal to or more than the threshold of T minutes, her mom will bring Alex to the doctor.

You are tasked to help her mom decide whether Alex needs to see a doctor.

Input format
Your program must read from standard input.

The first line of input contains 2 integers separated with a space. X represents the number of days her mum is monitoring Alex, and T represents the threshold of the total amount of time Alex sleepwalks before her mom brings Alex to see the doctor.

The next line has X number of integers separated with a space, each representing Si, the amount of time in minutes Alex sleepwalk for that particular day.

Output format
Your program must print to standard output.

Your program should output yes if her mom needs to bring Alex to see a doctor or no if her mom does not need to bring Alex to see a doctor. (Note: Ensure output character is in lowercase)

Constraints
The maximum execution time on each instance is 1.0s. Your program will be tested on sets of input instances that satisfy the following limits:

Copy
• 1 ≤ X ≤ 106
• 1 ≤ T ≤ 108
• 0 ≤ Si ≤ 100
Subtask	Marks	Additional Limits
1	30	

~1 <= T <= 10^3
2	70	No further restrictions
Sample Testcase 1
This testcase is valid for all subtasks.

Input	Output
5 10
2 4 6 8 6	yes
Explanation
Alex sleepwalks a total of 2 + 4 + 6 + 8 + 6 = 26 minutes for the 5 days that her mum decided to monitor her.

Since the threshold is 10 minutes, which is less than the total amount she sleepwalked, her mom will take her to the doctor.

Sample Testcase 2
This testcase is valid for all subtasks.

Input	Output
3 50
5 10 15	no
Explanation
Alex sleepwalks a total of 5 + 10 + 15 = 30 minutes for the 3 days that her mum decided to monitor her.

Since the threshold is 50 minutes, which is more than the total amount she sleepwalked, her mom does not need to take her to the doctor.
"""

X = input().split()
Y = input().split()

sum = 0

for item in Y:
    sum += int(item)

if sum >= int(X[1]):
    print("yes")
else:
    print("no")
