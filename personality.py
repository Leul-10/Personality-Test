#creating variables for every colour
Red = 0
Yellow = 0
Green = 0
Blue = 0

#creating variables that represent an alternative
letter_1 = "A"
letter_2 = "B"
letter_3 = "C"
letter_4 = "D"

#introducing and instructing the user on what to do
print("          Personality Test: Discover Your Dominant Personality Colour!          ")
print("Welcome to the Personality Test!")
print("Please answer the following questions by picking the letter that represents your choice A, B, C, or D.")
print("Remember, there are no right or wrong answers, just be honest and have fun discovering your dominant personality colour!")
print("Let's get started!")

#printing line for organized output and better readability
print("-" * 100)

#asking the user the first question and providing its options
print("1. When starting a new project, what is your primary focus?")
print("  A. Getting immediate results and taking charge.")#red
print("  B. Building strong relationships and ensuring everyone is heard.")#green 
print("  C. Keeping the atmosphere fun and light-hearted.")#yellow
print("  D. Organizing the details and creating a precise plan.")#blue

#asking the user for their answer and converting it to uppercase for consistency
answer_1 = input().strip().upper()

#checking for valid input and prompting the user to enter a valid option if the input is invalid
while answer_1 != letter_1 and answer_1 != letter_2 and answer_1 != letter_3 and answer_1 != letter_4:
    print("1. When starting a new project, what is your primary focus?")
    print("  A. Getting immediate results and taking charge.")#red
    print("  B. Building strong relationships and ensuring everyone is heard.")#green 
    print("  C. Keeping the atmosphere fun and light-hearted.")#yellow
    print("  D. Organizing the details and creating a precise plan.")#blue
    print("Invalid input. Please pick a valid answer between A, B, C, or D.")
    answer_1 = input().strip().upper()

#calculating the score for the first question based on the user's answer
if answer_1 == letter_1:
    Red = Red + 1
elif answer_1 == letter_2:
    Green = Green + 1
elif answer_1 == letter_3:
    Yellow = Yellow + 1
elif answer_1 == letter_4:
    Blue = Blue + 1

#telling the user what they chose for the first question
print("You chose: " + answer_1)

#printing line for organized output and better readability
print("-" * 100)

#asking the user the second question and providing its options
print("2. How do you usually handle a heated argument?")
print("  A. I try to crack a joke or change the subject to lighten the mood.")#yellow
print("  B. I use logic and facts to explain why I am right.")#blue
print("  C. I face it head-on and try to win the point.")#red
print("  D. I try to keep the peace and might give in to avoid conflict.")#green

#asking the user for their answer and converting it to uppercase for consistency
answer_2 = input().strip().upper()

#checking for valid input and prompting the user to enter a valid option if the input is invalid
while answer_2 != letter_1 and answer_2 != letter_2 and answer_2 != letter_3 and answer_2 != letter_4:
    print("2. How do you usually handle a heated argument?")
    print("  A. I try to crack a joke or change the subject to lighten the mood.")#yellow
    print("  B. I use logic and facts to explain why I am right.")#blue
    print("  C. I face it head-on and try to win the point.")#red
    print("  D. I try to keep the peace and might give in to avoid conflict.")#green
    print("Invalid input. Please pick a valid answer between A, B, C, or D.")
    answer_2 = input().strip().upper()

#calculating the score for the second question based on the user's answer
if answer_2 == letter_1:
    Yellow = Yellow + 1
elif answer_2 == letter_2:
    Blue = Blue + 1
elif answer_2 == letter_3:
    Red = Red + 1
elif answer_2 == letter_4:
    Green = Green + 1

print("You chose: " + answer_2)

print("-" * 100)

#asking the user the third question and providing its options
print("3. Which of these best describes your workspace?")
print("  A. A bit messy, filled with colorful or cool items.")#yellow
print("  B. Highly organized, neat, and functional.")#blue
print("  C. Cozy, with photos of family or friends.")#green
print("  D. Efficient and geared toward productivity.")#red

