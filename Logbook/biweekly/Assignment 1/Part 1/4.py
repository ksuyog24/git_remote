'''
4.The sum of digits in the number 4729.
'''
number = 4729
# Convert to string -> iterate digits -> convert back to int -> sum them
total = sum(int(digit) for digit in str(number))
print(total)