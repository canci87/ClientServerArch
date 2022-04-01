# 2. Tip
# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
  try:
    convert_int = int(total)
    convert_int = int(percentage)
    
    return (total * percentage) / 100
    
  except:
    print("Please enter integers for total and percentage")

output = tip(150, 20)

print(output)