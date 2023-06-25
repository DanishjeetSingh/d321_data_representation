## Python script  D321  Assignment 4

## domain Person P

P = [{'p': 'Emma'},
 {'p': 'Eric'},
 {'p': 'Vidya'},
 {'p': 'Anna'},
 {'p': 'YinYue'},
 {'p': 'Latha'},
 {'p': 'Qin'},
 {'p': 'Ryan'},
 {'p': 'Deepa'},
 {'p': 'Hasan'},
 {'p': 'Linda'},
 {'p': 'Chris'},
 {'p': 'Lisa'},
 {'p': 'Nick'},
 {'p': 'Arif'},
 {'p': 'Megan'},
 {'p': 'Margaret'},
 {'p': 'Jean'},
 {'p': 'John'},
 {'p': 'Danielle'},
 {'p': 'Pedro'}]

## Domain course C


C = [{'c': 'AI'},
 {'c': 'DataScience'},
 {'c': 'Algorithms'},
 {'c': 'Complexity'},
 {'c': 'Networks'},
 {'c': 'Databases'},
 {'c': 'Logic'},
 {'c': 'Programming'},
 {'c': 'Physics'},
 {'c': 'D321'}]


## Domain major M

M = [ {'m': 'DataScience'},
 {'m': 'Math'},
 {'m': 'English'},
 {'m': 'Physics'},
 {'m': 'CS'},
 {'m': 'Chemistry'},
 {'m': 'Philosophy'}]


## Unary predicates

professor = [ {'p': 'Jean'},
 {'p': 'Arif'},
 {'p': 'Eric'},
 {'p': 'Pedro'},
 {'p': 'Emma'},
 {'p': 'Anna'}]


student = [ {'p': 'YinYue'},
 {'p': 'Lisa'},
 {'p': 'Margaret'},
 {'p': 'Hasan'},
 {'p': 'Deepa'},
 {'p': 'Megan'},
 {'p': 'Chris'},
 {'p': 'Linda'},
 {'p': 'Latha'},
 {'p': 'Nick'},
 {'p': 'Vidya'},
 {'p': 'Danielle'},
 {'p': 'Qin'},
 {'p': 'Ryan'},
 {'p': 'John'}]



## Binary predicates

enroll = [{'p': 'Nick','c':'Logic'},
 {'p': 'Hasan','c':'Logic'},
 {'p': 'Eric','c':'Complexity'},
 {'p': 'Vidya','c':'DataScience'},
 {'p': 'Jean','c':'Physics'},
 {'p': 'Deepa','c':'Complexity'},
 {'p': 'Megan','c':'AI'},
 {'p': 'Vidya','c':'AI'},
 {'p': 'Hasan','c':'Databases'},
 {'p': 'Deepa','c':'D321'},
 {'p': 'Deepa','c':'D321'},
 {'p': 'Anna','c':'Physics'},
 {'p': 'Danielle','c':'D321'},
 {'p': 'Emma','c':'Complexity'},
 {'p': 'Hasan','c':'Physics'},
 {'p': 'Nick','c':'Programming'},
 {'p': 'Jean','c':'AI'},
 {'p': 'Anna','c':'D321'},
 {'p': 'John','c':'Logic'},
 {'p': 'Jean','c':'Logic'},
 {'p': 'Lisa','c':'Physics'},
 {'p': 'Jean','c':'DataScience'},
 {'p': 'Hasan','c':'Networks'},
 {'p': 'Jean','c':'Complexity'},
 {'p': 'YinYue','c':'AI'},
 {'p': 'John','c':'AI'},
 {'p': 'Chris','c':'DataScience'},
 {'p': 'Margaret','c':'Logic'},
 {'p': 'Latha','c':'Physics'},
 {'p': 'Jean','c':'Networks'},
 {'p': 'Qin','c':'Complexity'},
 {'p': 'Latha','c':'Logic'},
 {'p': 'Deepa','c':'Physics'},
 {'p': 'Linda','c':'Networks'},
 {'p': 'Anna','c':'Databases'},
 {'p': 'Margaret','c':'AI'},
 {'p': 'Linda','c':'Logic'},
 {'p': 'Jean','c':'Programming'},
 {'p': 'Qin','c':'Networks'},
 {'p': 'Eric','c':'Logic'},
 {'p': 'Ryan','c':'DataScience'},
 {'p': 'Latha','c':'Networks'},
 {'p': 'Deepa','c':'Programming'},
 {'p': 'Nick','c':'DataScience'},
 {'p': 'Ryan','c':'D321'},
 {'p': 'Anna','c':'DataScience'},
 {'p': 'Latha','c':'D321'},
 {'p': 'Chris','c':'Programming'},
 {'p': 'Vidya','c':'Complexity'},
 {'p': 'Arif','c':'Programming'},
 {'p': 'Emma','c':'Programming'},
 {'p': 'Margaret','c':'Complexity'},
 {'p': 'Eric','c':'D321'},
 {'p': 'Margaret','c':'Algorithms'},
 {'p': 'Hasan','c':'Algorithms'},
 {'p': 'Hasan','c':'AI'}]



