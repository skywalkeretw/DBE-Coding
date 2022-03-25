import pyjokes
import funcs
from myClasses import filectr

def isEven(val):
    if val % 2 == 0:
        return True
    return False

def animalLoop():
    animals = ["dog", "cat", "bird", "lion", "snake", "bear", "dragon"]
    for animal in animals:
        print(animal,  "is a cool animal")


if __name__ == '__main__':
    funcs.infoMsg("Hello this small script will give a quick start to python")
    
    #Simple maths and variables
    funcs.infoMsg("Simple Maths")
    a , b = 5 , 4
    ans = a * b
    print("Answer of a * b = ", ans)

    # Maps / assosiated Array
    funcs.infoMsg("Map with some data")
    data = {
        "name": "John Doe",
        "age": 45,
        "employed": True
    }
    funcs.infoMsg("Printing Data Object")
    print(data)
    funcs.infoMsg("Print only age of John")
    print("Age:",data["age"])
    funcs.infoMsg("Change age of John")
    data["age"] = 50
    print("Age:",data["age"])

    # Array
    funcs.infoMsg("Array of Colours")
    colors = ["red", "green", "blue"]
    print(colors)
    funcs.infoMsg("Append yellow to colors")
    colors.append("yelllow")
    print(colors)
    funcs.infoMsg("Get amount of colors")
    l = len(colors)
    print("There are ",l ,"colors")

    # Calling a Function
    funcs.infoMsg("Calling a function that checks if a number is even or odd")
    e = isEven(200)
    print("200 is even: ", e)
    o = isEven(173)
    print("173 is even: ", o)

    # Calling Module
    funcs.infoMsg("Using a Pip Module")
    joke = pyjokes.get_joke()
    print(joke)

    # Calling function with for loop
    funcs.infoMsg("Call Function Containing Loop")
    animalLoop()

    # use function from another file 
    funcs.infoMsg("Use function from another file")
    funcs.helloWorld()

    # File Class
    funcs.infoMsg("Class with File handling")
    fctr = filectr("file.txt")
    fctr.createFile()
    fctr.createFile()
    fctr.writeFile("This is a cool file ")
    fc = fctr.readFile()
    print(fc)