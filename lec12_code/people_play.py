# -*- coding: utf-8 -*-
# Created on Wed Nov  9 17:02:20 2016
# For use in Scientific Python course
# Topic: objects
# @author: Alexander Pitchford
# @organisation: IMPACS, Aberystwyth University

"""
Script for trying out with the people objects
"""

from people import Person, generate_random_people, PersonalStatistics

# make a person

alex = Person('Alex Pitchford', 'male', 42, 1.75)
print(alex)

# make some people
peeps = generate_random_people(100)


stats = PersonalStatistics(peeps)
stats.report()

# Add standard deviation for age
# Add mean and standard deviation
# Add shoe size for Person

# Use property setters for value checking