teaches = [{'p': 'Jean','c':'Databases'},
 {'p': 'Emma','c':'Networks'},
 {'p': 'Eric','c':'Databases'},
 {'p': 'Eric','c':'D321'},
 {'p': 'Emma','c':'Algorithms'},
 {'p': 'Pedro','c':'AI'},
 {'p': 'Emma','c':'Complexity'},
 {'p': 'Anna','c':'Complexity'},
 {'p': 'Jean','c':'Logic'},
 {'p': 'Arif','c':'Networks'},
 {'p': 'Emma','c':'Logic'},
 {'p': 'Anna','c':'AI'},
 {'p': 'Eric','c':'Logic'},
 {'p': 'Anna','c':'D321'},
 {'p': 'Eric','c':'AI'},
 {'p': 'Emma','c':'Physics'},
 {'p': 'Eric','c':'Networks'},
 {'p': 'Emma','c':'DataScience'},
 {'p': 'Jean','c':'D321'}]




hasmajor = [ {'p': 'Qin','m':'Chemistry'},
 {'p': 'Danielle','m':'Chemistry'},
 {'p': 'Megan','m':'Chemistry'},
 {'p': 'John','m':'Chemistry'},
 {'p': 'Lisa','m':'English'},
 {'p': 'YinYue','m':'Physics'},
 {'p': 'Margaret','m':'English'},
 {'p': 'Latha','m':'Math'},
 {'p': 'Deepa','m':'English'},
 {'p': 'Nick','m':'Chemistry'},
 {'p': 'Hasan','m':'English'},
 {'p': 'Megan','m':'DataScience'},
 {'p': 'John','m':'English'},
 {'p': 'Danielle','m':'Physics'},
 {'p': 'Latha','m':'Chemistry'},
 {'p': 'Danielle','m':'Math'},
 {'p': 'Hasan','m':'DataScience'},
 {'p': 'Margaret','m':'Physics'}]




knows = [{'p1': 'Jean','p2':'Megan'},
 {'p1': 'Nick','p2':'Megan'},
 {'p1': 'Margaret','p2':'Lisa'},
 {'p1': 'Danielle','p2':'YinYue'},
 {'p1': 'Eric','p2':'Megan'},
 {'p1': 'Nick','p2':'Margaret'},
 {'p1': 'Lisa','p2':'John'},
 {'p1': 'Qin','p2':'Chris'},
 {'p1': 'Vidya','p2':'Margaret'},
 {'p1': 'Ryan','p2':'Emma'},
 {'p1': 'Latha','p2':'Emma'},
 {'p1': 'Hasan','p2':'Vidya'},
 {'p1': 'Vidya','p2':'Anna'},
 {'p1': 'Anna','p2':'Deepa'},
 {'p1': 'Emma','p2':'Jean'},
 {'p1': 'Deepa','p2':'Qin'},
 {'p1': 'Megan','p2':'Deepa'},
 {'p1': 'Danielle','p2':'Hasan'},
 {'p1': 'Vidya','p2':'Latha'},
 {'p1': 'Lisa','p2':'YinYue'},
 {'p1': 'Anna','p2':'Linda'},
 {'p1': 'Emma','p2':'Linda'},
 {'p1': 'Hasan','p2':'Danielle'},
 {'p1': 'Chris','p2':'Eric'},
 {'p1': 'Ryan','p2':'Eric'},
 {'p1': 'Qin','p2':'Qin'},
 {'p1': 'YinYue','p2':'Emma'},
 {'p1': 'Ryan','p2':'Hasan'},
 {'p1': 'Megan','p2':'Eric'},
 {'p1': 'Deepa','p2':'Linda'},
 {'p1': 'Qin','p2':'YinYue'},
 {'p1': 'Vidya','p2':'YinYue'},
 {'p1': 'Eric','p2':'Qin'},
 {'p1': 'Lisa','p2':'Jean'},
 {'p1': 'Danielle','p2':'Nick'},
 {'p1': 'Eric','p2':'Ryan'},
 {'p1': 'Linda','p2':'John'},
 {'p1': 'Lisa','p2':'Margaret'},
 {'p1': 'Qin','p2':'Nick'},
 {'p1': 'Ryan','p2':'Linda'},
 {'p1': 'Chris','p2':'Lisa'},
 {'p1': 'Chris','p2':'Anna'},
 {'p1': 'Anna','p2':'Lisa'},
 {'p1': 'Arif','p2':'Arif'},
 {'p1': 'Nick','p2':'Qin'},
 {'p1': 'Arif','p2':'Latha'},
 {'p1': 'Margaret','p2':'Latha'},
 {'p1': 'Anna','p2':'Arif'},
 {'p1': 'Megan','p2':'Margaret'},
 {'p1': 'Deepa','p2':'Hasan'},
 {'p1': 'Arif','p2':'YinYue'}]



