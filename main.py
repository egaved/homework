'''домашняя работа'''

import pandas as pd
import matplotlib.pyplot as plt

def conversion(string):
    '''меняет формат числа: 1k -> 1000'''
    if string[-1] == 'k':
        return float(string.rstrip('k')) * 1000
    if string[-1] == 'm':
        return float(string.rstrip('m')) * 1000000
    return float(string)

courses = pd.read_csv('coursera_data.csv', delimiter=',', index_col='id')
courses['course_students_enrolled'] = courses['course_students_enrolled'].apply(conversion)
top_by_students = courses.sort_values(by='course_students_enrolled', ascending=False).head(10)
plt.hist(top_by_students['course_students_enrolled'], bins=10)
plt.savefig('students_enrolled.png')
plt.clf()
plt.bar(top_by_students['course_title'],top_by_students['course_students_enrolled'])
plt.show()
top_by_rating = courses.sort_values(by='course_rating', ascending=False).head(10)
plt.hist(top_by_students['course_rating'], bins=10)
plt.savefig('students_rating.png')
plt.clf()
plt.bar(top_by_rating['course_title'],top_by_rating['course_rating'])
plt.show()
