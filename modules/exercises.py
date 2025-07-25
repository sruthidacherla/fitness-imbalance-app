import streamlit as sl
from modules.exercise_groups.shoulder_exercises import rotator_exercises, deltoid_exercises

##Shoulder
def run_shoulder(): 
    sl.title('Shoulder Exercises')

    #Rotator Cuff
    rotator_exercises()

    #Deltoids
    deltoid_exercises()

'''
def run_arms():
    sl.title('Arm Exercises')

    #Triceps
    sl.header('Triceps')
    ##About Triceps
    sl.text_area('', 'Takl about Triceps')
    ##Exercises for Triceps
    left, middle, right = sl.columns(3)
    if left.button("Single Arm Dumbell Press", use_container_width=True):
        sl.text('Display Exercise')
    if middle.button("Lateral Raises", use_container_width=True):
        sl.text('Display Exercise')
    if right.button("Front Raises", use_container_width=True):
        sl.text('Display Exercise')

    #Biceps

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