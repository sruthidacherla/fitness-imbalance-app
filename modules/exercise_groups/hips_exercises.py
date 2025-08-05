import streamlit as sl

def glutes_exercises():
    sl.header('Glutes')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/glutes.png', width=250)
    with text:
        sl.text_area('', "The glutes are made up of three main muscles: gluteus maximus, gluteus medius, and gluteus minimus. These muscles are responsible for hip extension, abduction, and external rotation. They play a vital role in stabilizing the pelvis, supporting posture, and generating power during walking, running, and squatting. Weak or imbalanced glutes can lead to poor movement patterns, lower back pain, and increased risk of injury.")

    left, middle, right = sl.columns(3)

    if left.button("Glute Bridge", use_container_width=True):
        sl.markdown("**Glute Bridge**")
        sl.markdown("Muscles Targeted: *Gluteus Maximus*")
        sl.markdown("""
        1. Lie on your back with knees bent and feet flat on the floor, hip-width apart.  
        2. Press through your heels to lift your hips until your body forms a straight line from shoulders to knees.  
        3. Squeeze your glutes at the top and hold briefly.  
        4. Lower your hips back down with control.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps, rest 30–45 seconds")

    if middle.button("Clamshells", use_container_width=True):
        sl.markdown("**Clamshells (With Band Optional)**")
        sl.markdown("Muscles Targeted: *Gluteus Medius, Minimus*")
        sl.markdown("""
        1. Lie on your side with knees bent and legs stacked.  
        2. Keep your feet together and open your top knee as high as possible without moving your pelvis.  
        3. Slowly close your knee back down with control.  
        4. Add a resistance band above the knees for increased difficulty.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–12 reps per side, rest 30 seconds")

    if right.button("Step-Ups", use_container_width=True):
        sl.markdown("**Step-Ups (Weighted or Bodyweight)**")
        sl.markdown("Muscles Targeted: *Gluteus Maximus*")
        sl.markdown("""
        1. Stand in front of a box or step about knee height.  
        2. Step up with one foot, pressing through your heel to lift your body up.  
        3. Lower back down with control and repeat.  
        4. Alternate sides or complete all reps on one side first.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 8–10 reps per leg, rest 45–60 seconds")


def flexor_exercises():
    sl.header('Hip Flexors')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/hip_flexors.png', width=250)
    with text:
        sl.text_area('', "The hip flexors include the iliopsoas, rectus femoris, and sartorius muscles. These muscles are essential for lifting the thigh toward the torso, walking, running, and maintaining upright posture. Tight or weak hip flexors can contribute to back pain, limited range of motion, and postural issues. Strengthening and stretching these muscles helps improve hip stability and movement efficiency.")

    left, middle, right = sl.columns(3)

    if left.button("Knee Drive Marches", use_container_width=True):
        sl.markdown("**Knee Drive Marches**")
        sl.markdown("Muscles Targeted: *Iliopsoas, Rectus Femoris*")
        sl.markdown("""
        1. Stand tall with arms by your sides.  
        2. Drive one knee up toward your chest while balancing on the opposite leg.  
        3. Lower the leg and alternate sides with a marching motion.  
        4. Add ankle weights or resistance band for more challenge.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 20 marches (10 each leg), rest 30 seconds")

    if middle.button("Hollow Body Hold", use_container_width=True):
        sl.markdown("**Hollow Body Hold**")
        sl.markdown("Muscles Targeted: *Hip Flexors, Core*")
        sl.markdown("""
        1. Lie on your back with arms extended overhead and legs straight.  
        2. Lift your shoulders and legs off the ground, keeping your lower back pressed to the floor.  
        3. Hold this position, engaging your hip flexors and core.  
        4. Modify by bending knees or lowering arms if needed.
        """)
        sl.markdown("**Reps/Sets:** 2–3 holds of 20–30 seconds, rest 30–60 seconds")

    if right.button("Lunge Pulses", use_container_width=True):
        sl.markdown("**Lunge Pulses**")
        sl.markdown("Muscles Targeted: *Hip Flexors, Quads*")
        sl.markdown("""
        1. Step into a lunge position with one leg forward and the other back.  
        2. Lower your body halfway and begin pulsing up and down in a small range.  
        3. Focus on stretching the back leg’s hip flexor and engaging the front leg.  
        4. Switch legs after completing reps.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 15–20 pulses per leg, rest 30–45 seconds")

