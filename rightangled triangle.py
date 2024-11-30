def triangle ():
    import math
    hyp=int(input("Enter length of first side:"))

    base=int(input("Enter length of second side:"))

    height=int(input("Enter length of third side:"))

    if hyp==math.sqrt(base**2+height**2):

          print("The given triangle is a right triangle.")

    else:

          print("The given triangle is not a right triangle.")
triangle()