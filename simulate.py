import random

# Define the maximum number of days in each month
max_days = {"January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

# Define months globally
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def simulate(num_people):
  # Simulate a room with a certain number of people
  birthdays = [' '.join([random.choice(months), str(random.randint(1, max_days[random.choice(months)]))]) for _ in range(num_people)]
  print("Here's what our room looks like:\n")
  for i, birthday in enumerate(birthdays, start=1):
      print(f"Person {i}'s birthday: {birthday}")
  calculate_probability(num_people)
  if len(birthdays) == len(set(birthdays)):
      print("\n\nIn our simulation, no two people have the same birthday")
  else:
      people = [i+1 for i, birthday in enumerate(birthdays) if birthdays.count(birthday) > 1]
      print("\n\nIn our simulation, the following people have the same birthdays: ")
      for person in people:
          print(f"Person {person}")

def calculate_probability(num_people):
  if num_people < 2:
      print("\n\nNot enough people in the room!")
      return
  numerator = 365
  countdown = 364
  for i in range(2, num_people + 1):
      numerator = numerator * countdown
      countdown -= 1
  denominator = 365 ** num_people
  probability = 1 - numerator/float(denominator)
  rounded = round(probability*100, 2)
  print(f"\n\nThe probability that two people in a room of {num_people} people have the same birthday is nearly {rounded}%")
