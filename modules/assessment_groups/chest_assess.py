import streamlit as sl

def run_pecs():
    tests = ['Wall Push-Up Test', 'Single-Arm Resistance Band Chest Press']

    sl.text_area(
    'Wall Push-Up Test (pectoralis major):',
    "1. Stand facing a wall with your feet shoulder-width apart, about 2 feet away.\n"
    "2. Place your hands on the wall at chest height and shoulder-width apart.\n"
    "3. Slowly lower your chest toward the wall by bending your elbows.\n"
    "4. Push back to the starting position by engaging your chest and keeping your elbows at a 45° angle.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
    )
    
    sl.text_area(
    'Single-Arm Resistance Band Chest Press (pectoralis major):',
    "1. Anchor a resistance band behind you at chest height.\n"
    "2. Stand with one foot slightly forward and hold the band handle in one hand, elbow bent and hand at chest level.\n"
    "3. Press your hand forward until your arm is fully extended, then return slowly to the starting position.\n"
    "4. Keep your core engaged and body stable during the press.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
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
                sl.error(f"Muscle Imbalance Detected in Pecs during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Pec during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Pec during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")