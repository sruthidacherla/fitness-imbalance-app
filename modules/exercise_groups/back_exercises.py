import streamlit as sl

def lowerback_exercises():
    sl.header('Lower Back')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/lower_back.png', width = 250)
    with text:
        sl.text_area('', "The lower back is primarily supported by the erector spinae, multifidus, and quadratus lumborum muscles. These muscles work together to stabilize the spine, support posture, and enable movements like bending, lifting, and twisting. A strong lower back is essential for daily tasks and athletic performance. Weakness or imbalance in these muscles can result in pain, limited mobility, and increased risk of injury, especially during lifting or rotational movements.")
    left, middle, right = sl.columns(3)
    if left.button("Superman Reps", use_container_width=True):
        sl.markdown("**Superman Reps**")
        sl.markdown("Muscles Targeted: *Erector Spinae*")
        sl.markdown("""
        1. Lie face down on the floor with your arms extended straight ahead and legs behind you.  
        2. Lift your chest, arms, and legs off the ground at the same time.  
        3. Pause at the top for 2–3 seconds while squeezing your lower back.  
        4. Lower back down with control.  
        5. Repeat for reps rather than holding.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps, rest 30–45 seconds")

    if middle.button("Bird Dog Reps", use_container_width=True):
        sl.markdown("**Bird Dog Reps**")
        sl.markdown("Muscles Targeted: *Multifidus, Core Stabilizers*")
        sl.markdown("""
        1. Begin on hands and knees in a tabletop position.  
        2. Extend your right arm and left leg simultaneously.  
        3. Pause for 2–3 seconds, focusing on spinal stability and balance.  
        4. Return to starting position and repeat on the other side.  
        5. Move slowly and keep your hips level.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 8–10 reps per side, rest 30–45 seconds")
        
    if right.button("Side Plank Hip Lifts", use_container_width=True):
        sl.markdown("**Side Plank Hip Lifts**")
        sl.markdown("Muscles Targeted: *Quadratus Lumborum (QL), Obliques*")
        sl.markdown("""
        1. Start in a side plank with your elbow under your shoulder and legs stacked.  
        2. Lower your hips toward the floor slightly without touching it.  
        3. Lift your hips back up to the starting position, squeezing your side.  
        4. Perform all reps on one side before switching.  
        5. Keep your body in a straight line throughout.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–12 reps per side, rest 30–45 seconds")

def upperback_exercises():
    sl.header('Upper Back')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/upper_back.png', width = 250)
    with text:
        sl.text_area('', "The upper back is made up of several muscles, including the trapezius, rhomboids, and latissimus dorsi. These muscles work together to support posture, stabilize the shoulder blades, and control arm and upper body movements. The trapezius spans the upper spine and neck, helping with shoulder elevation and retraction. The rhomboids lie beneath it, pulling the shoulder blades inward. The latissimus dorsi, the largest upper body muscle, extends the arms and supports powerful pulling motions. \nWeakness or imbalance in the upper back can lead to poor posture, rounded shoulders, or pain during overhead or pulling activities.")
    left, middle, right = sl.columns(3)

    if left.button("Band Face Pull", use_container_width=True):
        sl.markdown("**Resistance Band Face Pull**")
        sl.markdown("Muscles Targeted: *Trapezius, Rhomboids*")
        sl.markdown("""
        1. Anchor a resistance band at chest height and hold one end in each hand.  
        2. Step back to create tension with arms extended in front of you.  
        3. Pull the band toward your face while flaring your elbows out to the sides.  
        4. Squeeze your shoulder blades together at the peak.  
        5. Slowly return to the start position with control.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps, rest 30–45 seconds")

    if middle.button("Bent Over Row", use_container_width=True):
        sl.markdown("**Bent Over Row (Dumbbell or Band)**")
        sl.markdown("Muscles Targeted: *Rhomboids, Mid Trapezius*")
        sl.markdown("""
        1. Hold a dumbbell in each hand (or use a resistance band under your feet).  
        2. Hinge at the hips to bring your torso almost parallel to the floor.  
        3. Pull the weights/band handles toward your waist, squeezing your shoulder blades together.  
        4. Lower back to starting position slowly.  
        5. Keep your back flat and elbows close to your sides.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–12 reps, rest 45–60 seconds")

    if right.button("Lat Pulldown (Band)", use_container_width=True):
        sl.markdown("**Resistance Band Lat Pulldown**")
        sl.markdown("Muscles Targeted: *Latissimus Dorsi*")
        sl.markdown("""
        1. Anchor a resistance band overhead (e.g., over a door).  
        2. Kneel or sit with the band handles in each hand, arms extended upward.  
        3. Pull the handles down toward your chest while squeezing your lats.  
        4. Slowly return to the starting position.  
        5. Focus on shoulder depression and avoid shrugging.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps, rest 30–60 seconds")
