import streamlit as sl

def quad_exercises():
    sl.header('Quadriceps')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/quad.png', width=250)
    with text:
        sl.text_area('', "The quadriceps, or 'quads', are a group of four muscles located on the front of the thigh: rectus femoris, vastus lateralis, vastus medialis, and vastus intermedius. These muscles work together to extend the knee and stabilize the leg during walking, running, squatting, and jumping. The rectus femoris also assists in hip flexion. Weakness or imbalance in the quads can lead to knee pain, reduced athletic performance, and increased risk of injury during lower body movements.")

    left, middle, right = sl.columns(3)

    if left.button("Bodyweight Squat", use_container_width=True):
        sl.markdown("**Bodyweight Squat**")
        sl.markdown("Muscles Targeted: *All Quadriceps (Especially Vastus Lateralis and Medialis)*")
        sl.markdown("""
        1. Stand with feet shoulder-width apart and toes slightly turned out.  
        2. Lower your body by bending your knees and hips as if sitting into a chair.  
        3. Go as low as your mobility allows while keeping heels on the ground.  
        4. Push through your heels to return to standing.  
        5. Keep your chest up and knees tracking over toes.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps, rest 30–60 seconds")

    if middle.button("Resistance Band Step-Up", use_container_width=True):
        sl.markdown("**Resistance Band Step-Up**")
        sl.markdown("Muscles Targeted: *Rectus Femoris, Vastus Medialis*")
        sl.markdown("""
        1. Anchor a resistance band under one foot and step onto a bench or box.  
        2. Hold the other end of the band at shoulder level on the same side.  
        3. Step up by pushing through the heel of the front foot.  
        4. Slowly lower yourself down with control.  
        5. Repeat all reps on one leg, then switch sides.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–12 reps per leg, rest 30–60 seconds")

    if right.button("Wall Sit Hold", use_container_width=True):
        sl.markdown("**Wall Sit Hold**")
        sl.markdown("Muscles Targeted: *All Quadriceps (Isometric Focus)*")
        sl.markdown("""
        1. Stand with your back against a wall and feet about 2 feet away.  
        2. Slide down until your knees form a 90° angle.  
        3. Hold this seated position, keeping your back and hips flat against the wall.  
        4. Keep knees over ankles and breathe steadily.  
        5. Optionally, lift one leg to isolate sides.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 30–60 second holds, rest 45–60 seconds")


def hamstring_exercises():
    sl.header('Hamstrings')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/hamstrings.png', width=250)
    with text:
        sl.text_area('', "The hamstrings are a group of three muscles located at the back of the thigh: biceps femoris, semitendinosus, and semimembranosus. They are responsible for knee flexion, hip extension, and play a vital role in running, jumping, and bending. Tight or weak hamstrings can increase the risk of injury and contribute to lower back pain or reduced athletic performance.")

    left, middle, right = sl.columns(3)
    if left.button("Hamstring Walkout", use_container_width=True):
        sl.markdown("**Hamstring Walkout**")
        sl.markdown("Muscles Targeted: *All Hamstring Muscles*")
        sl.markdown("""
        1. Start in a glute bridge position.  
        2. Walk your feet slowly forward, one heel at a time, keeping hips lifted.  
        3. Once extended, walk them back in.  
        4. Maintain control and tension in the hamstrings.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 6–8 walkouts, rest 45–60 seconds")

    if middle.button("Resistance Band Leg Curl", use_container_width=True):
        sl.markdown("**Resistance Band Leg Curl**")
        sl.markdown("Muscles Targeted: *Hamstrings*")
        sl.markdown("""
        1. Anchor a resistance band to a low point behind you.  
        2. Lie on your stomach and attach the band to your ankles.  
        3. Curl your heels toward your glutes, keeping hips down.  
        4. Control the motion as you return to start.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps, rest 30–60 seconds")

    if right.button("Good Morning", use_container_width=True):
        sl.markdown("**Good Morning**")
        sl.markdown("Muscles Targeted: *Hamstrings, Lower Back*")
        sl.markdown("""
        1. Stand with feet shoulder-width apart and hands behind your head.  
        2. Hinge forward at the hips while keeping your back flat.  
        3. Go until your torso is nearly parallel to the ground.  
        4. Return to standing by squeezing the hamstrings.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 10–15 reps, rest 45–60 seconds")


def calf_exercises():
    sl.header('Calves')
    image, text = sl.columns(2)
    with image:
        sl.image('data/images/calves.png', width=250)
    with text:
        sl.text_area('', "The calf is made up of two primary muscles: the gastrocnemius and the soleus. These muscles are responsible for plantarflexion and play an essential role in walking, running, and jumping. Strong, flexible calves contribute to ankle stability and efficient lower body movement. Imbalance or tightness in the calves can lead to foot, ankle, or Achilles tendon problems.")

    left, middle, right = sl.columns(3)
    if left.button("Standing Calf Raise", use_container_width=True):
        sl.markdown("**Standing Calf Raise**")
        sl.markdown("Muscles Targeted: *Gastrocnemius*")
        sl.markdown("""
        1. Stand tall with feet hip-width apart.  
        2. Slowly rise onto the balls of your feet as high as possible.  
        3. Pause at the top and lower down with control.  
        4. Use a wall or chair for balance if needed.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 15–20 reps, rest 30–45 seconds")

    if middle.button("Seated Calf Raise", use_container_width=True):
        sl.markdown("**Seated Calf Raise**")
        sl.markdown("Muscles Targeted: *Soleus*")
        sl.markdown("""
        1. Sit on a chair with feet flat on the ground.  
        2. Place a dumbbell or weighted object on your thighs above the knees.  
        3. Raise your heels while keeping toes on the ground.  
        4. Lower slowly and repeat.
        """)
        sl.markdown("**Reps/Sets:** 2–3 sets of 12–15 reps, rest 30–45 seconds")

    if right.button("Jump Rope", use_container_width=True):
        sl.markdown("**Jump Rope**")
        sl.markdown("Muscles Targeted: *Gastrocnemius, Soleus*")
        sl.markdown("""
        1. Use a jump rope and jump with both feet, landing softly on the balls of your feet.  
        2. Maintain a quick rhythm while staying light on your toes.  
        3. Keep knees slightly bent and core engaged.  
        4. Start slow and increase duration as you improve.
        """)
        sl.markdown("**Reps/Sets:** 2–3 rounds of 30–60 seconds, rest 45–60 seconds")

