"""
class animal:
  species = None
  name = None
  sound = None

  def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
    self.name = name
    self.species = species
    self.sound = sound
    self.color = color

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = "green"

cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
print(cow.sound)

dog = animal("Brian", "Canine", "Woof", "red") # Use the animal class to create a new object called 'dog' with the following parameters.

print(dog.name)

############################################################################
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}"))

dog = animal("Brian", "Canine", "Woof")
dog.talk()
cow = animal("Ermintrude", "Bo Taurus", "Moo")
cow.talk()

############################################################################
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound, color):
    self.name = name
    self.species = species
    self.sound = sound

##### The New Bit ##########

class bird(animal):

  def __init__(self, color): # Add 'color' as a parameter
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color #Initialize the color attribute with the provided parameter

  def talk(self):
    print(f"{self.name} says {self.sound}")

polly = bird("Green") # Sets polly's colour to 'Green'
polly.talk()
print(polly.color) # Prints polly's color
"""

#Day 64 Challenge
#🌟Jobs Jobs Jobs!🌟

print("🌟Jobs Jobs Jobs!🌟")
print()

class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

class doctor(job):
  def __init__(self, salary, hoursWorked, speciality, years):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.speciality = speciality
    self.years = years

  def print(self):
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.speciality:<20} {self.years:>21}")

class teacher(job):
  def __init__(self, salary, hoursWorked, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.subject = subject
    self.position = position

  def print(self):
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

class lawyer(job):
  def __init__(self, salary, hoursWorked, lawyer):
    self.name = "Lawyer"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.lawyer = lawyer

  def print(self):
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.lawyer:<10}")

lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()
doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()
teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()