#asking the user for their answer and converting it to uppercase for consistency
answer_3 = input().strip().upper()

#checking for valid input and prompting the user to enter a valid option if the input is invalid
while answer_3 != letter_1 and answer_3 != letter_2 and answer_3 != letter_3 and answer_3 != letter_4:
    print("3. Which of these best describes your workspace?")
    print("  A. A bit messy, filled with colorful or cool items.")#yellow
    print("  B. Highly organized, neat, and functional.")#blue
    print("  C. Cozy, with photos of family or friends.")#green
    print("  D. Efficient and geared toward productivity.")#red
    print("Invalid input. Please pick a valid answer between A, B, C, or D.")
    answer_3 = input().strip().upper()

#calculating the score for the third question based on the user's answer
if answer_3 == letter_1:
    Yellow = Yellow + 1
elif answer_3 == letter_2:
    Blue = Blue + 1
elif answer_3 == letter_3:
    Green = Green + 1
elif answer_3 == letter_4:
    Red = Red + 1

#telling the user what they chose for the third question
print("You chose: " + answer_3)

#printing a line for organized input and better readability
print("-" * 100)

#asking user the fourth question and providing its options
print("4. What action do you find the most annoying and frustrating in others?")
print("  A. Boredom or overly strict rules.")#yellow
print("  B. Indecisiveness or moving too slowly.")#red
print("  C. Inaccuracy or lack of preparation.")#blue
print("  D. Aggression or insensitivity.")#green

#asking user for their answer and converting it to uppercase for consistency
answer_4 = input().strip().upper()

#checking for valid input and prompting the user to enter a valid option if the input is invalid
while answer_4 != letter_1 and answer_4 != letter_2 and answer_4 != letter_3 and answer_4 != letter_4:
    print("4. What action do you find the most annoying and frustrating in others?")
    print("  A. Boredom or overly strict rules.")#yellow
    print("  B. Indecisiveness or moving too slowly.")#red
    print("  C. Inaccuracy or lack of preparation.")#blue
    print("  D. Aggression or insensitivity.")#green
    print("Invalid input. Please pick a valid answer between A, B, C, or D.")
    answer_4 = input().strip().upper()

#calculating the score for the fourth question based on the user's answer
if answer_4 == letter_1:
    Yellow = Yellow + 1
elif answer_4 == letter_2:
    Red = Red + 1
elif answer_4 == letter_3:
    Blue = Blue + 1
elif answer_4 == letter_4:   
    Green = Green + 1

#telling the user what they chose for the fourth question
print("You chose: " + answer_4)

#printing a line for organized output and better readability
print("-" * 100)

#asking the user the fifth question and providing its options
print("5. In a social setting, you are most likely the one who:")
print("  A. Listens intently to others and offers support.")#green
print("  B. Observes the room and stays out of the spotlight.")#blue
print("  C. Directs the group on where to go or what to do.")#red
print("  D. Tells the best stories and keeps people laughing.")#yellow

#asking user for their answer and converting it to uppercase for consistency
answer_5 = input().strip().upper()

#checking for valid input
while answer_5 != letter_1 and answer_5 != letter_2 and answer_5 != letter_3 and answer_5 != letter_4:
    print("5. In a social setting, you are most likely the one who:")
    print("  A. Listens intently to others and offers support.")#green
    print("  B. Observes the room and stays out of the spotlight.")#blue
    print("  C. Directs the group on where to go or what to do.")#red
    print("  D. Tells the best stories and keeps people laughing.")#yellow
    print("Invalid choice! Please pick between A, B, C, or D")
    answer_5 = input().strip().upper()

#instructing the program to calculate the score for the fifth question behind the scenes
if answer_5 == letter_1:
    Green = Green + 1
elif answer_5 == letter_2:
    Blue = Blue + 1
elif answer_5 == letter_3:
    Red = Red + 1
elif answer_5 == letter_4:
    Yellow = Yellow + 1

