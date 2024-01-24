import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def bench_user_rating(body_weight, strength_weight):
    bw_multiplier = strength_weight / body_weight

    if bw_multiplier <= 0.50:
        # Scale within 0-20
        return max(0, min(20, int(bw_multiplier / 0.50 * 20)))
    elif bw_multiplier <= 0.75:
        # Scale within 21-40
        return 21 + int((bw_multiplier - 0.50) / 0.25 * 19)
    elif bw_multiplier <= 1.25:
        # Scale within 41-70
        return 41 + int((bw_multiplier - 0.75) / 0.50 * 29)
    elif bw_multiplier <= 1.75:
        # Scale within 71-90
        return 71 + int((bw_multiplier - 1.25) / 0.50 * 19)
    elif bw_multiplier <= 2.00:
        # Scale within 91-99
        return 91 + int((bw_multiplier - 1.75) / 0.25 * 8)
    else:
        # Max out at 99 for anything above 2.00xBW
        return 99

def overhead_user_rating(body_weight, strength_weight):
    bw_multiplier = strength_weight / body_weight

    if bw_multiplier <= 0.35:
        # Scale within 0-20
        return max(0, min(20, int(bw_multiplier / 0.35 * 20)))
    elif bw_multiplier <= 0.55:
        # Scale within 21-40
        return 21 + int((bw_multiplier - 0.35) / 0.20 * 19)
    elif bw_multiplier <= 0.80:
        # Scale within 41-70
        return 41 + int((bw_multiplier - 0.55) / 0.25 * 29)
    elif bw_multiplier <= 1.10:
        # Scale within 71-90
        return 71 + int((bw_multiplier - 0.80) / 0.30 * 19)
    elif bw_multiplier <= 1.40:
        # Scale within 91-99
        return 91 + int((bw_multiplier - 1.10) / 0.30 * 8)
    else:
        # Max out at 99 for anything above 1.40xBW
        return 99

def squat_user_rating(body_weight, strength_weight):
    bw_multiplier = strength_weight / body_weight

    if bw_multiplier <= 0.75:
        # Scale within 0-20
        return max(0, min(20, int(bw_multiplier / 0.75 * 20)))
    elif bw_multiplier <= 1.25:
        # Scale within 21-40
        return 21 + int((bw_multiplier - 0.75) / 0.50 * 19)
    elif bw_multiplier <= 1.50:
        # Scale within 41-70
        return 41 + int((bw_multiplier - 1.25) / 0.25 * 29)
    elif bw_multiplier <= 2.25:
        # Scale within 71-90
        return 71 + int((bw_multiplier - 1.50) / 0.75 * 19)
    elif bw_multiplier <= 2.75:
        # Scale within 91-99
        return 91 + int((bw_multiplier - 2.25) / 0.50 * 8)
    else:
        # Max out at 99 for anything above 2.75xBW
        return 99

def deadlift_user_rating(body_weight, strength_weight):
    bw_multiplier = strength_weight / body_weight

    if bw_multiplier <= 1.00:
        # Scale within 0-20
        return max(0, min(20, int(bw_multiplier / 1.00 * 20)))
    elif bw_multiplier <= 1.50:
        # Scale within 21-40
        return 21 + int((bw_multiplier - 1.00) / 0.50 * 19)
    elif bw_multiplier <= 2.00:
        # Scale within 41-70
        return 41 + int((bw_multiplier - 1.50) / 0.50 * 29)
    elif bw_multiplier <= 2.50:
        # Scale within 71-90
        return 71 + int((bw_multiplier - 2.00) / 0.50 * 19)
    elif bw_multiplier <= 3.00:
        # Scale within 91-99
        return 91 + int((bw_multiplier - 2.50) / 0.50 * 8)
    else:
        # Max out at 99 for anything above 3.00xBW
        return 99

def calculate_pullup_rating(reps):
    if reps < 1:
        # Beginner level
        return max(0, min(20, int(reps / 1 * 20)))
    elif reps < 6:
        # Novice level
        return 21 + int((reps - 1) / 5 * 19)
    elif reps < 13:
        # Intermediate level
        return 41 + int((reps - 6) / 7 * 29)
    elif reps < 21:
        # Advanced level
        return 71 + int((reps - 13) / 8 * 19)
    elif reps < 30:
        # Elite level
        return 91 + int((reps - 21) / 9 * 8)
    else:
        # Max out at 99 for 30 or more reps
        return 99

