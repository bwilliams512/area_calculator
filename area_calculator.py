"""
This is an area calculator that can compute the area
of a circle or triangle.
"""

# inform the user the program is running
print("This area calculator is ready.")


# get input from user and return data
option = input("Enter C for Circle or T for Triangle: ")
   
# now calculate the area of the shape user specifies
if option.lower() == 'c':
    # prompt the user to input the radius
    # float converts a string to a floating point number
    radius = float(input("Enter radius: "))

    # calculate the area of a circle
    area = 3.14159 * radius**2
    print("Area: %f" % area)

# move on to the next shape triangle
elif option.lower() == 't':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    # calculate the area of a triangle
    area = 0.5 * base * height
    print("Area: %f" % area)

else:
    print("Error! Try again.")

print("If we are done, have a great day. Goodbye.")

