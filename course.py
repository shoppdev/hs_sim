import random

last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
    "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright",
    "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez",
    "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez",
    "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson",
    "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly"
]
teacher_titles = [
    "Mr.", "Mrs.", "Ms.", "Miss", "Dr.", "Professor"
]

course_names = [
    "Mathematics", "English Language Arts", "Science", "Social Studies", "History", "Foreign Language",
    "Physical Education", "Computer Science", "Art", "Music", "Drama", "Health Education",
    "Economics", "Government", "Psychology", "Sociology", "Biology", "Chemistry", "Physics",
    "Geography", "Literature", "Creative Writing", "Statistics", "Algebra",
    "Calculus", "Trigonometry", "World History", "European History", "American History",
    "World Geography", "Environmental Science", "Anatomy", "Physiology", "Earth Science",
    "Astronomy", "Political Science", "Anthropology", "Philosophy", "Ethics", "Business",
    "Finance", "Marketing", "Accounting", "Entrepreneurship", "Public Speaking",
    "Journalism", "Broadcasting", "Film Studies", "Digital Media", "Memeology", 
    "Superhero Studies", "Advanced Procrastination", "Extreme Napping Techniques",
    "Unicorn Biology", "Zombie Survival Strategies"
]

class Course:
    def __init__(self, grade_level = 9, passing_grade = 60):
        self.name = list_picker(course_names)
        teach_title = list_picker(teacher_titles)
        teach = list_picker(last_names)
        self.teacher = teach_title + " " + teach
        self.grade_level = grade_level
        self.difficulty = random_num_picker(5, 1) + self.grade_level
        if self.difficulty >= 15:
            self.name = 'Honors ' + self.name
        self.final_grade = 0
        self.passing_grade = passing_grade
    
    def __repr__(self):
        return "Welcom to {course}, the course is taught by {teacher}. The difficulty of this course is {difficulty}.".format(course = self.name, teacher = self.teacher, difficulty = self.difficulty)
    
    def determine_grade(self):
        #grade will be determined by randomness and difficulty add age as determining factor?
        self.final_grade = (random_num_picker(100,70)) - self.difficulty

    def effect_chooser(self):
        # might put this under student
        pass

def random_num_picker(high, low = 0):
    return random.randint(low, high)

def list_picker(name_list, start_num = 0):
    num = random.randint(start_num, len(name_list) - 1)
    return name_list[num]