import streamlit as sl
from modules.exercise_groups.shoulder_exercises import rotator_exercises, deltoid_exercises
from modules.exercise_groups.arm_exercises import tricep_exercises, bicep_exercises

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
    
'''
def run_back(): 
    sl.title('Arm Exercises')
    #Triceps
    sl.header('Triceps')
    ##About Rotator Cuff
    sl.text_area('Tricep....')
    ##Muscle Imbalance in Rotator Cuff
    ##Exercises for Rotator Cuff

    #Lower Back

    #Upper Back

def run_chest():
    sl.title('Arm Exercises')
    #Triceps
    sl.header('Triceps')
    ##About Rotator Cuff
    sl.text_area('Tricep....')
    ##Muscle Imbalance in Rotator Cuff
    ##Exercises for Rotator Cuff
    #Pecs

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