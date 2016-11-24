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
                                
    def __repr__(self):
        return self.__str__()
        
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
        
        ss.update((key, p/n) 
                            for key, p in ss.items())
                            
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
    def __init__(self):
        # options for sex, with proportions
        self.sexes = {'male':49, 'female':49, 'other':2}
        # options for age group, with proportions
        self.age_groups = {'young':30, 'older':70}
        # distribution parameters for the age groups
        self.young_age_lbound = 0
        self.young_age_ubound = 42
        self.older_age_mean = 60
        self.older_age_std = 20
        self.min_age = 0
        self.max_age = 130
        # distribution parameters for the height
        self.height_mean = 1.7
        self.height_std = 0.2
        # files for the random names
        self.male_firstname_fname = 'male_first_names.txt'
        self.female_firstname_fname = 'female_first_names.txt'
        self.surname_fname = 'surnames.txt'
        self.male_firstnames = None
        self.female_firstnames = None
        self.surnames = None
        self.names_loaded = False
        self.normalize_grp_probs()
    
    def load_names(self):
        self.male_names = np.genfromtxt(self.male_firstname_fname, 
                                   dtype=str).tolist()
        self.female_names = np.genfromtxt(self.female_firstname_fname,
                                     dtype=str).tolist()
        self.surnames = np.genfromtxt(self.surname_fname, dtype=str).tolist()
        self.names_loaded = True
    
    def normalize_grp_probs(self):
        """Normalise all the group probability attributes"""
        self.normalize_probs(self.sexes)
        self.normalize_probs(self.age_groups)
        
    def normalize_probs(self, prob_dict):
        """
        normalise the probabilties in the dictionary
        scale so that they sum to 1.0
        """
        total_prob = sum(prob_dict.values())
        if total_prob != 1:
            prob_dict.update((key, p/total_prob) 
                            for key, p in prob_dict.items())
        
    def select_rnd_key(self, prob_dict):
        """
        select a key from the dictionary based on the probabilties,
        which are the dictionary values.        
        """
        x = random.random()
        cumul_prob = 0.0
        for key in prob_dict:
            p = prob_dict[key]
            cumul_prob += p
            if x < cumul_prob:
                return key
        raise ValueError("Unable to choose item, "
                        "check probabilities have been normalised")
        
    def choose_age(self):
        """
        Custom distribution for ages
        Choose an age group, then use the distribution for this group
        with the corresponding args
        """
        agegrp = self.select_rnd_key(self.age_groups)
        if agegrp == 'young':
            age = random.uniform(self.young_age_lbound, self.young_age_ubound)
        elif agegrp == 'older':
            age = random.gauss(self.older_age_mean, self.older_age_std)
        else:
            raise KeyError("No option for agegrp '{}'".format(agegrp))
            
        return min(self.max_age, max(self.min_age, int(age)))
            
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
        sex = self.select_rnd_key(self.sexes)
        # choose a name
        name = self.choose_name(sex)
        # sample age
        age = self.choose_age()
        # sample height
        height = random.gauss(self.height_mean, self.height_std)

        return cls(name, sex, age, height)
                    
    def generate_random_people(self, n, cls=Person):
        """Generate a list of n people with random attributes"""
        # check group dicts are normalised
        self.normalize_grp_probs()
        return [self.generate_person(cls) for i in range(n)]
        
