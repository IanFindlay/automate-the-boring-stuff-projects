#Multiplication Game

import emoji

print(
    "Name your multiple and answer the problems from the multiplication table")

multiple = int(input("What is your multiple: "))

counter = 1

#Answer 10 questions
for i in range(1, 11):
    print("Question " + str(counter))
    answer = int(input("What is " + str(multiple) + " times " + str(i) + ": "))
    if answer == multiple * i:
        print("Correct!")
        counter += 1
    else:
        print("Incorrect!")

    if counter == 11:
        print("You have answered all the questions correctly!")
        print(emoji.emojize(":smiling_face_with_smiling_eyes:"))

print("")
print("You answered " + str(counter - 1) + " out of 10 questions correctly")
print("Thank you for playing!")
