"""
Qn:
🐱 Designing a Cat Playground
Once upon a time, there was a group of cats who loved to play and jump around. One day, their caretaker 🙋‍♀️ decided to build them a playground with a specially designed cat tree. The cat tree had several standing posts of different heights to keep the cats entertained.

To ensure the cats could jump and play to their hearts' content, the caretaker needed to design the playground carefully. They had an array of integers that represented the average height that a cat could jump, and two integers minK and maxK that represented the minimum and maximum heights of the standing posts from the floor.

The caretaker wanted to make sure that the playground had several fixed-bound subarrays - contiguous parts of the array where the minimum value was equal to minK and the maximum value was equal to maxK. They needed to know how many fixed-bound subarrays there were in the array so they could build the playground accordingly 🤔.

To solve this problem, the caretaker decided to write a program that would count the number of fixed-bound subarrays in the array. They knew that dynamic programming could be used to solve this problem efficiently, so they set to work designing an algorithm that would work for any array of integers and values of minK and maxK.

📥 Input
The first line includes the integer value minK followed by maxK.
The second line contains an array of integers representing the average height that a cat can jump.
📤 Output
The number of fixed-bound subarrays in nums. A fixed-bound subarray is a subarray where the minimum value is equal to minK and the maximum value is equal to maxK.

🚧 Constraints
2 <= nums.length <= 1,048,576
1 <= nums[i], minK, maxK <= 231 - 1
minK <= maxK
Example 1
📥 Input
Copy
1 6
1 7 1 4 6 2 6 4 6
📤 Output
Copy
5
💡Explanation
The highlighted subarray is the one that includes both the minimum value minK and the maximum value maxK.

Copy
1 7 ==1 4 6== 2 6 4 6
1 7 ==1 4 6 2== 6 4 6
1 7 ==1 4 6 2 6== 4 6
1 7 ==1 4 6 2 6 4== 6
1 7 ==1 4 6 2 6 4 6==
Example 2
📥 Input
Copy
1 6
1 6 4 3 7 7 7 4 2 1 4 6 2 6 2 7 5 6
📤 Output
Copy
15
💡Explanation
The highlighted subarray is the one that includes both the minimum value minK and the maximum value maxK.

Copy
==1 6== 4 3 7 7 7 4 2 1 4 6 2 6 2 7 5 6
==1 6 4== 3 7 7 7 4 2 1 4 6 2 6 2 7 5 6
==1 6 4 3== 7 7 7 4 2 1 4 6 2 6 2 7 5 6
1 6 4 3 7 7 7 ==4 2 1 4 6== 2 6 2 7 5 6
1 6 4 3 7 7 7 ==4 2 1 4 6 2== 6 2 7 5 6
1 6 4 3 7 7 7 ==4 2 1 4 6 2 6== 2 7 5 6
1 6 4 3 7 7 7 ==4 2 1 4 6 2 6 2== 7 5 6
1 6 4 3 7 7 7 4 ==2 1 4 6== 2 6 2 7 5 6
1 6 4 3 7 7 7 4 ==2 1 4 6 2== 6 2 7 5 6
1 6 4 3 7 7 7 4 ==2 1 4 6 2 6== 2 7 5 6
1 6 4 3 7 7 7 4 ==2 1 4 6 2 6 2== 7 5 6
1 6 4 3 7 7 7 4 2 ==1 4 6== 2 6 2 7 5 6
1 6 4 3 7 7 7 4 2 ==1 4 6 2== 6 2 7 5 6
1 6 4 3 7 7 7 4 2 ==1 4 6 2 6== 2 7 5 6
1 6 4 3 7 7 7 4 2 ==1 4 6 2 6 2== 7 5 6
Example 3
📥 Input
Copy
3 7
7 3 1 4 6 1 3 7 4 6
📤 Output
Copy
4
💡Explanation
The highlighted subarray is the one that includes both the minimum value minK and the maximum value maxK.

Copy
==7 3== 1 4 6 1 3 7 4 6
7 3 1 4 6 1 ==3 7== 4 6
7 3 1 4 6 1 ==3 7 4== 6
7 3 1 4 6 1 ==3 7 4 6==
"""

# Solution Submitted
from sys import stdin

minK, maxK = stdin.readline().rstrip().split()
cats = list(input().split())

sum = 0

for i in range(len(cats)):
    
    if int(minK) <= int(cats[i]) <= int(maxK):
        sum += 1

print(sum)
