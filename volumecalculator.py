import volumes #Importing volume.py file to use the module and the functions associated to calculate volumes

def main(): #Defined as main, this is the main code that will run when initiated and refer to all other functions to perform necessary tasks
    counter = 0 #Set a variable counter to 0, used to count how many times the program is being run
    cubeArray = [] #Declared an empty list called cubeArray to store volumes of the cube
    pyramidArray = [] #Declared an empty list called pyrmaidArray to store volumes of the pyramid
    ellipsoidArray = [] #Declared an empty list called ellipsoidArray to store volumes of the ellipsoid

    while True: #Infinite while loop set to true until it is broken using "break;"
        if counter is 0: #If the program has only ran once, the following will output
            print("Would you like to calculate the volume for a cube, pyramid, or ellipsoid?\n")
            choice = input() #Taking user's input of the shape
            choice = choice.lower() #Converting user's input to all lowercase

        else: #If the counter is not 0 (program has already ran atleast once) the following will output
            print("\nWould you like calculate another volume for a cube, pyramid, ellipsoid or would you like to quit the program?\n")
            choice = input() #Taking user's input if they want to quit or calculate another shape
            choice = choice.lower() #Converting user's input to all lowercase
        
        if choice == 'cube' or choice == 'c': #If user chose cube shape the following will run
            finalVolume = volumes.cubeVolume() #Starting funtion cubeVolume in volume.py file and stores response in variable "finalVolume"
            cubeArray.append(finalVolume) #Adding the stored value in finalVolume to the cube list, named cubeArray
            counter += 1 #Adding one to counter, to keep track of how many times the program has ran

        elif choice == 'p' or choice == 'pyramid': #If user chose pyramid shape the following will run
            finalVolume = volumes.pyramidVolume() #Starting funtion pyramidVolume in volume.py file and stores response in variable "finalVolume"
            pyramidArray.append(finalVolume) #Adding the stored value in finalVolume to the pyramid list, named pyrmaidArray
            counter += 1 #Adding one to counter, to keep track of how many times the program has ran

        elif choice == 'e' or choice == 'ellipsoid': #If user chose ellipsoid shape the following will run
            finalVolume = volumes.ellipsoidVolume() #Starting funtion ellipsoidVolume in volume.py file and stores response in variable "finalVolume"
            ellipsoidArray.append(finalVolume) #Adding the stored value in finalVolume to the ellipsoid list, named ellipsoidArray
            counter += 1 #Adding one to counter, to keep track of how many times the program has ran

        elif choice == 'q' or choice == 'quit': #If user chose to quit the program, the following will run
            if counter is 0: #If no volumes have been calculated the following will run
                print("You have reached the end of your session.")
                print("You did not perform any volume calculations.")
            
            else: #If the program has ran atleast more than once, the following will output
                print("You have reached the end of your session.")
                
            break; #The while loop will break, the the function will stop looping
            
        else:
            print("Invalid input: Please try again!") #The user did not put in a valid input, the program will loop and ask the user to try again
            
    if counter > 0: #The followwing will only output if counter is above 0, therefore a calculation must have been done atleast once.
        
        print("The volume calculated for each shape are: ")
        if not cubeArray: #If there is nothing in the cube list named cubeArray, the following will output
            print("Cube: No shapes entered!")
            
        else: #If there is something in the cube list, the follwoing will output
            cubeArray.sort() #Sorting all the volumes in the cube list from lowest to highest
            print("Cube:", ", ".join(map(str, cubeArray))) #Outputting the volume of the cube by converting it from an array to a string and joining them together

        if not pyramidArray: #If there is nothing in the pyrmaid list named pyramidArray, the following will output
            print("Pyramid: No shapes entered!")
            
        else:
            pyramidArray.sort() #Sorting all the volumes in the pyramid list from lowest to highest
            print("Pyramid:", ", ".join(map(str, pyramidArray))) #Outputting the volume of the pyrmaid by converting it from an array to a string and joining them together

        if not ellipsoidArray: #If there is nothing in the ellipsoid list named ellipsoidArray, the following will output
            print("Ellipsoid: No shapes entered!")
            
        else:
            ellipsoidArray.sort() #Sorting all the volumes in the ellipsoid list from lowest to highest
            print("Ellipsoid:", ", ".join(map(str, ellipsoidArray))) #Outputting the volume of the pyramid by converting it from an array to a string and joining them together

main() #Starting the main function using this line
