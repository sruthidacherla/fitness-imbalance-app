import streamlit as sl

def pecs_exercises():
    sl.header('Pectorals')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/pecs.png', width=250) 
    with text:
        sl.text_area('', 
            "The pectoralis muscles include the pectoralis major and pectoralis minor. These muscles are responsible for movements like pushing, hugging, and bringing the arm across the chest. "
            "They play a key role in upper body strength, posture, and stability of the shoulder joint. "
            "Weakness or imbalance in the pecs can affect pressing strength, limit mobility, and lead to shoulder or upper back compensation.")

    left, middle, right = sl.columns(3)

    if left.button("Wall Push-Ups", use_container_width=True):
        sl.markdown("**Wall Push-Ups**")
        sl.markdown("Muscles Targeted: *Pectoralis Major (Both Heads)*")
        sl.markdown("""
        1. Stand facing a wall with your hands shoulder-width apart at chest level.  
        2. Step back slightly and keep your body in a straight line.  
        3. Bend your elbows to bring your chest toward the wall.  
        4. Push away from the wall to return to start.  
        5. Keep your core engaged throughout.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 15–20 reps, rest 30–45 seconds")

    if middle.button("Single-Arm Band Press", use_container_width=True):
        sl.markdown("**Single-Arm Resistance Band Chest Press**")
        sl.markdown("Muscles Targeted: *Pectoralis Major (Unilateral Focus)*")
        sl.markdown("""
        1. Anchor a resistance band behind you at chest height.  
        2. Hold the handle in one hand with your elbow bent and hand at chest level.  
        3. Press your hand straight forward until your arm is extended.  
        4. Slowly return to the starting position.  
        5. Repeat on the same side before switching.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–12 reps per side, rest 30–60 seconds")

    if right.button("Incline Push-Ups", use_container_width=True):
        sl.markdown("**Incline Push-Ups**")
        sl.markdown("Muscles Targeted: *Pectoralis Major (Upper Fibers)*")
        sl.markdown("""
        1. Place your hands on an elevated surface (bench, box, or wall) shoulder-width apart.  
        2. Step your feet back into a straight line from head to heels.  
        3. Lower your chest toward the surface by bending your elbows.  
        4. Push through your palms to return to start.  
        5. Keep your core tight and body aligned.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps, rest 30–45 seconds")

