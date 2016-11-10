# -*- coding: utf-8 -*-
# Created on Wed Nov  9 17:02:20 2016
# For use in Scientific Python course
# Topic: objects
# @author: Alexander Pitchford
# @organisation: IMPACS, Aberystwyth University

"""
Script for trying out with the people objects
"""

from people import (Person, generate_random_people, 
                    PersonalStatistics)

alex = Person('Alex Pitchford', 'male', 42, 1.75)
fred = Person('Fred Blogs', 'male', 55, 1.9)
bilbo = Person('Bilbo Baggins', 'male', 131, 0.9)
meandmyfriends = [alex, fred, bilbo]
for p in meandmyfriends:
    print(p)
    
mmf_stats = PersonalStatistics(meandmyfriends)
mmf_stats.report()


# make some more people
peeps10 = generate_random_people(10)
stats10 = PersonalStatistics(peeps10)
stats10.report()

peeps100 = generate_random_people(100)
stats100 = PersonalStatistics(peeps100)
stats100.report()

peeps10000 = generate_random_people(10000)
stats10000 = PersonalStatistics(peeps10000)
stats10000.report()

# Add standard deviation for age
# Add mean and standard deviation for height
# Add shoe size for Person

# Use property setters for value checking

