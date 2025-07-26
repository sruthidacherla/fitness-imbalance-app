import streamlit as sl

def tricep_exercises():
    sl.header('Tricep')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/tricep.png', width = 250)
    with text:
        sl.text_area('', "The triceps brachii, commonly known as the triceps, is a large muscle on the back of the upper arm made up of three heads: the long head, lateral head, and medial head. These heads work together to extend the elbow joint, allowing you to straighten your arm. The long head also assists with shoulder stability and extension. The triceps play a key role in pushing movements such as pressing, throwing, and performing push-ups. Weakness or imbalance in this muscle can lead to reduced arm strength, joint instability, or overcompensation by other muscles during upper body movements.")
    left, middle, right = sl.columns(3)
    if left.button("Overhead Extension", use_container_width=True):
        sl.markdown("**Overhead Triceps Extension**")
        sl.markdown("Muscles Targeted: *Triceps Brachii (Long Head)*")
        sl.markdown("""
        1. Start by holding a dumbbell/resistance band in one hand, with your elbow bent and your hand resting behind your head.
        2. Your elbow should point straight up toward the ceiling, close to your ear.
        3. From this position, fully extend your arm overhead until your arm is straight.
        4. Slowly lower back down to the starting position behind your head with control.
        5. Repeat on the other arm.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps each arm, rest 30–60 seconds")

    if middle.button("Triceps Kickback", use_container_width=True):
        sl.markdown("**Triceps Kickback**")
        sl.markdown("Muscles Targeted: *Triceps Brachii (Lateral and Medial Heads)*")
        sl.markdown("""
        1. Hold a dumbbell/resistance band in one hand and hinge forward at the hips.  
        2. Bend your elbow to 90° with your upper arm parallel to the floor.  
        3. Extend your arm straight back by straightening your elbow.  
        4. Pause at the top, then return to the starting position with control.  
        5. Repeat on each side.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps each arm, rest 30–60 seconds")

    if right.button("Close-Grip Push-Up", use_container_width=True):
        sl.markdown("**Close-Grip Push-Up**")
        sl.markdown("Muscles Targeted: *Triceps Brachii (All Heads)*")
        sl.markdown("""
        1. Get into a high plank position with your hands directly under your shoulders.  
        2. Keep your elbows tucked close to your sides as you lower your chest.  
        3. Push back up by fully extending your arms.  
        4. Maintain a straight line from head to heels throughout the movement.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 8–12 reps, rest 45–60 seconds")


def bicep_exercises():
    sl.header('Bicep')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/bicep.png', width = 250)
    with text:
        sl.text_area('', "The biceps brachii, commonly known as the biceps, is a two-headed muscle located on the front of the upper arm. It consists of the long head and the short head, which work together to flex the elbow, supinate the forearm (rotate the palm upward), and assist in lifting and pulling movements. The biceps are heavily engaged in everyday actions like lifting objects, pulling doors, or carrying bags. Weakness or imbalance in this muscle can lead to reduced arm function, elbow instability, and increased strain on the shoulder or forearm muscles.")
    ## Exercises for Biceps
    left, middle, right = sl.columns(3)
    if left.button("Concentration Curl", use_container_width=True):
        sl.markdown("**Concentration Curl**")
        sl.markdown("Muscles Targeted: *Biceps Brachii (Short Head)*")
        sl.markdown("""
        1. Sit on a chair with your legs apart and a dumbbell in one hand.  
        2. Rest your working elbow on the inside of your thigh, letting the weight hang down.  
        3. Curl the dumbbell toward your shoulder, keeping your upper arm still.  
        4. Squeeze at the top, then lower with control.  
        5. Repeat on the other arm.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps each arm, rest 30–60 seconds")

    if middle.button("Hammer Curl", use_container_width=True):
        sl.markdown("**Hammer Curl**")
        sl.markdown("Muscles Targeted: *Biceps Brachii (Long Head)*")
        sl.markdown("""
        1. Stand with a dumbbell in each hand, arms at your sides, palms facing inward.  
        2. Curl both dumbbells up while keeping your palms facing each other throughout the motion.  
        3. Pause at the top, then lower both arms with control.  
        4. Focus on keeping your elbows close to your torso.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps, rest 30–60 seconds")

    if right.button("Resistance Band Curl", use_container_width=True):
        sl.markdown("**Resistance Band Curl**")
        sl.markdown("Muscles Targeted: *Biceps Brachii (Both Heads)*")
        sl.markdown("""
        1. Stand on the center of a resistance band and hold a handle in each hand.  
        2. Keep your elbows close to your body and curl the handles up toward your shoulders.  
        3. Squeeze your biceps at the top, then slowly lower the handles back down.  
        4. Control the tension throughout the movement.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps, rest 30–60 seconds")
