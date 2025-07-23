import streamlit as sl

##Shoulder
def run_shoulder(): 
    sl.title('Shoulder Exercises')

    #Rotator Cuff
    sl.header('Rotator Cuff')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/rotator.png', width = 250)
    ##About Rotator Cuff
    with text:
        sl.text_area('', f'The rotator cuff is a group of four muscles: supraspinatus, infraspinatus, teres minor, and subscapularis. \nThey stabilize and move your shoulder joint while working together to keep the head of the upper arm bone firmly within the shallow socket of the shoulder. The rotator cuff plays a key role in lifting, rotating, and controlling the arm during both daily tasks and athletic movements. \nWeakness or imbalance in this muscle can lead to pain, reduced mobility, or shoulder injuries.')
    ##Exercises for Rotator Cuff
    left, middle, right = sl.columns(3)
    if left.button("External Rotation", use_container_width=True):
        sl.markdown("**Resistance Band External Rotation**")
        sl.markdown("Muscles Targeted: *Infraspinatus, Teres Minor*")
        sl.markdown("""
        1. Attach a resistance band to a stable surface at waist height.  
        2. Stand sideways to the anchor point, holding the band with the hand farthest from it.  
        3. Keep your elbow bent at 90° and tucked against your side.  
        4. Slowly rotate your forearm outward, away from your body, then return to the starting position.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps each arm, rest 30–60 seconds")
    if middle.button("Internal Rotation", use_container_width=True):
        sl.markdown("**Resistance Band Internal Rotation**")
        sl.markdown("Muscles Targeted: *Subscapularis*")
        sl.markdown("""
        1. Attach a resistance band to a stable surface at waist height.  
        2. Stand sideways to the anchor point, holding the band with the hand closest to it.  
        3. Keep your elbow bent at 90° and tucked against your side.  
        4. Slowly pull your forearm inward, toward your belly, then return to the starting position.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps each arm, rest 30–60 seconds")
    if right.button("Empty Can", use_container_width=True):
        sl.markdown("**Empty Can Test**")
        sl.markdown("Muscles Targeted: *Supraspinatus*")
        sl.markdown("""
        1. Stand tall with your arms by your sides.  
        2. Raise your arms diagonally in front of you, like forming a 'Y'.  
        3. Rotate your thumbs downward, as if pouring out a can.  
        4. Slowly lift your arms to shoulder height.  
        5. Lower them back down with control.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–12 reps, rest 30–60 seconds")


    #Deltoids
    sl.header('Deltoids')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/deltoid.png', width = 250)
    ##About Rotator Cuff
    with text:
        sl.text_area('', 'Talk about the Deltoid')
    ##Exercises for Deltoids
    left, middle, right = sl.columns(3)
    if left.button("Single Arm Dumbell Press", use_container_width=True):
        sl.text('Display Exercise')
    if middle.button("Lateral Raises", use_container_width=True):
        sl.text('Display Exercise')
    if right.button("Front Raises", use_container_width=True):
        sl.text('Display Exercise')

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