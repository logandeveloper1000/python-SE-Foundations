#Even or Odd
def even_or_odd(number):
  return "Even" if number % 2 == 0 else "Odd"

print (even_or_odd(10))

#Convert a Number to a String
def number_to_string(num):
  return str(num)

print(number_to_string(123))

#Remove String Spaces
def no_space(x):
  return x.replace(" ", "")
print(no_space("A B C       V W X Y Z"))  
