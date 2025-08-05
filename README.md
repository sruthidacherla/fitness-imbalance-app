# Muscle Imbalance Tracker

An interactive **Streamlit web application** that helps users identify and address muscle imbalances through guided self-assessments and targeted exercise recommendations.

Designed as a full-stack healthtech demo to highlight skills in:

- **Python & Streamlit** for UI logic and layout  
- **Modular architecture** with reusable assessment functions  
- **Image handling** and user interaction design  
- Includes **user authentication** (login/register)  
- **Condition-based feedback and dynamic result handling**

---

🔗 **Website**: [https://muscleimbalance.streamlit.app/](https://muscleimbalance.streamlit.app/)


---

## 🚀 Features

- 🔐 **User Authentication**: Secure login and registration system using `users.json`.
- 🧠 **Assessment Module**: Self-assessment tests across major muscle groups including:
  - Shoulders (Rotator Cuff, Deltoids)
  - Arms (Biceps, Triceps)
  - Back (Upper & Lower Back)
  - Chest (Pecs)
  - Hips (Glutes, Hip Flexors)
  - Legs (Quads, Hamstrings, Calves)
- 📊 **Result Tracking**: Identifies left/right muscle imbalances with clear visual feedback.
- 🏋️ **Exercise Library**: Recommended corrective exercises with instructions, muscle targets, and sets/reps.
- 👤 **Session Handling**: Prevents unauthorized access to assessments.

---

## 🚀 Tech Stack

| Tech | Description |
|------|-------------|
| [Streamlit](https://streamlit.io) | Frontend + Backend framework |
| Python | Core programming language |
| JSON | Lightweight storage for user login info |
| AI Images | Muscle diagrams for each body part |
| GitHub | Version control and project hosting |

---

## 🚀 Project Structure

```
.
├── app.py                         # Main Streamlit entry point
├── modules/
│   ├── assessment_groups/         # Self-assessment modules by muscle group
│   │   ├── arm_assess.py
│   │   ├── back_assess.py
│   │   ├── chest_assess.py
│   │   ├── hips_assess.py
│   │   ├── leg_assess.py
│   │   └── shoulder_assess.py
│   ├── exercise_groups/          # Targeted exercises for muscle groups
│   │   ├── arm_exercises.py
│   │   ├── back_exercises.py
│   │   ├── chest_exercises.py
│   │   ├── hips_exercises.py
│   │   ├── leg_exercises.py
│   │   └── shoulder_exercises.py
│   ├── assessment.py             # Master controller for assessment routing
│   ├── exercises.py              # Master controller for exercise routing
│   ├── home.py                   # Homepage layout
│   └── login.py                  # Login, register, and user auth logic
├── data/
│   ├── images/                   # Muscle group diagrams
│   └── users.json                # Stores registered users
├── requirements.txt              # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/sruthidacherla/muscle-imbalance-checker.git
cd muscle-imbalance-checker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🚀 My Interests for this Project!

As someone who’s active in the fitness world, whether it’s lifting weights or playing sports, I’ve become highly aware of how muscle imbalances affect performance, posture, and injury risk. I’ve personally experienced these imbalances during workouts, and I’ve seen countless others at the gym and athletes struggle with the same issues.

This project was born out of that experience. I wanted to create a tool that helps people like me assess their muscle health, identify weaknesses, and take action to correct them. All in a simple, interactive way.

It also gave me the chance to combine my passions:

- 💪 Fitness and biomechanics  
- 💻 Software engineering  
- 📈 Building solutions that empower people to improve themselves

This project reflects not only my technical abilities but also my commitment to building tools that solve real, everyday problems.

---

## 📬 Contact

**Made by Sruthi Dacherla**  
[LinkedIn](https://linkedin.com/in/sruthi-dacherla) | [GitHub](https://github.com/sruthidacherla) | [Email](sruthi.dacherla@mgmail.com)
