# -*- coding: utf-8 -*-
# Created on Mon Nov  7 13:40:40 2016
# For use in Scientific Python course
# Topic: objects
# @author: Alexander Pitchford
# @organisation: IMPACS, Aberystwyth University

"""
Script for playing around with the washing objects
"""

from washing import WashingMachine, WasherDryer, ZanussiZWF91483W

# make a washing machine
print("Testing the washing machine")
mach1 = WashingMachine()

# load some dirty clothes
mach1.load("dirty clothes")
print("machine contains: {}".format(mach1.contents))

# start the wash cycle
mach1.wash()

# Check the contents
print("machine contains: {}".format(mach1.contents))

# Remember to add the detergent this time!
mach1.add_detergent()
mach1.wash()
# Check the contents
print("machine contains: {}".format(mach1.contents))

# Try washing something else
mach1.load("grubby elephant")
mach1.add_detergent()
mach1.wash()
# Check the contents
print("machine contains: {}".format(mach1.contents))

print("\nTesting the washer dryer")
# Make a washer dryer
wd1 = WasherDryer()
# load some dirty clothes
wd1.load("dirty clothes")
print("machine contains: {}".format(wd1.contents))
wd1.add_detergent()
wd1.wash()
wd1.dry()
# Check the contents
print("machine contains: {}".format(wd1.contents))

print("\nTesting the wash and dry cycle")
# load some dirty clothes
wd1.load("dirty clothes")
print("machine contains: {}".format(wd1.contents))
wd1.add_detergent()
wd1.wash_and_dry()
# Check the contents
print("machine contains: {}".format(wd1.contents))

zan1 = ZanussiZWF91483W()
print("\nNow testing a specific model '{}'".format(zan1.model))
zan1.load("dirty clothes")
print("machine contains: {}".format(zan1.contents))
zan1.add_detergent()
zan1.wash()
zan1.dry()
# Check the contents
print("machine contains: {}".format(zan1.contents))


