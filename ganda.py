def myFunction(x,y):
  if x == 5 and y ==3: 
      print("Hello, world!")    # missing space around operator
  return  x + y #mixed indentation; inconsistent space/tabs

  #function to calculate sum of squares.
  def calc_sum_squares(a,b, c):
    sum_squares = (a**2 + b**2+c**2) # this line is too long, exceeds 79 characters.
  return sum_squares  #  closing parenthesis error

  total =  calc_sum_squares (4 ,3, 6)
    print(total) #  misaligned indentation 

def calculate_area_of_circle(radius):
    # The formula for the area of a circle is πr^2
    area = 3.14 * radius ** 2
    return area

def check_conditions(a,b):
    if a > b:   # incorrect comparison operator usage, should be '==' or '!=', not '='
        print("A is greater than B")  
    elif a == b:
       print("A is equal to B")
    else:
        print("B is greater than A")

print(myFunction(5, 3))   # unclosed comment here
