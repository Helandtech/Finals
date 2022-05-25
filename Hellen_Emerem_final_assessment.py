#Hellen

from random import randint

"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""


class CFGStudent:
    number =[]
    new_id_number =[]
    def __init__(self, name, surname, age, email, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id

    @staticmethod
    def generate_id(number):
        for i in range(1):
            x = randint(0, 10000)
            number.append(x)
            return number

    def get_id(self, number):
        print(number)



    def get_fullname(self):
        "Expected outcome should be 'Name Surname' "
        'your code goes here'
        fullname = self.name + ' ' + self.surname
        return fullname


class NanoStudent(CFGStudent):

    def __init__(self, specialization,course_grades  ):
        #'your code goes here'
        self.specialization = specialization
        self.course_grades = course_grades

    @staticmethod
    def generate_id():
        'your code goes here'
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "

        for y in range(1):
            y = randint(0, 10000)
            new_id = 'NANO'+ str(y)
            new_id_number.append(y)
            return new_id

    def add_new_grade(self, grades):
        'your code goes here'
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"
        grades =  { Math: 6,
                    History : 7,
                    English: 8}
        add_subjects = input("Enter grades:")
        add_subjects_grades = int(input("Enter value:"))
        grades.update({add_subjects : add_subjects_grades})
        return grades

    def get_course_grades(self,grades):
        'your code goes here'
        'fetch course grades container and its values'
        subjects = input("Enter subject:")
        x = grades(subjects)
        print(x)



############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com', number)  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""
number = int(input("Enter limit value"))
def findfibonaccilist(number):
    firstnumbers = [0,1]

    for i in range(2,number+1):
        next_number = firstnumbers [-1] + firstnumbers [-2]

        firstnumbers.append(next_number)
    return firstnumbers

firstnumbers  = findfibonaccilist(number)
print(firstnumbers)

for i in firstnumbers:
    even_fibonacci_sum =


##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0








"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""



#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""
# Name variable with a semantic meaning of it function, as well short and similar between each other to avoid confusion
#less repetition of function and function names as well as variable
#use more inheritance to avoid repeating same function






