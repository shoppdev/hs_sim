# INCLUDES

import random

# VARS

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
first_names = [
    "Emily", "Jacob", "Olivia", "Michael", "Sophia", "Ethan", "Ava", "Matthew", "Isabella", "William",
    "Mia", "Alexander", "Charlotte", "James", "Amelia", "Benjamin", "Harper", "Daniel", "Evelyn", "Joseph",
    "Abigail", "Samuel", "Emily", "David", "Elizabeth", "Henry", "Sofia", "Jackson", "Madison", "Andrew",
    "Avery", "Sebastian", "Ella", "Gabriel", "Scarlett", "Carter", "Grace", "Ryan", "Lily", "John", "Chloe",
    "Luke", "Victoria", "Oliver", "Aria", "Jonathan", "Natalie", "Dylan", "Layla", "Isaac", "Addison", "Nathan",
    "Brooklyn", "Caleb", "Zoe", "Anthony", "Audrey", "Christian", "Savannah", "Landon", "Hannah", "Isaac", "Zoey",
    "Thomas", "Penelope", "Eli", "Leah", "Aaron", "Stella", "Connor", "Aurora", "Cameron", "Claire", "Hunter", "Riley"
]
student_list = []

# Events
funny_events = {
    "The class pet, a turtle, decides to take a stroll during the lesson, causing a slow-speed chase around the room": "Students' intelligence decreases as they get distracted by the turtle.",
    "The classmate with a talent for beatboxing suddenly bursts into an impromptu performance, disrupting the class": "Charisma suffers as students struggle to focus amidst the noise.",
    "The classroom's resident prankster releases a swarm of plastic bugs, sparking panic": "Strength improves slightly as students jump out of their seats in fright.",
    "The teacher accidentally spills coffee on their shirt, leading to an impromptu fashion statement": "Intelligence takes a hit as students struggle to keep a straight face.",
    "The class computer malfunctions, displaying memes instead of the lesson slides": "Charisma improves as students bond over the humor.",
    "A sudden outbreak of contagious laughter spreads through the classroom, disrupting the lesson": "Intelligence decreases as students struggle to regain composure.",
    "A group of birds perched outside the window starts singing in unison, distracting everyone": "Charisma improves as students enjoy the unexpected concert.",
    "A stray cat wanders into the classroom and decides to take a nap on a student's desk": "Intelligence suffers as students find it hard to focus with the adorable distraction.",
    "The classmate known for elaborate pranks sets up a fake spider, causing chaos when it's discovered": "Strength increases as students jump out of their seats in fright.",
    "The teacher accidentally sets off the classroom's emergency alarm instead of the projector": "Charisma takes a hit as students try to stifle their laughter.",
    "A sudden gust of wind blows all the papers off the teacher's desk, creating a paper tornado": "Strength improves slightly as students rush to help gather the papers.",
    "The class clown starts a spontaneous game of 'Simon Says', causing confusion and laughter": "Intelligence decreases as students get caught up in the game.",
    "A science experiment goes awry, resulting in a small explosion that covers everyone in foam": "Charisma improves as students bond over the unexpected mess.",
    "The classmate with a knack for magic tricks pulls off an impressive illusion, surprising everyone": "Intelligence takes a hit as students try to figure out how the trick was done.",
    "The teacher accidentally plays the wrong video, revealing embarrassing footage from the last school play": "Charisma takes a hit as students try to hide their embarrassment."
}
disaster_events = {
    "Aliens abduct the entire classroom, causing widespread panic and confusion": "Students' hit points decrease as they are transported into the alien spacecraft.",
    "A rift in the space-time continuum opens up, transporting the classroom to a parallel universe": "Intelligence takes a hit as students try to comprehend their new surroundings.",
    "A giant mutant hamster rampages through the classroom, devouring everything in its path": "Strength decreases as students try to avoid being eaten by the mutant hamster.",
    "The classroom is engulfed by a sudden tornado made entirely of textbooks": "Charisma suffers as students try to dodge flying textbooks.",
    "A horde of zombie students rises from the ground, hungry for brains": "Students' hit points decrease as they fend off the zombie horde.",
    "A portal to the underworld opens beneath the classroom, releasing a swarm of demons": "Intelligence takes a hit as students try to banish the demons back to the underworld.",
    "The classroom is teleported to the top of a snowy mountain, leaving everyone freezing cold and stranded": "Strength decreases as students try to stay warm and find a way down the mountain.",
    "A mad scientist's experiment goes awry, transforming everyone in the classroom into chickens": "Charisma suffers as students cluck and peck at each other in confusion.",
    "A rogue AI takes control of the classroom's electronics, turning them into killer robots": "Students' hit points decrease as they dodge the attacks of the killer robots.",
    "The classroom is swallowed by a giant sinkhole, plummeting into the depths of the earth": "Intelligence takes a hit as students try to navigate the underground caverns.",
    "A swarm of giant mutant mosquitoes invades the classroom, sucking blood from everyone inside": "Charisma suffers as students try to swat away the giant mosquitoes.",
    "The classroom is transported to a deserted island, surrounded by sharks and hungry wildlife": "Strength decreases as students try to survive and find a way back home.",
    "A freak lightning storm strikes the classroom, imbuing everyone with unpredictable superpowers": "Students' hit points decrease as they struggle to control their newfound abilities.",
    "The classroom is engulfed in a whirlwind of candy, causing chaos and sugar-induced madness": "Intelligence takes a hit as students succumb to the sugar rush.",
    "A giant squid emerges from the floor, spraying ink everywhere and causing chaos": "Charisma suffers as students try to avoid getting covered in squid ink."
}
safe_events = {
    "The class is visited by a group of friendly aliens who offer to help with homework": "Students' hit points increase as they receive alien assistance with their assignments.",
    "The teacher declares it 'Opposite Day', leading to hilarious misunderstandings and antics": "Charisma improves as students embrace the silliness of Opposite Day.",
    "The school's mascot challenges the class to a dance-off, resulting in laughter and fun": "Intelligence increases as students showcase their dance moves and creativity.",
    "The classroom is transformed into a giant pillow fort, complete with blankets and stuffed animals": "Students' hit points increase as they relax and enjoy the cozy atmosphere of the pillow fort.",
    "A group of clowns visits the classroom and puts on a silly performance, eliciting laughter from everyone": "Charisma improves as students enjoy the comedic antics of the clowns.",
    "The teacher announces a surprise pajama day, allowing everyone to come to class in their comfiest sleepwear": "Intelligence increases as students feel relaxed and comfortable in their pajamas.",
    "The class is treated to a magic show performed by a talented magician, leaving everyone amazed and entertained": "Students' hit points increase as they marvel at the magic tricks and illusions.",
    "The school cafeteria serves up a bizarre but delicious new dish that becomes an instant hit among the students": "Charisma improves as students bond over their love for the strange new dish.",
    "The classroom is invaded by a group of friendly ghosts who offer to help with classwork and assignments": "Intelligence increases as students receive ghostly assistance with their studies.",
    "The teacher leads the class in a spontaneous karaoke session, belting out cheesy pop songs together": "Students' hit points increase as they enjoy singing and dancing along to their favorite tunes.",
    "The school announces a surprise puppy day, bringing in a bunch of adorable puppies for the class to play with": "Charisma improves as students cuddle and play with the cute puppies.",
    "The class participates in a wacky hat day, with students wearing outrageous hats of all shapes and sizes": "Intelligence increases as students get creative with their wacky hat designs.",
    "The classroom is transformed into a giant ball pit, providing endless fun and laughter for everyone": "Students' hit points increase as they dive into the ball pit and enjoy the playful atmosphere.",
    "The school organizes a silly string fight in the gymnasium, with students spraying each other with colorful string": "Charisma improves as students engage in friendly competition and silliness.",
    "The teacher announces a surprise visit from the Tooth Fairy, who leaves a special treat for everyone in the class": "Intelligence increases as students enjoy the magical surprise from the Tooth Fairy."
}



