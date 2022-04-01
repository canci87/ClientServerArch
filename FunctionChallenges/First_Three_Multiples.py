# 1. First Three Multiples
# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.

def first_three_multiples(num):
  try:
    # Convert num to int to check if value is int
    convert_int = int(num)
    
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3
    
  except:
    # if num not integer
    print("Please enter an integer")
  
output = first_three_multiples("2")

print(output)