import streamlit as sl

def run_glutes():
    tests = ["Glute Bridge Hold", "Single-Leg Step-Up"]

    sl.text_area(
    'Glute Bridge Hold (gluteus maximus):',
    "1. Lie on your back with knees bent and feet flat on the floor, hip-width apart.\n"
    "2. Press through your heels and lift your hips until your body forms a straight line from shoulders to knees.\n"
    "3. Hold this position for 20–30 seconds while squeezing your glutes.\n"
    "4. Keep your core engaged and avoid arching your lower back.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
    )

    sl.text_area(
    'Single-Leg Step-Up (gluteus medius/minimus):',
    "1. Stand in front of a low step or sturdy platform.\n"
    "2. Step up with one leg, pressing through the heel to lift your body.\n"
    "3. Avoid pushing off the back foot and keep your knee aligned over your ankle.\n"
    "4. Slowly lower back down and repeat on the other side.\n"
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
                sl.error(f"Muscle Imbalance Detected in Glutes during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Glute during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Glute during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")

def run_flexors():
    tests = ["Knee-to-Chest Hold", "Seated Hip Flexion"]

    sl.text_area(
    'Knee-to-Chest Hold (iliopsoas, rectus femoris):',
    "1. Lie on your back with legs extended.\n"
    "2. Pull one knee toward your chest using your hands while keeping the other leg flat.\n"
    "3. Hold the stretch for 20–30 seconds and feel for resistance or tightness.\n"
    "4. Switch legs and repeat on the other side.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if movement felt strong and pain-free, or 'positive' if it felt weak, unstable, or painful for that side."
    )

    sl.text_area(
    'Seated Hip Flexion Test (iliopsoas):',
    "1. Sit upright on a chair with feet flat on the floor.\n"
    "2. Lift one knee as high as possible without leaning back or shifting weight.\n"
    "3. Hold the lifted position for 5–10 seconds, then lower with control.\n"
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
                sl.error(f"Muscle Imbalance Detected in Hip Flexors during {test}")
                imbalance_detected = True
            elif left == 1 and right == 0:
                sl.error(f"Muscle Imbalance Detected in Left Hip Flexor during {test}")
                imbalance_detected = True
            elif right == 1 and left == 0:
                sl.error(f"Muscle Imbalance Detected in Right Hip Flexor during {test}")
                imbalance_detected = True
        
        if imbalance_detected == False:
            sl.success("Congrats! No muscle imbalances were detected.")