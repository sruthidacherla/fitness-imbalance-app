import streamlit as sl

def run_lowerback():
    tests = ["Superman Hold", 'Bird-Dog', 'Side Plank']

    sl.text_area(
    'Superman Hold Test (erector spinae):',
    "1. Lie face down on the floor with your arms extended straight ahead and legs extended behind you.\n"
    "2. Lift your chest, arms, and legs off the ground simultaneously, engaging your lower back.\n"
    "3. Hold this position for 20–30 seconds while maintaining a steady breath.\n"
    "4. Focus on squeezing your glutes and erector spinae muscles.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
    )

    sl.text_area(
    'Bird Dog Test (multifidus):',
    "1. Start in a tabletop position on hands and knees with your back flat and core tight.\n"
    "2. Extend your right arm forward and left leg straight back at the same time.\n"
    "3. Hold this position for 5–10 seconds, keeping your hips and spine stable.\n"
    "4. Return to the starting position, then switch sides.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
    )

    sl.text_area(
    'Side Plank Test (quadratus lumborum):',
    "1. Lie on your side with your elbow directly under your shoulder and your legs stacked.\n"
    "2. Lift your hips off the floor so your body forms a straight line from head to feet.\n"
    "3. Hold this position for 20–30 seconds, engaging your obliques and lower back.\n"
    "4. Repeat on the other side.\n"
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
                sl.error(f"Muscle Imbalance Detected in Lower Back during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left side of Lower Back during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right side of Lower Back during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")

def run_upperback():
    tests = ["Shoulder Blade Squeeze", "Wall Scapular Slide", "Overhead Reach"]

    sl.text_area(
    'Shoulder Blade Squeeze Test (trapezius):',
    "1. Sit or stand tall with your arms relaxed at your sides.\n"
    "2. Squeeze your shoulder blades together as if trying to pinch a pencil between them.\n"
    "3. Hold the squeeze for 5–10 seconds while keeping your shoulders relaxed (not shrugged).\n"
    "4. Release and repeat several times.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
    )

    sl.text_area(
    'Wall Scapular Slide Test (rhomboids):',
    "1. Stand with your back flat against a wall, feet about 6 inches away from it.\n"
    "2. Raise your arms to shoulder level, bend elbows to 90°, and press your arms and hands against the wall (goalpost position).\n"
    "3. Slowly slide your arms upward as high as you can while keeping everything in contact with the wall.\n"
    "4. Return to the starting position with control.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
    )

    sl.text_area(
    'Overhead Reach Test (latissimus dorsi):',
    "1. Stand or lie flat on your back with your knees bent and feet flat on the ground.\n"
    "2. Extend both arms straight overhead and attempt to bring them to the floor behind you without arching your lower back.\n"
    "3. Keep your ribs down and back flat throughout the motion.\n"
    "4. Repeat individually for each arm to isolate sides.\n"
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
                sl.error(f"Muscle Imbalance Detected in Upper Back during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left side of Upper Back during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right side of Upper Back during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")