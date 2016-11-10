# -*- coding: utf-8 -*-
# Created on Wed Nov  9 17:02:20 2016
# For use in Scientific Python course
# Topic: objects
# @author: Alexander Pitchford
# @organisation: IMPACS, Aberystwyth University

"""
Script for trying out with the people objects
"""

from people import (Person, PeopleFactory, 
                    PersonalStatistics)

alex = Person('Alexander Pitchford', 'male', 42, 1.75)
kath = Person('Katherine Jenkins', 'female', 36, 1.6)
sid = Person('Sidharth Kashap', 'male', 29, 1.9)
meandmyfriends = [alex, kath, sid]
for p in meandmyfriends:
    print(p)
    
mmf_stats = PersonalStatistics(meandmyfriends)
mmf_stats.report()


# make some more people
pf = PeopleFactory()
peeps10 = pf.generate_random_people(10)
stats10 = PersonalStatistics(peeps10)
stats10.report()

peeps100 = pf.generate_random_people(100)
stats100 = PersonalStatistics(peeps100)
stats100.report()

peeps10000 = pf.generate_random_people(10000)
stats10000 = PersonalStatistics(peeps10000)
stats10000.report()



