'''
Qn:
🔍 The Secret Agent's Adventure
A group of spies has infiltrated a secret facility, and you are tasked with finding them. The spies have been assigned unique code numbers, and the information about the code numbers is stored in an array. Your job is to find the spy with a specific code number.

You are given an array of n elements, each representing a code number of one of the spies. Your task is to find the code number of the spy you are looking for. You are also given the range of the code numbers, which is from 1 to 2 31 - 1.

To make your search more efficient, you need to first sort the array of code numbers. After sorting, you can use a specific search technique to find the code number of the spy you are looking for.

Can you find the spy?

📝 Input
The input is read from standard input.

An integer n representing the total number of spies (size of array).
An array arr of the code numbers of the spies
An integer key representing the code number of the spy you are searching for.
💻 Output
The index of the spy with the code number key in the sorted array, or -1 if the spy with the code number key is not found.
⚙️ Constraints
1 <= n <= 216 - 1
1 <= arr[i], key <= 231 - 1
💼 Requirements
Your solution should sort the array of code numbers and then search for the code number of the spy you are looking for in an efficient manner.

Please note that you are NOT allowed to utilize any built-in sort or search functions provided in the libraries of the programming languages you are using (e.g. the C+Standard Template Library (STL)).

📊 Example
🔢 Input
Copy
5
1 3 5 2 4
2
💾 Output
Copy
1
💡 Explanation
The code numbers of the spies are 1 3 5 2 4. After sorting, the array becomes 1 2 3 4 5. The code number of the spy you are searching for is 2, and it is located at index 1 in the sorted array.
'''
# Score: 50/100
"""
Batch #1 (25/25 points)
Case #1:	AC	[0.052s,	10.46 MB]
Case #2:	AC	[0.051s,	10.39 MB]
Case #3:	AC	[0.050s,	10.43 MB]
Case #4:	AC	[0.052s,	10.51 MB]
Case #5:	AC	[0.052s,	10.43 MB]

Batch #2 (25/25 points)
Case #1:	AC	[0.051s,	10.38 MB]
Case #2:	AC	[0.053s,	10.42 MB]
Case #3:	AC	[0.057s,	10.39 MB]
Case #4:	AC	[0.072s,	10.40 MB]
Case #5:	AC	[0.115s,	10.53 MB]

Batch #3 (0/25 points)
Case #1:	AC	[0.300s,	10.48 MB]
Case #2:	AC	[1.025s,	10.50 MB]
Case #3:	TLE	[>2.000s,	10.73 MB]
Case #4:	—		
Case #5:	—		

Batch #4 (0/25 points)
Case #1:	TLE	[>2.000s,	12.77 MB]
Case #2:	—		
Case #3:	—		
Case #4:	—		


Resources: ---, 12.77 MB
Final score: 50/100 (50.0/100 points)
"""

from sys import stdin

n = int(input())
arr = list(stdin.readline().split())
key = input()

s_arr = []

while n > 0:
    
    start = arr[-1]
    
    for i in range(0, n):
            
        if int(start) > int(arr[i]):
            start =  arr[i]
        
    s_arr.append(start)
    arr.remove(start)
    n -= 1

c = False
        
for i in range(len(s_arr)):
    if key == s_arr[i]:
        print(i)
        c = True
        break

if c == False:
    print(-1)

