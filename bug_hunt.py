count = 1
total = 0

# BUG: The while condition was missing its required colon, so Python could not parse the loop.
# BUG: The loop stopped before 5, so the sum omitted the final number.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The integer total was concatenated with a string; converting it to text fixes the TypeError.
print("Sum of 1 to 5 is: " + str(total))
