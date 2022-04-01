# 3. Bond, James Bond
# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

def introduction(first_name, last_name):
  try:
    # check whether strings are empty or not
    if first_name and not first_name.isspace() and last_name and not last_name.isspace():
      return last_name + ", " + first_name + " " + last_name

    else:
      return print("First name and/or last name is empty!")
            
  except:
    return print("Please fill in your first and last name")

output = introduction("elia","cancilleri")

print(output)