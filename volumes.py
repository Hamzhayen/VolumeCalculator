import math #Importing math library to use PI math constant
PI_CONSTANT = math.pi #Storing the constant PI and in a constant named PI_CONSTANT

def cubeVolume(): #Function defined as cubeVolume, used to calculate volume of a cube
    print("\nPlease enter the length of a side on the cube\n")
    sideLength = float(input()) #Taking user's input for cube length and storing it in variable sideLength
    volume = sideLength ** 3 #Taking sideLength and cubing it to get volume of a cube
    volume = round(volume, 3) #Rounding the answer to three decimal places
    print("\nThe volume of the cube with the side length", sideLength, "is", volume) #Printing out volume for user
    return volume #The volume will get returned to the variable in the main function

def pyramidVolume(): #Function defined as pyramidVolume, used to calculate volume of a pyramid
    print("\nPlease enter the base length of the pyramid")
    baseLength = float(input()) #Taking user's input for the base length of the pyramid
    print("Please enter the height of the pyramid")
    height = float(input()) #Storing user's input of the height of the pyramid
    volume = 1/3 * (baseLength**2) * height #Calculating volume of pyramid using user's input
    volume = round(volume, 3) #Rounding volume to three decimal places
    print("\nThe volume of the pyramid with the base of", baseLength, "and height", height, "is", volume) #Outputting volume to user
    return volume #The volume will get returned to the variable in the main function

def ellipsoidVolume(): #Function defined as ellipsoidVolume, used to calculate volume of an ellipsoid
    print("\nPlease enter the first radius of the ellipsoid")
    radius1 = float(input()) #Taking user's input for the first radius
    print("Please enter the second radius of the ellipsoid")
    radius2 = float(input()) #Taking user's input for the second radius
    print("Please enter the third radius of the ellipsoid")
    radius3 = float(input()) #Taking user's input for the third radius
    volume = 4/3 * PI_CONSTANT * radius1 * radius2 * radius3 #Calculating the volume of the ellipsoid
    volume = round(volume, 3) #Rounding the volume to three decimal places
    print("\nThe volume of the ellipsoid with a radii", radius1, ",",radius2, ",",radius3, "is", volume) #Outputting volume to user
    return volume #The volume will get returned to the variable in the main function

