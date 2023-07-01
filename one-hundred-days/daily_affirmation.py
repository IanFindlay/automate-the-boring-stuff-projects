#Daily Affirmation Generator

import time

print(
    "Welcome to the Daily Affirmation Generator! Please answer the following questions to get your affirmation: "
)
time.sleep(1)
print("")

name = input("What is your name? ")
day_of_week = input("What is the current day of the week? ")
favorite_things = input("What are a few of your favorite things? ")
print("")

if day_of_week.lower() == "monday":
    affirmation = "Hey " + name.title(
    ) + "! Start your week with a smile and conquer the day. Remember, " + favorite_things + " bring you joy!"
elif day_of_week.lower() == "tuesday":
    affirmation = "Hello " + name.title(
    ) + "! Embrace the challenges of today with enthusiasm. Your passion for " + favorite_things + " will guide you!"
elif day_of_week.lower() == "wednesday":
    affirmation = "Good day, " + name.title(
    ) + "! You're halfway through the week. Stay focused and let " + favorite_things + " inspire your success!"
elif day_of_week.lower() == "thursday":
    affirmation = "Greetings, " + name.title(
    ) + "! Keep pushing forward. Your dedication to " + favorite_things + " will lead to great accomplishments!"
elif day_of_week.lower() == "friday":
    affirmation = "Happy Friday, " + name.title(
    ) + "! Finish strong and celebrate your achievements. Thinking about " + favorite_things + " and your favorite beverage at the end of the day will make your day even better!"
elif day_of_week.lower() == "saturday":
    affirmation = "Hey there, " + name.title(
    ) + "! Enjoy your weekend and indulge in your favorite things, like " + favorite_things + ". You deserve it!"
elif day_of_week.lower() == "sunday":
    affirmation = "Good morning, " + name.title(
    ) + "! Take some time for yourself today. Relax and cherish your favorite things, like " + favorite_things + "."
else:
    affirmation = "I don't recognize that day. Please enter a valid day of the week."

print(affirmation)

#In the above code, we convert the input day_of_week to lowercase using .lower() to make the if statements case-insensitive. The .title() method is used for the name variable to capitalize the first letter.
