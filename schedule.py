'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    # constructor
    def __init__(self, courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    # loads courses
    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json", "r", encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    # filter by lastname
    def lastname(self, names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    # filter by email
    def email(self, emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    # filter by term
    def term(self, terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    # filter by enrolled
    def enrolled(self, vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    # filter by subject
    def subject(self, subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    # filter by sort
    def sort(self, field):
        '''sorts'''
        if field == 'subject':
            return Schedule(sorted(self.courses, key = lambda course: course['subject']))
        else:
            print("can't sort by " + str(field) + " yet")
            return self

    # filters by title
    def title(self, phrase):
        '''filters by title'''
        return Schedule([course for course in self.courses if phrase in course['name']])

    # filters by description
    def description(self, phrase):
        '''filters by description'''
        return Schedule([course for course in self.courses if phrase in course['description']])

    # filters by status
    def status(self, status):
        '''filters by status'''
        return Schedule([course for course in self.courses if course['status_text'] == status])

