import streamlit as sl

def run_quads():
    tests = ["Wall Sit", 'Step-Up']

    sl.text_area(
        'Wall Sit:',
        "1. Stand with your back flat against a wall and your feet about shoulder-width apart, 1–2 feet away from the wall.\n"
        "2. Slide down until your knees are at 90° and thighs are parallel to the floor.\n"
        "3. Hold the position and lift one leg slightly to isolate each side.\n"
        "4. Compare both sides for strength, control, or discomfort.\n"
        "5. Select 'negative' if strong and pain-free, or 'positive' if weak, shaky, or painful."
    )

    sl.text_area(
        'Resistance Band Step-Up:',
        "1. Step onto a platform while holding a band under your stepping foot.\n"
        "2. Press up, lifting your body against resistance.\n"
        "3. Slowly return with control and repeat on the other leg.\n"
        "4. Compare both sides for strength, balance, or discomfort.\n"
        "5. Select 'negative' if strong and pain-free, or 'positive' if weak, wobbly, or painful."
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
                sl.error(f"Muscle Imbalance Detected in Quads during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Quad during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Quad during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")

def run_hamstrings():
    tests = ['Single-Leg Glute Bridge', 'Resistance Band Hamstring Curl']

    sl.text_area(
        'Single-Leg Glute Bridge Test:',
        "1. Lie on your back with one leg extended and the other foot flat.\n"
        "2. Lift your hips using the planted leg, keeping your body straight.\n"
        "3. Repeat with the other leg.\n"
        "4. Compare both sides for strength, control, or discomfort.\n"
        "5. Select 'negative' if strong and pain-free, or 'positive' if weak, unstable, or painful."
    )

    sl.text_area(
        'Hamstring Curl with Resistance Band:',
        "1. Loop a resistance band around one ankle while lying face down.\n"
        "2. Curl your heel toward your glutes against resistance.\n"
        "3. Slowly return and switch legs.\n"
        "4. Compare both sides for strength, control, or discomfort.\n"
        "5. Select 'negative' if strong and pain-free, or 'positive' if weak, shaky, or painful."
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
                sl.error(f"Muscle Imbalance Detected in Hamstrings during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Hamstring during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Hamstring during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")

def run_calves():
    tests = ['Single-Leg Calf Raise', 'Resistance Band Calf Flexion']
    sl.text_area(
        'Single-Leg Calf Raise Test:',
        "1. Stand near a wall or chair for balance.\n"
        "2. Raise up onto your toes on one foot, then slowly lower.\n"
        "3. Repeat on both sides.\n"
        "4. Compare both sides for strength, control, or discomfort.\n"
        "5. Select 'negative' if strong and pain-free, or 'positive' if weak, shaky, or painful."
    )

    sl.text_area(
        'Resistance Band Calf Flexion:',
        "1. Sit with your leg extended and a resistance band looped around your foot.\n"
        "2. Point your toes forward against resistance, then return.\n"
        "3. Repeat on both sides.\n"
        "4. Compare both sides for strength, control, or discomfort.\n"
        "5. Select 'negative' if strong and pain-free, or 'positive' if weak, shaky, or painful."
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
                sl.error(f"Muscle Imbalance Detected in Calves during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Calf during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Calf during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")