#telling user their answer
print("You chose: " + answer_5)

#printing a line for organization
print("-" * 100)

#asking the user the sixth question
print("6. How do you make important decisions?")
print("  A. Deliberately, after researching all the data.")#blue
print("  B. Spontaneously, based on what feels exciting.")#yellow
print("  C. Slowly, making sure it doesn't hurt anyone's feelings.")#green
print("  D. Quickly, based on my gut and the bottom line.")#red

#asking user for their answer
answer_6 = input().strip().upper()

#checking for valid input
while answer_6 != letter_1 and answer_6 != letter_2 and answer_6 != letter_3 and answer_6 != letter_4:
    print("6. How do you make important decisions?")
    print("  A. Deliberately, after researching all the data.")#blue
    print("  B. Spontaneously, based on what feels exciting.")#yellow
    print("  C. Slowly, making sure it doesn't hurt anyone's feelings.")#green
    print("  D. Quickly, based on my gut and the bottom line.")#red
    print("Invalid pick! Please pick another answer between A, B, C, or D")
    answer_6 = input().strip().upper()

#instructing the program to calculate the personality based on the user's answer
if answer_6 == letter_1:
    Blue = Blue + 1
elif answer_6 == letter_2:
    Yellow = Yellow + 1
elif answer_6 == letter_3:
    Green = Green + 1
elif answer_6 == letter_4:
    Red = Red + 1

#telling user their answer
print("You chose: " + answer_6)

#printing line for organization
print("-" * 100)

#asking user the seventh question
print("7. What is your ultimate goal in a professional environment?")
print("  A. To achieve power, status, and measurable success.")#red
print("  B. To be liked, recognized, and enjoy the work.")#yellow
print("  C. To achieve perfection and master my craft.")#blue
print("  D. To build meaningful relationships and help others.")#green

#asking user for their answer
answer_7 = input().strip().upper()

#checking for valid input
while answer_7 != letter_1 and answer_7 != letter_2 and answer_7 != letter_3 and answer_7 != letter_4:
    print("7. What is your ultimate goal in a professional environment?")
    print("  A. To achieve power, status, and measurable success.")#red
    print("  B. To be liked, recognized, and enjoy the work.")#yellow
    print("  C. To achieve perfection and master my craft.")#blue
    print("  D. To build meaningful relationships and help others.")#green
    print("Invalid choice! Please pick a valid answer between A, B, C, and D")
    answer_7 = input().strip().upper()

#instructing the program to do calculations behind the scenes
if answer_7 == letter_1:
    Red = Red + 1
elif answer_7 == letter_2:
    Yellow = Yellow + 1
elif answer_7 == letter_3:
    Blue = Blue + 1
elif answer_7 == letter_4:
    Green = Green + 1

#telling user their answer
print("You chose: " + answer_7)

#printing line for organization
print("-" * 100)

#asking user the eighth question
print("8. If you were stranded on a deserted island, what would be your priority?")
print("  A. Building a shelter and finding a way to escape immediately.")#red
print("  B. Making sure everyone is staying calm and getting along.")#green
print("  C. Exploring the island to see what interesting things are there.")#yellow
print("  D. Mapping the terrain and rationing the supplies.")#blue

#asking user for their answer
answer_8 = input().strip().upper()

#checking for valid input
while answer_8 != letter_1 and answer_8 != letter_2 and answer_8 != letter_3 and answer_8 != letter_4:
    print("8. If you were stranded on a deserted island, what would be your priority?")
    print("  A. Building a shelter and finding a way to escape immediately.")#red
    print("  B. Making sure everyone is staying calm and getting along.")#green
    print("  C. Exploring the island to see what interesting things are there.")#yellow
    print("  D. Mapping the terrain and rationing the supplies.")#blue
    print("Invalid choice! Please pick a valid answer between A, B, C, and D")
    answer_8 = input().strip().upper()

#instructing the program to do calculations behind the scenes
if answer_8 == letter_1:
    Red = Red + 1
