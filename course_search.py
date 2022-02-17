'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
#import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5, 1000)) # eliminate courses with no students

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

def coursenum_filter(num):
    '''filters by course number'''
    return ([c for c in schedule.courses if c['coursenum'] == num])

def instructor(instr):
    '''filters by instructor'''
    return ([c for c in schedule.courses if instr in c['instructor']])

def subject(subj):
    '''filters by subject'''
    return ([c for c in schedule.courses if c['subject'] == subj])

def title(title):
    '''filters by title'''
    return ([c for c in schedule.courses if title in c['name']])

def description(desc):
    '''filters by description'''
    return ([c for c in schedule.courses if desc in c['desc']])

def tiancheng_filter(phrase, subj):
    '''filters all courses above a certain level in a certain subject'''
    return ([c for c in subject(subj) if c['enrolled'] > phrase])

def jason_filter(subjct):
    '''filters only remote courses in a certain subject'''
    return ([c for c in subject(subjct) if 'remote' in c['details']])

def iria_filter(day, subj):
    '''filters all courses of a certain subject that does not meet on a specified day'''
    return ([c for c in subject(subj) if c['time'] != [] and day not in c['time'][0]['days']])


terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command == 'quit':
            return
        if command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-' * 40 + '\n\n')
            continue
        if command in ['r', 'reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5, 1000))
            continue
        if command in ['t', 'term']:
            term = input("enter a term:" + str(terms) + ":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['title']:
            subject = input("enter a title phrase:")
            schedule = schedule.title(subject)
        elif command in ['description']:
            subject = input("enter a description phrase:")
            schedule = schedule.description(subject)
        elif command in ['status']:
            subject = input("enter a status:")
            schedule = schedule.status(subject)
        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(schedule.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n' * 3)

def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])

if __name__ == '__main__':
#    course = tiancheng_filter(100, 'COSI')
#    print(course)
    topmenu()
