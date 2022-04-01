# 4. Dog Years
# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"
# Test this function with your name and your age!

def dog_years(name, age):
  try:
    # check whether strings are empty or not
    if name and not name.isspace():
      convert_int = int(age)
      
      age = age * 7
      #convert int to string for output
      convert_age = str(age)
    
      return name + ", you are " + convert_age + " years old in dog years!"

    else:
      print("Name ist empty!")

  except:
    print("Enter your name and your age")

output = dog_years("Elia", 21)

print(output)