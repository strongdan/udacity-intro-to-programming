# CSVs with headers will be a list of dictionaries

#unicodecsv module

import unicodecsv

def read_csv(filename):
with open(filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

    enrollments = read_csv('enrollments.csv')
    daily_engagement = read_csv('daily_engagement.csv')
    project_submissions = read_csv('project_submissions.csv')
