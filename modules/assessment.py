import streamlit as sl

def run_assessment(choice):
    if choice == 'Assessment':
        if sl.session_state.login_success == True:

            sl.header("Self Assessment")

            assessment_completed = False

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
                    tests = ["Empty Can Test", "External Rotation Test", "Drop Arm Test"]
                    sl.text_area('1) Empty Can Test: ', "explain it")
                    sl.text_area('1) External Rotation Test: ', "explain it")
                    sl.text_area('1) Drop Arm Test: ', "explain it")

                    results = {}
                    
                    for test in tests: 
                        col1, col2 = sl.columns(2)
                        with col1:
                            left = sl.radio(
                                f"{test} (Left)",
                                options=["negative", "positive"],
                                horizontal=True,
                                key=f"{test} left"
                            )
                        with col2:
                            right = sl.radio(
                                f"{test} (Right)",
                                options=["negative", "positive"],
                                horizontal=True,
                                key=f"{test} right"
                            )
                        
                        results[test] = {
                            'left': 0 if left == 'negative' else 1,
                            'right': 0 if right == 'negative' else 1
                        }
                    
                    if sl.button('Submit Assessment'):
                        #show results for user
                        
                        for test, outcome in results.items():
                            left = outcome["left"]
                            right = outcome["right"]

                            if left == 1 and right == 1:
                                sl.error(f"Muscle Imbalance Detected in both Rotator Cuffs during {test}")
                            elif left == 1 and right == 0:
                                sl.error(f"Muscle Imbalance Detected in Left Rotator Cuff during {test}")
                            elif right == 1 and left == 0:
                                sl.error(f"Muscle Imbalance Detected in Right Rotator Cuff during {test}")

                        ##go to rotator cuff exercises
                        sl.button('Rotator Cuff Exercises')
                        

    elif sl.session_state.login_success != True and choice == 'Assessment':
        sl.error('Please login to start the Assessment!')