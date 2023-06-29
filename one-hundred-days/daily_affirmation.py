#Daily Affirmation Generator

import random
import time

positive = ["You are a great person!", "You are a wonderful person!", "You are a beautiful person!", "You are a smart person!", "You are a kind person!", "You are a loving person!", "You are a caring person!", "You are a strong person!", "You are a brave person!", "You are a confident person!", "You are a powerful person!", "You are a successful person!", "You are a talented person!", "You are a unique person!", "You are a special person!", "You are a good person!", "You are a great person!", "You are a wonderful person!", "You are a beautiful person!", "You are a smart person!", "You are a kind person!", "You are a loving person!", "You are a caring person!", "You are a strong person!", "You are a brave person!", "You are a confident person!", "You are a powerful person!", "You are a successful person!", "You are a talented person!", "You are a unique person!", "You are a special person!"]
negative = ["You are a bad person!", "You are a terrible person!", "You are an ugly person!", "You are a dumb person!", "You are a mean person!", "You are a hateful person!", "You are a selfish person!", "You are a weak person!", "You are a cowardly person!", "You are an insecure person!", "You are a powerless person!", "You are a failure!", "You are a talentless person!", "You are a boring person!", "You are a normal person!", "You are a regular person!", "You are a bad person!", "You are a terrible person!", "You are an ugly person!", "You are a dumb person!", "You are a mean person!", "You are a hateful person!", "You are a selfish person!", "You are a weak person!", "You are a cowardly person!", "You are an insecure person!", "You are a powerless person!", "You are a failure!", "You are a talentless person!", "You are a boring person!", "You are a normal person!", "You are a regular person!"]
neutral = ["You're an ok person"]

affirmations = [positive, negative, neutral]

print("Welcome to the Daily Affirmation Generator!")
time.sleep(1)
print("This program will generate a random affirmation for you!")
time.sleep(1)
print("Let's begin!")
time.sleep(1)
print("Your affirmation is...")
time.sleep(1)
print(random.choice(affirmations))
time.sleep(1)
print("Thank you for using the Daily Affirmation Generator!")