elif answer_8 == letter_2:
    Green = Green + 1
elif answer_8 == letter_3:
    Yellow = Yellow + 1
elif answer_8 == letter_4:
    Blue = Blue + 1

#telling user their answer
print("You chose: " + answer_8)

print("-" * 100)

#asking user the ninth question
print("9. How do you react to sudden changes in plans?")
print("  A. I adapt quickly as long as we are still moving forward.")#red
print("  B. I feel slightly stressed but go along with the group.")#green
print("  C. I love it! Variety is the spice of life.")#yellow
print("  D. I find it frustrating because it disrupts my schedule.")#blue

#asking user for their answer
answer_9 = input().strip().upper()

#checking for valid input
while answer_9 != letter_1 and answer_9 != letter_2 and answer_9 != letter_3 and answer_9 != letter_4:
    print("9. How do you react to sudden changes in plans?")
    print("  A. I adapt quickly as long as we are still moving forward.")#red
    print("  B. I feel slightly stressed but go along with the group.")#green
    print("  C. I love it! Variety is the spice of life.")#yellow
    print("  D. I find it frustrating because it disrupts my schedule.")#blue
    print("Invalid choice! Please pick a valid answer between A, B, C, and D")
    answer_9 = input().strip().upper()

#instructing the program to do calculations behind the scenes
if answer_9 == letter_1:
    Red = Red + 1
elif answer_9 == letter_2:
    Green = Green + 1
elif answer_9 == letter_3:
    Yellow = Yellow + 1
elif answer_9 == letter_4:
    Blue = Blue + 1

#telling user their answer
print("You chose: " + answer_9)

print("-" * 100)

#asking user the tenth question
print("10. Which word would your friends use to describe you most?")
print("  A. Enthusiastic")#yellow
print("  B. Reliable")#green
print("  C. Logical")#blue
print("  D. Determined")#red

#asking user for their answer
answer_10 = input().strip().upper()

#checking for valid input
while answer_10 != letter_1 and answer_10 != letter_2 and answer_10 != letter_3 and answer_10 != letter_4:
    print("10. Which word would your friends use to describe you most?")
    print("  A. Enthusiastic")#yellow
    print("  B. Reliable")#green
    print("  C. Logical")#blue
    print("  D. Determined")#red
    print("Invalid choice! Please pick a valid answer between A, B, C, and D")
    answer_10 = input().strip().upper()

#instructing the program to do calculations behind the scenes
if answer_10 == letter_1:
    Yellow = Yellow + 1
elif answer_10 == letter_2:
    Green = Green + 1
elif answer_10 == letter_3:
    Blue = Blue + 1
elif answer_10 == letter_4:
    Red = Red + 1

#telling user their answer
print("You chose: " + answer_10)

#printing line for organization
print("-" * 100)

#instructing the program to calculate the dominant personality colour based on the scores and print the results
winner = max(Red, Green, Yellow, Blue)
if winner == Red:
    print("Your dominant personality colour is Red.")
    print("Your core motivation is Power & Control.")
    print("Strengths: Decisive, Assertive, Goal-oriented")
    print("Weaknesses: Impatient, Blunt, Controlling")
elif winner == Green:
    print("Your dominant personality colour is Green.")
    print("Your core motivation is Peace & Harmony.")
    print("Strengths: Loyal, Patient, Good listener")
    print("Weaknesses: Passive, Avoids conflict, Indecisive")
elif winner == Yellow:
    print("Your dominant personality colour is Yellow.")
    print("Your core motivation is Optimism & Enthusiasm.")
    print("Strengths: Energetic, Optimistic, Persuasive")
    print("Weaknesses: Disorganized, Forgetful, Attention-seeking")
elif winner == Blue:
    print("Your dominant personality colour is Blue.")
    print("Your core motivation is Perfection & Order.")
    print("Strengths: Detail-oriented, Analytical, Precise")
    print("Weaknesses: Overly cautious, Resistant to change, Perfectionist")