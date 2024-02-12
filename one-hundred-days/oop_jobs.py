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
    #self.color = color

##### The New Bit ##########

class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    #self.color = color # Only applies to the bird sub class

  def talk(self):
    print(f"{self.name} says {self.sound}")

polly = bird("Green") # Sets polly's colour to 'Green'
polly.talk()
print(polly.color) # Prints polly's color
