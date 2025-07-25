import streamlit as sl

def run_rotator():
    tests = ["Empty Can Test", "Lift-Off Test", "External Rotation Test", "Patte Test"]
    sl.text_area(
        '1) Empty Can Test - Resistance Band (supraspinatus):',
        "1. Anchor a light resistance band under your foot/stable surface.\n"
        "2. Hold the band with one hand, arm by your side.\n"
        "3. Raise your arm diagonally in front of you, forming a 'Y'.\n"
        "4. Rotate your thumb downward (like pouring out a can).\n"
        "5. Slowly lift your arm to shoulder height against the band's resistance.\n"
        "6. Lower it back down with control.\n"
        "7. Repeat on the other arm.\n"
        "8. Compare each side for strength, control, or discomfort.\n"
        "9. Select 'negative' if movement was strong and pain-free, or 'positive' if it was weak or painful for that arm."
    )
    sl.text_area(
        'Lift-Off Test (subscapularis):',
        "1. Place the back of your hand on your lower back (back of hand touching your back).\n"
        "2. Try to lift your hand away from your back without arching your spine.\n"
        "3. Keep your elbow bent and close to your body as you lift.\n"
        "4. Repeat on the other arm.\n"
        "5. Compare both sides for ease of movement, control, and any pain or weakness.\n"
        "6. Then select 'negative' if you could lift easily and pain-free, or 'positive' if you could not lift, felt weakness, or had pain."
    )
    sl.text_area(
        'External Rotation - Resistance Band/Partner (infraspinatus)',
        "1. Stand tall with your arms bent at 90° and elbows tucked against your sides.\n"
        "2. Hold your forearms straight out in front of you.\n"
        "3. Ask a partner to place resistance on the outside of your wrists.\n"
        "4. Push your hands outward against the resistance, keeping your elbows at your sides.\n"
        "5. Repeat on the other arm.\n"
        "6. Compare both sides for strength, control, or any pain.\n"
        "7. Then select 'negative' if both sides were strong and pain-free, or 'positive' if one side was weaker or painful."
    )
    sl.text_area(
        'Patte Test - Partner (teres minor)',
        "1. Raise your arm so that it is parallel to the floor and bend your elbow at 90° (like you're holding a horn to your mouth).\n"
        "2. Ask a partner to gently push your hand downward while you resist, trying to keep your hand from moving.\n"
        "3. Repeat on the other arm.\n"
        "4. Compare both sides for strength and control.\n"
        "5. Then select 'negative' if you could hold the position easily and pain-free, or 'positive' if your arm dropped, felt weak, or painful."
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
                sl.error(f"Muscle Imbalance Detected in both Rotator Cuffs during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Rotator Cuff during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Rotator Cuff during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")

def run_deltoids():
    tests = ["Front Raise", "Lateral Raise", "Reverse Fly"]

    sl.text_area(
    'Front Raise - Resistance Band/Dumbell/Partner (anterior deltoid):',
    "1. Stand tall with your arms at your sides.\n"
    "2. Hold a light dumbbell, anchor a resistance band under your feet, or ask a partner to apply downward resistance.\n"
    "3. Raise one arm straight in front of you to shoulder height, palm facing the floor.\n"
    "4. Try to hold steady against the resistance.\n"
    "5. Lower your arm with control.\n"
    "6. Repeat on the other arm.\n"
    "7. Compare both sides for strength, control, or discomfort.\n"
    "8. Select 'negative' if movement was strong and pain-free, or 'positive' if it was weak or painful for that arm."
)
    sl.text_area(
    'Lateral Raise - Resistance Band/Dumbell/Partner (lateral deltoid):',
    "1. Stand tall with arms at your sides.\n"
    "2. Hold a light dumbbell, anchor a resistance band under your feet, or ask a partner to apply downward resistance.\n"
    "3. Raise one arm directly out to the side until it reaches shoulder height.\n"
    "4. Keep your elbow slightly bent and your wrist in line with your shoulder.\n"
    "5. Hold at the top, then lower with control.\n"
    "6. Repeat on the other arm.\n"
    "7. Compare both sides for strength, control, or discomfort.\n"
    "8. Select 'negative' if movement was strong and pain-free, or 'positive' if it was weak or painful for that arm."
)
    sl.text_area(
    'Reverse Fly - Resistance Band/Dumbell/Partner (posterior deltoid):',
    "1. Bend slightly forward at the waist while keeping your back straight.\n"
    "2. Hold a light dumbbell, anchor a resistance band under your feet, or ask a partner to apply resistance.\n"
    "3. With elbows slightly bent, raise your arms out to the sides until shoulder height.\n"
    "4. Squeeze your shoulder blades together at the top of the movement.\n"
    "5. Lower with control.\n"
    "6. Repeat on the other arm.\n"
    "7. Compare both sides for strength, control, or discomfort.\n"
    "8. Select 'negative' if movement was strong and pain-free, or 'positive' if it was weak or painful for that arm."
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
                sl.error(f"Muscle Imbalance Detected in both Deltoids during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Deltoid during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Deltoid during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")