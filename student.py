import random

first_names = [
    "Emily", "Jacob", "Olivia", "Michael", "Sophia", "Ethan", "Ava", "Matthew", "Isabella", "William",
    "Mia", "Alexander", "Charlotte", "James", "Amelia", "Benjamin", "Harper", "Daniel", "Evelyn", "Joseph",
    "Abigail", "Samuel", "Emily", "David", "Elizabeth", "Henry", "Sofia", "Jackson", "Madison", "Andrew",
    "Avery", "Sebastian", "Ella", "Gabriel", "Scarlett", "Carter", "Grace", "Ryan", "Lily", "John", "Chloe",
    "Luke", "Victoria", "Oliver", "Aria", "Jonathan", "Natalie", "Dylan", "Layla", "Isaac", "Addison", "Nathan",
    "Brooklyn", "Caleb", "Zoe", "Anthony", "Audrey", "Christian", "Savannah", "Landon", "Hannah", "Isaac", "Zoey",
    "Thomas", "Penelope", "Eli", "Leah", "Aaron", "Stella", "Connor", "Aurora", "Cameron", "Claire", "Hunter", "Riley"
]

class Student:
    def __init__(self, grade_level = 9):
        self.name = list_picker(first_names)
        self.age = random_num_picker(15, 13)
        self.grade_level = grade_level
        self.hp = random_num_picker(15, 10)
        self.str = random_num_picker(18, 10)
        self.int = random_num_picker(18, 10)
        self.cha = random_num_picker(18, 10)
        self.grade = 0
    
    def __repr__ (self):
        return '''
{student} is in year {grade}.
\nSTATS:
hp : {hp}
str: {str}
int: {int}
cha: {cha}

STATUS:
{status}
        '''.format(student = self.name, grade = self.grade_level, hp = self.hp, str = self.str, int = self.int, cha = self.cha, status = self.status)

    def create_player(self):
        self.name = input("What is your student first name: ")
        self.age = input("\nWhat is your age: ")
        # self.favorite = input("\nYour favorite food i guess?: ")

    def level_up(self):
        self.age += 1
        self.grade_level += 1
        self.grade = 0

    def add_status(self):
        pass

    def change_stats(self, stat, amount):
        pass

def random_num_picker(high, low = 0):
    return random.randint(low, high)

def list_picker(name_list, start_num = 0):
    num = random.randint(start_num, len(name_list) - 1)
    return name_list[num]