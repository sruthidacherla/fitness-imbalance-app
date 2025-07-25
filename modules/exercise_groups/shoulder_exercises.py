import streamlit as sl

def rotator_exercises():
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

def deltoid_exercises():
    sl.header('Deltoids')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/deltoid.png', width = 250)
    ##About Rotator Cuff
    with text:
        sl.text_area('', "The deltoid is a large muscle made up of three parts: anterior, lateral, and posterior. \nIt is responsible for lifting and rotating the arm in multiple directions while helping stabilize the shoulder joint. The anterior deltoid helps lift the arm forward, the lateral deltoid raises the arm to the side, and the posterior deltoid moves the arm backward. \nBalanced strength across all three heads of the deltoid is essential for proper shoulder function, posture, and injury prevention. Weakness or imbalance in any part of the deltoid can lead to poor movement mechanics and shoulder injuries.")
    ##Exercises for Deltoids
    left, middle, right = sl.columns(3)
    if left.button("Front Raise", use_container_width=True):
        sl.markdown("**Front Raise**")
        sl.markdown("Muscles Targeted: *Anterior Deltoid*")
        sl.markdown("""
        1. Stand tall with a light dumbbell in each hand, arms at your sides.  
        2. Keep your palms facing the ground and elbows slightly bent.  
        3. Raise both arms straight in front of you to shoulder height.  
        4. Pause briefly, then lower slowly with control.  
        5. Avoid swinging or using momentum.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps, rest 30–60 seconds")

    if middle.button("Lateral Raise", use_container_width=True):
        sl.markdown("**Lateral Raise**")
        sl.markdown("Muscles Targeted: *Lateral Deltoid*")
        sl.markdown("""
        1. Stand tall with a light dumbbell in each hand, arms at your sides.  
        2. With a slight bend in your elbows, raise both arms out to the sides until shoulder height.  
        3. Keep wrists neutral and shoulders relaxed.  
        4. Lower back down slowly with control.  
        5. Don’t let the weights touch your body at the bottom.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps, rest 30–60 seconds")

    if right.button("Reverse Fly", use_container_width=True):
        sl.markdown("**Reverse Fly**")
        sl.markdown("Muscles Targeted: *Posterior Deltoid*")
        sl.markdown("""
        1. Bend slightly forward at the waist while keeping your back flat.  
        2. Hold a dumbbell in each hand with your palms facing each other.  
        3. With elbows slightly bent, raise your arms out to the sides like wings.  
        4. Squeeze your shoulder blades together at the top.  
        5. Lower with control and return to start.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps, rest 30–60 seconds")