def calculate_core_rating(seconds_of_plank):
    if seconds_of_plank < 30:
        # Beginner level
        return max(0, min(20, int(seconds_of_plank / 30 * 20)))
    elif seconds_of_plank < 60:
        # Novice level
        return 21 + int((seconds_of_plank - 30) / 30 * 19)
    elif seconds_of_plank < 120:
        # Intermediate level
        return 41 + int((seconds_of_plank - 60) / 60 * 29)
    elif seconds_of_plank < 240:
        # Advanced level
        return 71 + int((seconds_of_plank - 120) / 120 * 19)
    elif seconds_of_plank >= 240:
        # Elite level
        return min(99, 91 + int((seconds_of_plank - 240) / 160 * 8))






# Example usage
def main():
    st.title("Gym Avatar")

    # User inputs
    weight_unit = st.selectbox("Please select your weight unit:", options=["kg", "lbs"])
    body_weight = st.number_input("Please enter your weight:", min_value=0.0)
    bench = st.number_input("Please enter your bench press max:", min_value=0.0)
    overhead = st.number_input("Please enter your overhead press max:", min_value=0.0)
    squat = st.number_input("Please enter your squat max:", min_value=0.0)
    deadlift = st.number_input("Please enter your deadlift max:", min_value=0.0)
    pullup = st.number_input("Please enter your pull up reps:", min_value=0)
    plank = st.number_input("Please enter your plank time (seconds):", min_value=0)
    
    # Convert weights to kg if user chose lbs
    if weight_unit == "lbs":
        body_weight /= 2.20462
        bench /= 2.20462
        overhead /= 2.20462
        squat /= 2.20462
        deadlift /= 2.20462

    if st.button("Calculate"):
        # Ratings
        push = (bench_user_rating(body_weight, bench) + overhead_user_rating(body_weight, overhead))/2
        pull = calculate_pullup_rating(pullup)
        squat = squat_user_rating(body_weight, squat)
        hinge = deadlift_user_rating(body_weight, deadlift)
        core = calculate_core_rating(plank)
        
        # Calculate overall rating
        overall_rating = int((push + pull + squat + hinge + core) / 5)

        # Display overall rating
        st.write(f'Overall rating: {overall_rating}')

        # Categories
        categories = ['Push', 'Pull', 'Squat', 'Hinge', 'Core']

        # Values
        values = [push, pull, squat, hinge, core]

        # Number of categories
        num_vars = len(categories)

        # Compute angle of each axis
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

        # The plot is a circle, so we need to "complete the loop"
        # and append the start value to the end.
        values += values[:1]
        angles += angles[:1]
        categories += categories[:1]  # Add this line

        # Plot
        radar_fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        radar_fig.patch.set_facecolor('#FAFAFA')
        radar_fig.patch.set_alpha(0.5)

        ax.plot(angles, values, color='red', linewidth=2)
        ax.fill(angles, values, color='none')
        ax.scatter(angles[:-1], values[:-1], color='red', s=40)  # s is the size of the point
        ax.set_yticklabels([])
        ax.set_xticks(angles)
        ax.set_xticklabels(categories)
        ax.set_facecolor('#FAFAFA')
        ax.patch.set_alpha(0.5)
       
        ax.set_xticklabels(categories, color='white', fontweight='bold')

        
        
        # Annotate data points
        for i, value in enumerate(values[:-1]):
            ax.text(angles[i], value + 5, str(int(value)), color='white', fontweight='bold', 
                    horizontalalignment='center', verticalalignment='center')

        # Add the overall score to the center of the radar chart
        ax.annotate(str(overall_rating), xy=(0.5, 0.5), ha='center', va='center', 
                    fontsize=20, color='white', fontweight='bold', transform=ax.transAxes)


        # Set the limit of the y-axis (radial axis in this case) to 99
        ax.set_ylim(0, 99)

        st.pyplot(radar_fig)

if __name__ == "__main__":
    main()
    
    