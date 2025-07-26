import streamlit as sl

def run_quads():
    tests = ["Wall Sit", 'Step-Up']

    sl.text_area(
    'Wall Sit Test:',
    "1. Stand with your back flat against a wall and your feet about shoulder-width apart, 1–2 feet away from the wall.\n"
    "2. Slide down the wall until your knees are bent at 90° and your thighs are parallel to the floor.\n"
    "3. Hold this position for as long as you can while keeping your back and hips pressed against the wall.\n"
    "4. Repeat by lifting one leg slightly off the floor to isolate each side individually.\n"
    "5. Compare both sides for strength, control, or discomfort.\n"
    "6. Select 'negative' if the hold was strong and pain-free, or 'positive' if weakness, shaking, or pain occurred on one side."
    )

    sl.text_area(
    'Resistance Band Step-Up:',
    "1. Anchor a resistance band under one foot and step onto a sturdy bench or platform.\n"
    "2. Hold the other end of the band in the same-side hand (resting near your shoulder).\n"
    "3. Press through the foot on the step to lift your body upward against the band's resistance.\n"
    "4. Slowly lower yourself back down with control.\n"
    "5. Repeat on the other leg.\n"
    "6. Compare both sides for strength, balance, or discomfort.\n"
    "7. Select 'negative' if the movement was strong and pain-free, or 'positive' if it felt weak, wobbly, or painful for one side."
    )