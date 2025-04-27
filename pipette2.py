import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Pipetting Like a Pro", layout="wide")

st.title("🧪 Biotech in Action: Pipetting Like a Pro")

st.markdown("""
### 🧠 Learning Goals
- Set and operate three different sizes of micropipettes correctly.
- Identify signs of common pipetting errors.
- Handle tricky solutions like viscous liquids.
- Use a balance to confirm your accuracy and precision.

---

### 📘 Background Briefing
You just got hired for a summer internship at a local biotech startup. Your job is to help prep small volumes of reagents for a new diagnostic test kit. On your first day, your supervisor hands you a box of pipettes and says:

> "We need these buffers prepared accurately. If you can't pipette 50 µL correctly, none of our tests will work."

They leave you in front of a balance and some colored solutions. No pressure. But don't worry—you've got this.

Micropipettes are precision tools used in every biotechnology lab. Each has a specific range:
- **P20:** 2–20 µL
- **P200:** 20–200 µL
- **P1000:** 100–1000 µL

Using the wrong pipette or incorrect technique can result in wasted reagents or bad data.
""")

st.markdown("---")

st.subheader("🎯 Concept Check")

q1 = st.radio("1. What happens if you use a P1000 to pipette 20 µL?",
              ["It works perfectly", "It’s less accurate than using a P20", "It delivers more than you set it to", "Nothing happens"])

q2 = st.radio("2. Which of the following can cause inaccurate pipetting?",
              ["Pushing the plunger to the second stop before drawing up liquid", "Using the wrong tip", "Not fully inserting the tip", "All of the above"])

q3 = st.radio("3. You see a bubble in your pipette tip after drawing up liquid. What should you do?",
              ["Just dispense it—close enough", "Shake the pipette", "Eject the liquid and try again", "Tap it to remove the bubble"])

st.text_input("4. Describe the difference between the first stop and second stop when using a micropipette.")
st.text_input("5. You’re pipetting a thick syrup-like solution. What’s one trick you can use to make pipetting more accurate?")

st.markdown("---")

st.subheader("🛠️ Your Turn — Precision Challenge")

st.markdown("#### Enter your pipetting data below for both red food coloring and viscous liquid")

with st.expander("Pipetting Data Entry"):
    df_combined = pd.DataFrame({
        "Solution Type": ["Red Food Coloring"] * 3 + ["Viscous Liquid"] * 3,
        "Target Volume (µL)": [20, 200, 1000, 20, 200, 1000],
        "Trial 1 Mass (g)": [0.0] * 6,
        "Trial 2 Mass (g)": [0.0] * 6,
        "Trial 3 Mass (g)": [0.0] * 6,
        "Notes": [""] * 6
    })

    edited_combined = st.data_editor(df_combined, num_rows="dynamic", key="combined_data_editor")

    if edited_combined is not None:
        edited_combined["Average Mass (g)"] = edited_combined[["Trial 1 Mass (g)", "Trial 2 Mass (g)", "Trial 3 Mass (g)"]].mean(axis=1)
        edited_combined["Std Dev (g)"] = edited_combined[["Trial 1 Mass (g)", "Trial 2 Mass (g)", "Trial 3 Mass (g)"]].std(axis=1)
        st.dataframe(edited_combined)

st.markdown("---")

st.subheader("📝 Wrap-Up: Reflection")

st.text_area("1. Which liquid was harder to pipette accurately? Why?")
st.text_area("2. What would happen if you messed up pipetting in a real biotech lab?")
st.text_area("3. What would you do differently for a sensitive experiment?")
st.text_area("4. Look at your standard deviations. What does the size of the standard deviation tell you about your experimental error or pipetting technique?")

st.success("Great job! You've practiced one of the most essential skills in biotechnology.")



