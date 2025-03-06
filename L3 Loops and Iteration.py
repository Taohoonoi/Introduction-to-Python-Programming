# Lesson 3: Loops and Iteration

# For Loop
num: list[int] = [0, 1, 2, 3, 4]
names: list[str] = ["Alice", "Bob", "Charlie", "David", "Eve"]
for item in num:
    print(item) # 0, 1, 2, 3, 4

num: list[int] = range(5)
for item in range(5):
    print(item) # 0, 1, 2, 3, 4

# While Loop, keep doing something until a condition is met
count: int = 0
while count < 5: # condition to stop
    count += 1 # increment

# Python does not have a do-while loop, but you can simulate it using a while loop
count: int = 0
while True:
    count += 1
    if count >= 5:
        break