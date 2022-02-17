'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
#import sys

SCHEDULE = Schedule()
SCHEDULE.load_courses()
SCHEDULE = SCHEDULE.enrolled(range(5, 1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
status (filter by status, e.g. Open)
'''

# Jason
def coursenum_filter(num):
    '''filters by course number'''
    return ([c for c in SCHEDULE.courses if c['coursenum'] == num])

# Jason
def instructor(instr):
    '''filters by instructor'''
    return ([c for c in SCHEDULE.courses if instr in c['instructor']])

# Jason
def subject(subj):
    '''filters by subject'''
    return ([c for c in SCHEDULE.courses if c['subject'] == subj])

# Tiancheng
def title(title):
    '''filters by title'''
    return ([c for c in SCHEDULE.courses if title in c['name']])

# Tiancheng
def description(desc):
    '''filters by description'''
    return ([c for c in SCHEDULE.courses if desc in c['desc']])

# Tiancheng
def tiancheng_filter(phrase, subj):
    '''filters all courses above a certain enrollment level in certain subject'''
    return ([c for c in subject(subj) if c['enrolled'] > phrase])
# Jason
def jason_filter(subjct):
    '''filters only remote courses in a certain subject'''
    return ([c for c in subject(subjct) if 'remote' in c['details']])

#Iria
def iria_filter(day, subj):
    '''filters all courses of a certain subject that does not meet on a specified day'''
    return Schedule([c for c in subject(subj) \
             if (len(c['times']) == 1 and day not in c['times'][0]['days'] or \
             (len(c['times']) == 2 and day not in c['times'][0]['days'] and \
             day not in c['times'][1]['days']))])


terms = {c['term'] for c in SCHEDULE.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global SCHEDULE
    while True:
        command = input(">> (h for help) ")
        if command == 'quit':
            return
        if command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-' * 40 + '\n\n')
            continue
        if command in ['r', 'reset']:
            SCHEDULE.load_courses()
            SCHEDULE = SCHEDULE.enrolled(range(5, 1000))
            continue
        if command in ['t', 'term']:
            term = input("enter a term:" + str(terms) + ":")
            SCHEDULE = SCHEDULE.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
            SCHEDULE = SCHEDULE.subject([subject])
        elif command in ['title']:
            subject = input("enter a title phrase:")
            SCHEDULE = SCHEDULE.title(subject)
        elif command in ['description']:
            subject = input("enter a description phrase:")
            SCHEDULE = SCHEDULE.description(subject)
        elif command in ['status']:
            subject = input("enter a status:")
            SCHEDULE = SCHEDULE.status(subject)
        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(SCHEDULE.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in SCHEDULE.courses[:10]:
            print_course(course)
        print('\n' * 3)

def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])

if __name__ == '__main__':
    course = jason_filter('COSI')
    print(course)
    # topmenu()


# comment for video
####### Random comment for video