# CLASSES

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

# # # # # #
def list_picker(name_list, start_num = 0):
    num = random.randint(start_num, len(name_list) - 1)
    return name_list[num]

def random_num_picker(high, low = 0):
    return random.randint(low, high)

def event_manager(student_list):
    event_type = None
    up_down_list = [1, -1]

    # Event type picking -- 15% - disaster - 25% - funny - 25% - safe - 35% - nothing
    num = random_num_picker(100)
    if num >= 0 and num < 15:
        event_type = 'disaster'
        event_list = disaster_events
    elif num >= 15 and num < 40:
        event_type = 'funny'
        event_list = funny_events
    elif num >= 40 and num < 65:
        event_type = 'safe'
        event_list = safe_events
    else:
        event_type = 'nothing'
    
    if event_type != 'nothing':

        # Pick the event using event type
        event_choice = key, value = random.choice(list(event_list.items()))

        # Break up the event into event and result
        event_desc = event_choice[0]
        event_result = event_choice[1]

        # Pick affected students and assign them to a list
        affected_students = []
        num_students = random_num_picker(len(student_list))

        for num in range(num_students):
            temp_stud =(student_list[random_num_picker(len(student_list) - 1)])
            if temp_stud in affected_students:
                pass
            else:
                affected_students.append(temp_stud)

        # Change the stat
        for student in affected_students:
            if event_type == 'disaster':
                student.hp += -5
            elif event_type == 'funny':
                if random_num_picker(2) == 1:
                    student.hp += 2
                else:
                    student.hp += -5
            elif event_type == 'safe':
                student.hp += 2
            else:
                print("the is probebly doing nothing")
        print(event_desc)
        print(event_result)
    else:
        print('Nothing signigfigant happend this quarter')



