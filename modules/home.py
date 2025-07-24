import streamlit as sl

def home():

    sl.title('Muscle Imbalance Tracker')

    sl.header('What is Muscle Imbalance?')
    text, pics = sl.columns(2)
    with pics:
        sl.image('data/images/uneven_biceps.png', width = 250)
    with text:
        sl.write("""
                 Muscle imbalance occurs when a muscle on one side of your body is **stronger, more flexible, or better developed** than its counterpart on the opposite side. This can lead to: uneven movement, poor posture, and potential injury. 
                **Common Example:** Many right-handed individuals can lift more with their right bicep than their left.
                 """)
    
    sl.header('What are some Common Causes?')
    pic, block = sl.columns(2)
    with pic: 
        sl.image('data/images/bag_carry.png', width = 300)
    with block:
        sl.write( """
            - Poor Posture (Scoliosis, Slouching, etc)
            - Repetitive use of one side (Always carrying a bag with one arm)
            - Improper training (Overtraining chest, undertraining back)
        """
        )
    
    sl.header('Examples')
    text, pic = sl.columns(2)
    with text:
        sl.write( """
            - **Knee pain:** Overdeveloped quads + weak hamstrings → knee joint strain.
            - **Hip imbalance:** Weak glutes + tight hip flexors → lower back pain, poor gait
            - **Bad Posture:** Overtraining chest and neglecting back muscles → rounded shoulders 
        """
        )
    with pic:
        sl.image('data/images/kneepain.png', width = 200)

    sl.header('How to use the Muscle Imbalance Tracker!')
    sl.write( """
            1) **Login/Register**
            2) **Take the Assessment** for any muscle or muscle group  
            3) **View Your Results** and go to the **Muscle Groups** page to see targeted exercises
            4) **Reassess** after a few weeks by taking the Assessment Again to track progress
        """
        )
