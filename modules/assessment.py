import streamlit as sl
from modules.assessment_groups.shoulders import run_rotator, run_deltoids

def run_assessment(page):
    if page == 'Assessment':
        if not sl.session_state.get("login_success", False):
            sl.error("Login to start your assessment.")
    
        elif sl.session_state.login_success == True:

            sl.header("Self Assessment")

            muscle_groups = {
                "Shoulders": ["Rotator Cuff", "Deltoids"],
                "Arms": ["Triceps", "Biceps"],
                "Back": ["Lower Back", "Upper Back"],
                "Chest": ["Pecs"],
                "Hips": ["Glutes", "Hip Flexors"],
                "Legs": ["Quads", "Hamstrings", "Calves"]
            }

            group_selected = sl.selectbox('Choose a muscle group', list(muscle_groups.keys()))
            muscle_selected = sl.selectbox(f"Select a Muscle in {group_selected}", muscle_groups[group_selected])

            sl.markdown(f"""
            1) Perform the exercise/s for the muscle
            2) Complete the given evaluation for each exercise.
            3) Click Submit to check for imbalances!
            ### Assessment for {muscle_selected}:
            """)

            if group_selected == 'Shoulders':
                if muscle_selected == 'Rotator Cuff':
                    run_rotator()
                                
                if muscle_selected == 'Deltoids':
                    run_deltoids()
