'''
Qn:
🐱 The Binary World of Cats
A group of cats are living in a binary world, where everything is represented in binary format. They have a collection of binary strings and they want to perform a left rotation on each binary string by a certain number of positions. The cats are curious to know the sum of all the rotated binary strings after converting them to decimal form. Can you help them write a function that takes the rotation factor and a set of binary strings as input and returns the sum of all the converted integers?

📝 Input
The first line is a non-negative integer rotationFactor representing the number of positions each binary string should be rotated to the left.
The following lines contain a binary string each.
💻 Output
An integer representing the sum of the converted integers.
⚙️ Constraints
0 <= rotationFactor < length of each binary string.
4 <= length < 32.
💼 Requirements
The function should return an integer representing the sum of the converted integers.
The function should perform the left rotation on each binary string in the input and convert each rotated string to an integer in decimal form.
The function should not exceed a time complexity of O(n), where n is the number of binary strings.
📊 Example
🔢 Input
Copy
2
1010
1011
1100
1101
💾 Output
Copy
34
💡 Explanation
The first binary string 1010 rotated by 2 positions to the left becomes 1010 -> 10 in decimal form.
The second binary string 1011 rotated by 2 positions to the left becomes 1110 -> 14 in decimal form.
The third binary string 1100 rotated by 2 positions to the left becomes 0011 -> 3 in decimal form.
The fourth binary string 1101 rotated by 2 positions to the left becomes 0111 -> 7 in decimal form.
The sum of all the converted integers is 10 + 14 + 3 + 7 = 34.
'''


# ValueError: invalid literal for int() with base 10
# couldn't figure why this error only occur when I concat the binary string.

rotationFactor = int(input())
sum = 0
        
for i in range(4):
    s = input()
    p = s[rotationFactor::] + s[0:rotationFactor]
    sum += int("0b" + p)
    # Solution = int("0b" + p, 2) - Discovered after competition
print(sum)
