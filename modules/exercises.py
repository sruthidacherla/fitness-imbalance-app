import streamlit as sl
from modules.exercise_groups.shoulder_exercises import rotator_exercises, deltoid_exercises
from modules.exercise_groups.arm_exercises import tricep_exercises, bicep_exercises
from modules.exercise_groups.back_exercises import lowerback_exercises, upperback_exercises
from modules.exercise_groups.chest_exercises import pecs_exercises
##Shoulder
def run_shoulder(): 
    sl.title('Shoulder Exercises')

    #Rotator Cuff
    rotator_exercises()

    #Deltoids
    deltoid_exercises()

def run_arms():
    sl.title('Arm Exercises')

    #Triceps
    tricep_exercises()
    
    #Biceps
    bicep_exercises()
    
def run_back(): 
    sl.title('Arm Exercises')

    #Lower Back
    lowerback_exercises()

    #Upper Back
    upperback_exercises()

def run_chest():
    sl.title('Chest Exercises')
    #Pecs
    pecs_exercises()

'''
def run_hips():
    sl.title('Arm Exercises')
    #Triceps
    sl.header('Triceps')
    ##About Rotator Cuff
    sl.text_area('Tricep....')
    ##Muscle Imbalance in Rotator Cuff
    ##Exercises for Rotator Cuff
    #Glutes

    #Hip Flexors

def run_legs():
    sl.title('Arm Exercises')
    #Triceps
    sl.header('Triceps')
    ##About Rotator Cuff
    sl.text_area('Tricep....')
    ##Muscle Imbalance in Rotator Cuff
    ##Exercises for Rotator Cuff
    #Quads

    #Hamstrings

    #Calves

 '''