# -*- coding: utf-8 -*-

# Created on Mon Nov  7 15:41:11 2016
# For use in Scientific Python course
# Topic: objects
# @author: Alexander Pitchford
# @organisation: IMPACS, Aberystwyth University

"""
Practical example of class objects:
People and statistics about them
"""

import numpy as np
import random

class Person(object):
    """A generic person with some personal attributes"""
    age_distrib_func = random.uniform
    age_distrib_args = (1, 120)
    height_distrib_func = random.gauss
    height_distrib_args = (1.7, 0.2)
    
    def __init__(self, name, sex, age, height):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
                
    def __str__(self):
        return "{} of name: {}, sex: {}, age: {}, height {:0.2f}m".format(
                                                self.__class__.__name__, 
                                                self.name, self.sex, 
                                                self.age, self.height)
                                
                                
class PersonalStatistics(object):
    """Some statistics about lists of people"""
    def __init__(self, people=[]):
        self.people = people
    
    @property
    def num_people(self):
        """Number of people in the list"""
        return len(self.people)
        
    def sex_split(self):
        """
        Calculate the percentage of different sexes in the people list
        Result returned in dictionary with the sex as the key and the
        proportion as the value.
        """
        n = self.num_people
        if n == 0:
            return None
            
        ss = {}
        for p in self.people:
            if ss.get(p.sex, None):
                ss[p.sex] += 1.0
            else:
                ss[p.sex] = 1.0
        
        for k in ss:
            ss[k] = ss[k]/n
            
        return ss
        
    def mean_age(self):
        """Calculate the mean average age of the people in the list"""
        return np.mean([p.age for p in self.people])
        
    def std_age(self):
        """Calculate the standard deviation of age of the people in the list"""
        return np.std([p.age for p in self.people])
        
    def mean_height(self):
        """Calculate the mean average height 
        of the people in the list"""
        return np.mean([p.height for p in self.people])
        
    def std_height(self):
        """Calculate the standard deviation of 
        height of the people in the list"""
        return np.std([p.height for p in self.people])
        
    def median_age(self):
        """Calculate the median average age of the people in the list"""
        return np.median([p.age for p in self.people])
        
    def mode_age(self):
        """
        Calculate the mode average age and frequency  
        of the people in the list
        """
        counts = np.bincount([p.age for p in self.people])
        return np.argmax(counts), np.max(counts)
        
    def report(self):
        """Print out the statistics for the people in the list"""
        
        n = self.num_people
        if n == 0:
            print("No people to report on")
            return
        
        print("\nReporting on {} people".format(n))
        ss = self.sex_split()
        sss = "The split of the sexes is: "
        for k in sorted(ss, key=ss.__getitem__, reverse=True):
            sss += "{}: {:0.1f}%, ".format(k, ss[k]*100)
        # note treating string as character list and not printing last 
        # 2 characters (as they are a comma and a space)
        print(sss[:-2])
        print("Mean average age: {:0.2f}".format(self.mean_age()))
        print("Median average age: {}".format(self.median_age()))
        mode, freq = self.mode_age()
        print("Mode average age: {} (freq {})".format(mode, freq))
        print("Std dev age: {:0.2f}".format(self.std_age()))
        print("Mean average height: {:0.2f}".format(self.mean_height()))
        print("Std dev height: {:0.2f}".format(self.std_height()))
        

class PeopleFactory(object):
    """Generates lists of Person objects"""
    sexes = ['male', 'female', 'other']
    sex_prob = [0.49, 0.49, 0.02]
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.male_firstname_fname = 'male_first_names.txt'
        self.female_firstname_fname = 'female_first_names.txt'
        self.surname_fname = 'surnames.txt'
        self.male_firstnames = None
        self.female_firstnames = None
        self.surnames = None
        self.names_loaded = False
    
    def load_names(self):
        self.male_names = np.genfromtxt(self.male_firstname_fname, 
                                   dtype=str).tolist()
        self.female_names = np.genfromtxt(self.female_firstname_fname,
                                     dtype=str).tolist()
        self.surnames = np.genfromtxt(self.surname_fname, dtype=str).tolist()
        self.names_loaded = True
        
    def choose_sex(self):
        """choose a sex based on the probabilites"""
        x = random.random()
        cumul_prob = 0.0
        for s, p in zip(self.sexes, self.sex_prob):
            cumul_prob += p
            if x < cumul_prob:
                return s
        raise ValueError("Unable to choose sex, "
                        "check probabilities sum to 1.0")
                        
    def choose_name(self, sex):
        """return a name based on the sex"""
        if not self.names_loaded:
            self.load_names()
            
        if sex == 'male':
            first_name = random.choice(self.male_names)
        elif sex == 'female':
            first_name = random.choice(self.female_names)
        else:
            first_name = random.choice(self.male_names + self.female_names)
            
        return first_name + ' ' + random.choice(self.surnames)
        
    def generate_person(self, cls=Person):
        """Generate a Person with random attributes"""
        # choose a sex
        sex = self.choose_sex()
        # choose a name
        name = self.choose_name(sex)
        # sample age
        age = int(cls.age_distrib_func(*cls.age_distrib_args))
        # sample height
        height = cls.height_distrib_func(*cls.height_distrib_args)
        
        return Person(name, sex, age, height)
                    
    def generate_random_people(self, n, cls=Person):
        """Generate a list of n people with random attributes"""
        return [self.generate_person(cls) for i in range(n)]