# calculation for determining student grade
def grade_manager(student_list, course):
    for student in student_list:
        student.grade = (75 + student.int) - (course.difficulty + random_num_picker(20))
        print(student.name, student.grade)

def class_quarter(course, student_list):
    print('This quarter we are going to learn all about {course}. This class is taught by {teacher}.'.format(course = course.name, teacher = course.teacher))
    print('\nClass List: ')
    for student in student_list:
        print("{student} - Age: {age} - HP: {hp}".format(student = student.name, age = student.age, hp = student.hp))

    fake = input("\npress enter to continue")

    #print("\n\nThis quareter {event} happend causing {student} to have {effect}.".format(event = class_events(), student = s4.name, effect = 'Test effect'))
    
    event_manager(student_list)
    fake = input('\n\nQuarter is done! lets see how we did (hit enter)\n\n')
    grade_manager(student_list, course)

    #see if students pass and remove failed students
    for student in student_list:
        if student.grade < 65:
            print(student.name + " did not pass " + course.name)
            student_list.remove(student)
    #see if students are alive
    for student in student_list:
        if student.hp <= 0:
            print(student.name + " has died! RIP")
            student_list.remove(student)

    # level up remaining students
    for student in student_list:
        temp = int(student.age)
        student.age = temp + 1
        student.grade_level +=1

# make the courses
c = Course()
c2 = Course(10)
c3 = Course(11)
c4 = Course(12)

# make the students
player = Student()
s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
s5 = Student()
s6 = Student()
s7 = Student()
s8 = Student()
student_list = [s1, s2, s3, s4, s5, s6, s7, s8, player]

# MAIN

print('\n\nWelcome to High School!')
print('\nLets get you enrolled in the 9th grade!!')
player.create_player()


class_quarter(c, student_list)
class_quarter(c2, student_list)
class_quarter(c3, student_list)
class_quarter(c4, student_list)