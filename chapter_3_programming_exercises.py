
def dayConverter():
    
    day = int(input('Enter a number from 1 - 7: '))
    
    if day == 1:
        
        print('Lunes')
        
    elif day == 2:
        
        print('Martes')
        
    elif day == 3:
        
        print('Miercoles')
        
    elif day == 4:
        
        print('Jueves')
        
    elif day == 5:
        
        print('Viernes')
        
    elif day == 6:
        
        print('Sabado')
        
    elif day == 7:
        
        print('Domingo')
        
    else:
        
        print('Error. Enter a number between 1 and 7 please my sussy baka.')
        

def romanNumerals():
    
    num = int(input('Enter a number between 1 and 10 to convert to a roman numeral: '))
    
    if num == 1:
        
        print('I')
        
    elif num == 2:
        
        print('II')
        
    elif num == 3:
        
        print('III')
        
    elif num == 4:
        
        print('IV')
        
    elif num == 5:
        
        print('V')
        
    elif num == 6:
        
        print('VI')
        
    elif num == 7:
        
        print('VII')
        
    elif num == 8:
        
        print('VIII')
        
    elif num == 9:
        
        print('IX')
        
    elif num == 10:
        
        print('X')
    
    else:
        
        print('Error, please enter a number between 1 and 10.')
        

def romanNumerals2():
    
    num = int(input('Enter a number between 1 and 10 to convert to a roman numeral: '))
    
    roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    
    try:
        
        print(roman[num - 1])
        
    except:
        
        print('Error, please enter a number between 1 and 10.')
        

def colorMixer():
    
    colorOne = input('Enter the first color: ').lower()
    colorTwo = input('Enter the second color: ').lower()
    
    if (colorOne == 'red' and colorTwo == 'blue') or (colorOne == 'blue' and colorTwo == 'red'):
        
        print('You made purple.')
        
    elif (colorOne == 'red' and colorTwo == 'yellow') or (colorOne == 'yellow' and colorTwo == 'red'):
        
        print('You made orange.')
        
    elif (colorOne == 'blue' and colorTwo == 'yellow') or (colorOne == 'yellow' and colorTwo == 'blue'):
        
        print('You made green.')
    
    else:
        
        print('The colors you chose do not combine to make a secondary color.')
        

def hotDog():
    
    import math
    
    attendance = int(input('How many people are coming to the cookout? '))
    limit = int(input('What is the maximum number of hot dogs someone can get? '))
    
    total = attendance * limit
    
    bunAmount = math.ceil(total / 8)
    bunsLeftOver = (bunAmount * 8) - total
    
    hotDogAmount = math.ceil(total / 10)
    hotDogsLeftOver = (hotDogAmount * 10) - total
    
    print('Buns packages needed:', bunAmount)
    print('Buns left over:', bunsLeftOver)
    
    print('Hot Dog packages needed:', hotDogAmount)
    print('Hot Dogs left over:', hotDogsLeftOver)
    

def timeConverter():
    
    secondsInput = int(input('Enter the number of seconds: '))
        
    days = secondsInput // 86400
    hours = (secondsInput % 86400) // 3600
    minutes = ((secondsInput % 86400) % 3600) // 60
    seconds = ((secondsInput % 86400) % 3600) % 60
    
    print('Days:', days)
    print('Hours:', hours)
    print('Minutes:', minutes)
    print('Seconds:', seconds)
    
def leapYear():
    
    year = int(input('Enter a year: '))
    
    if (year % 100) == 0:
        
        if (year % 400) == 0:
            
            print(year, 'is a leap year! There are 29 days in the month of february.')
        
        else:
            
            print(year, 'is not a leap year. There are 28 days in the month of february.')
        
    else:
        
        if (year % 4) == 0:
            
            print(year, 'is a leap year! There are 29 days in the month of february.')
            
        else:
            
            print(year, 'is not a leap year. There are 28 days in the month of february.')
            

        
def sirFixAlot():
    
    print('Reboot computer and try to connect.')
    
    answer = input('Did that fix the problem(Y/N)')
    
    if answer.lower() == 'y':
        
        print('Netflix and Chill')
        
    else:
        
        print('Reboot router and try to connect.')
        
        answer = input('Did that fix the problem(Y/N)')
    
        if answer.lower() == 'y':
        
            print('Netflix and Chill')
        
        else:
        
            print('Verify cables are firmly attached.')
                
            answer = input('Did that fix the problem(Y/N)')
    
            if answer.lower() == 'y':
        
                print('Netflix and Chill')
        
            else:
        
                print('Move router to better location.')
                    
                answer = input('Did that fix the problem(Y/N)')
    
                if answer.lower() == 'y':
        
                    print('Netflix and Chill')
        
                else:
        
                    print('Get a new router.')
        

def canWeJustEat():
    
    vegetarian = input('Is anyone is in your party a vegetarian? (yes/no)').lower()
    vegan = input('Is anyone is in your party a vegan? (yes/no)').lower()
    gluten = input('Is anyone is in your party gluten intolerant? (yes/no)').lower()
    
    print('Here are your resturaunt choices: ')
    
    print('Corner Cafe')
    print("The Chef's Kitchen")
    
    if vegetarian == 'no' and vegan == 'no' and gluten == 'no':
        
        print("Joe's Gourmet Burgers")
        
    if vegan == 'no':
        
        print('Main Street Pizza Company')
        
    if vegan == 'no' and gluten == 'no':
        
        print("Mama's Fine Italian")
            
        
def hitTheTarget():
    
    # Hit the Target Game - 68 and 9
    import turtle
    
    # Named Constants
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TARGET_LLEFT_X = 100
    TARGET_LLEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    
    # Setup the window
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    
    # Draw the target
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    
    
    # Center the turtle
    turtle.goto(0, 0)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)
    
    
    # Get the angle and force from the user
    angle = float(input("Enter the projectile's angle: "))
    force = float(input("Enter the launch force (1-10): "))
    
    
    # Calculate the distance
    distance = force * FORCE_FACTOR
    
    
    # Set the heading
    turtle.setheading(angle)
    
    
    # Launch the projectile
    turtle.pendown()
    turtle.forward(distance)
    
    
    # Did it hit the target?
    if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        
        print('Target hit!')
        
    else:
        
        print('You missed the target.')