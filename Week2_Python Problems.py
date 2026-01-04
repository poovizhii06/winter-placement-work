# Week 2 - Python Problem Practice

# 1. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Find largest of three numbers
a, b, c = 10, 25, 15
print("Largest:", max(a, b, c))

# 3. Count vowels in a string
text = "placement"
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)

# 4. Reverse a string
print(text[::-1])

# 5. Factorial
fact = 1
n = 5
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)
