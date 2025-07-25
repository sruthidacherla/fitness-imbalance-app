import streamlit as sl

def run_triceps():
    tests = ["Overhead Triceps Extension"]

    sl.text_area(
        'Overhead Triceps Extension - Dumbbell/Resistance Band:',
        "1. Start by holding a light dumbbell/resistance band in one hand, with your elbow bent and your hand resting behind your head.\n"
        "2. Your elbow should point straight up toward the ceiling, close to your ear.\n"
        "3. From this position, fully extend your arm overhead until your arm is straight.\n"
        "4. Slowly lower back down to the starting position behind your head with control.\n"
        "5. Repeat on the other arm.\n"
        "6. Compare both sides for strength, control, or discomfort.\n"
        "7. Select 'negative' if the movement was strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that arm."
    )

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
        imbalance_detected = False
        
        for test, outcome in results.items():
            left = outcome["left"]
            right = outcome["right"]

            if left == 1 and right == 1:
                sl.error(f"Muscle Imbalance Detected in both Triceps during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Tricep during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Tricep during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")

def run_biceps():
    tests = ["Concentration Curl"]

    sl.text_area(
        'Concentration Curl - Dumbbell:',
        "1. Sit on a chair with your legs apart and a light dumbbell in one hand.\n"
        "2. Lean slightly forward and rest the back of your working arm’s elbow on the inside of your thigh, allowing the dumbbell to hang down.\n"
        "3. From this position, curl the dumbbell upward toward your shoulder, keeping your upper arm still.\n"
        "4. Squeeze your bicep at the top, then slowly lower back to the starting position with control.\n"
        "5. Repeat on the other arm.\n"
        "6. Compare both sides for strength, control, or discomfort.\n"
        "7. Select 'negative' if the movement was strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that arm."
    )

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
        imbalance_detected = False
        
        for test, outcome in results.items():
            left = outcome["left"]
            right = outcome["right"]

            if left == 1 and right == 1:
                sl.error(f"Muscle Imbalance Detected in both Biceps during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Bicep during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Bicep during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")

