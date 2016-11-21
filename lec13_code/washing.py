# -*- coding: utf-8 -*-

# Created on Mon Nov  7 13:14:41 2016
# For use in Scientific Python course
# Topic: objects
# @author: Alexander Pitchford
# @organisation: IMPACS, Aberystwyth University

"""
Toy example as introduction to classes and objects
You can't wash your clothes with a computer program!
"""

import time

class WashingMachine(object):
    """Machine for washing clothes (intended purpose anyway)"""
    
    dirty_words = ['dirty', 'filthy', 'grubby', 'soiled']
    wet_words = ['wet', 'damp', 'soggy', 'drenched']
    
    def __init__(self, model_name=None):
        """Initialise WashingMachine, optionally with model_name"""
        # This is called when a new object of this type is created.
        self.reset()
        if model_name is None:
            self.model = 'generic washing machine'
        else:
            self.model = model_name
        self.contents = 'empty'
        self.detergent_avail = False
        self.fill_time = 1.0
        self.wash_time = 2.0
        self.spin_time = 1.0
        
    def load(self, contents):
        """Load the machine with the contents"""
        self.contents = str(contents)
        
    def add_detergent(self):
        """Add some detergent to the machine"""
        self.detergent_avail = True
        
    def wash(self):
        """Run the wash cycle of the machine"""
        self.contents = self.contents.lower()
        print("Water filling...")
        time.sleep(self.fill_time)
        if not "wet" in self.contents:
            self.contents = "wet " + self.contents
        if not "soaking" in self.contents:
            self.contents = "soaking " + self.contents
        print("Washing...")
        time.sleep(self.wash_time)
        if self.detergent_avail:
            for dw in self.dirty_words:
                if dw in self.contents:
                    self.contents = self.contents.replace(dw, 'clean')
        self.detergent_avail = False
        print("Spinning...")
        time.sleep(self.spin_time)
        self.contents = self.contents.replace('soaking', '').strip()
        print("Wash cycle finished")
        
    def empty(self):
        """Remove the contents"""
        self.contents = 'empty'
        
    def dry(self):
        # Not implemented in this class, only here to give an Exception
        raise NotImplementedError(
                "{} cannot dry, try another machine".format(self.model))
        
class ZanussiZWF91483W(WashingMachine):
    """A 9kg load washing machine from Zanussi"""
    def reset(self):
        WashingMachine.reset(self)
        self.model = 'ZWF91483W'
        self.fill_time = 0.5
        self.wash_time = 1.25
        self.spin_time = 0.45
    