## Boolean functions for unary predicates Student(p) and Professor(p)

def Student(p): return p in student

def Professor(p): return p in professor


## Boolean functions for binary predicates Enroll(p,c), Teaches (p,c),
## hasMajor(p,m), and Knows(p_1,p_2)


def Enroll(p,c): return {'p':p['p'],'c':c['c']} in enroll

def Teaches(p,c): return {'p':p['p'],'c':c['c']} in teaches

def hasMajor(p,m): return {'p':p['p'],'m':m['m']} in hasmajor

def Knows(p1,p2): return {'p1':p1['p'],'p2':p2['p']} in knows

## Boolean function for Implies

def Implies (P, Q): return not P or Q

def print_Answer(L):  print("\n".join((str(x) for x in L)))  ## function to print elements of list one line at a time


print('Problem 5.b')
## Some student knows a professor who teaches the ‘Databases’
## course.

## Your Python code for this problem must go here
print(any([Student(i) and any([Professor(j) and Knows(i,j) and Teaches(j,{'c':'Databases'}) for j in P]) for i in P]))

print('Problem 6.b')
## Each course taught by professor ‘Anna’ is taken by at least two
## students.

## Your Python code for this problem must go here
for course in C:
    if Teaches({'p': 'Anna'}, course) and Professor('Anna'):
        student_count = sum(Enroll(student, course) and Student(student) for student in P)
        if student_count < 2:
            print(False)
            break
else:
    print(True)


print('Problem 6.e')

print(not any([Teaches({'p': 'Anna'},i) and Professor('Anna') and not any([Student(j) and Student(k) and j!=k and Enroll(j,i) and Enroll(k,i) for j,k in P]) for i in C]))

print('Problem 7.b')
## Find the majors of students who are enrolled in the course `Algorithms'

## Your Python code for this problem must go here
print_Answer([i for i in M if any([Student(j) and hasMajor(j,i) 
and Enroll(j, {'c': 'Algorithms'}) for j in P])])

print('Problem 8.b')
## Find each student who knows a student who takes a course taught by
## professor ‘Emma’ or a course taught by professor ‘Arif' or by Professor 'Anna'.

## Your Python code for this problem must go here
print_Answer([i for i in student if any([Knows(i,j) and any([Enroll(j,k) and (Teaches({'p': 'Emma'}, k) or Teaches({'p': 'Arif'}, k) or Teaches({'p': 'Anna'}, k)) for k in C]) for j in student])])


print('Problem 9.b')
## Find each pair of different students who both know a same professor
## who teaches the course ‘Databases’

## Your Python code for this problem must go here
print_Answer([(i,j) for i in P for j in P if Student(i) and Student(i) and i != j and any([Teaches(k,{'c':'Databases'}) and Knows(j,k) for k in P])])

print('Problem 10.b')
## Find each professor who only teaches courses taken by all students
## who major in `DataScience'

## Your Python code for this problem must go here
print_Answer([i for i in professor if all([Implies(Teaches(i,j), all([Implies(hasMajor(k, {'m':'DataScience'}), Enroll(k,j)) for k in student])) for j in C])])

print('Problem 11.b')
## Find each professor who does not know any student who majors in
## both ‘DataScience’ and in ‘Physics

## Your Python code for this problem must go here
print_Answer([i for i in professor if not any([hasMajor(j,{'m': 'DataScience'}) and hasMajor(j,{'m':'Physics'}) and Knows(i,j) for j in student])])

print('Problem 12.b')

## Find each pair of different students who have a common major and who
## take none of the courses taught by professor `Pedro'

## Your Python code for this problem must go here
print_Answer([(i,j) for i in P for j in P if Student(i) and Student(j) and i != j and any([hasMajor(i,k) and hasMajor(j,k) and not any([Teaches({'p':'Pedro'},l) and (Enroll(i,l) or Enroll(j,l)) for l in C]) for k in M])])

