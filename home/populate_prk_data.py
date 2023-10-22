#Import the model class and the random module
#from .models import prk
#import random

#List of Indian names (you can expand this list)
indian_names = [
    "Aarav",
    "Aditi",
    "Aishwarya",
    "Amit",
    "Ananya",
    "Deepak",
    "Divya",
    "Gaurav",
    "Isha",
    "Kunal",
    "Amey",
    "Rahul",
    "Chaitanya",
    "Andreaz",
    "Soham",
    "Aditya",
    'Vedant',
    "Rohit",
    "Rishab",
    "Ahaan",
    "Ajinkya",
    "Edith",
    "Huzaifa",
    "Uzair",
    "Ramesh",
    "Elizabeth",
    "Rose",
    "Charles",
    "Jake"

]

used_prkno = set()

# Initialize 'fltn' value to 100
fltn_value = 100

# Define a function to generate a unique random 'prkno'
def generate_unique_prkno():
    while True:
        prkno = random.randint(1, 100)
        if prkno not in used_prkno:
            used_prkno.add(prkno)
            return prkno

# Define a function to generate a random 'd_in' value
def generate_random_d_in():
    # Generate a random time between 1650 and 2150
    time = random.randint(16, 21)

    # Limit the last two digits to be 59 or less
    last_two_digits = min(random.randint(0, 59), 59)
    last_two_digits = last_two_digits - (last_two_digits % 15)

    # Combine the time and last_two_digits to create 'd_in'
    d_in = f"{time:02d}{last_two_digits:02d}"

    return d_in

# Define a function to generate a random 'd_out' value
def generate_random_d_out():
    # Generate a random time between 0600 and 1140
    time = random.randint(6, 11)

    # Ensure it's a multiple of 15

    # Limit the last two digits to be 59 or less
    last_two_digits = min(random.randint(0, 59), 59)
    last_two_digits = last_two_digits - (last_two_digits % 15)
    # Combine the time and last_two_digits to create 'd_out'
    d_out = f"{time:02d}{last_two_digits:02d}"

    return d_out

# Define a function to generate a random 'dist' value between 1 and 15
def generate_random_dist():
    return random.randint(1, 15)

# Create instances with the desired 'fltn', 'prkno', 'name', 'emp', 'd_in', 'd_out', 'dist', and 'wing' values
for _ in range(1104):  # Create 1104 instances
    if fltn_value % 100 <= 4:
        name = random.choice(indian_names)
        prkno = str(generate_unique_prkno())
        d_in = generate_random_d_in()
        d_out = generate_random_d_out()
        dist = generate_random_dist()
        wing = 'F'  # Set 'wing' to 'A'
        prk.objects.create(fltn=str(fltn_value), prkno=prkno, name=name, emp=True, d_in=d_in, d_out=d_out, dist=dist,
                           wing=wing)
        # Increment 'fltn' by 1
    fltn_value += 1


