import streamlit as st
import json
import numpy as np
import time

# Generator function that processes data in stages and yields progress updates
def main_process(data):
    # Step 1: Calculate the angle
    angle = data['slider1'] + data['slider2'] * 10 if data['checkbox1'] else data['slider2']
    yield "Step 1: Calculated angle.", 25, angle, None, None
    time.sleep(0.5)  # Simulate delay

    # Step 2: Generate Point Cloud 1
    size = 5
    point_cloud1 = np.random.rand(size, 3) * data['slider1']
    yield "Step 2: Generated Point Cloud 1.", 50, angle, point_cloud1, None
    time.sleep(0.5)

    # Step 3: Generate Point Cloud 2
    point_cloud2 = np.random.rand(size, 3) * data['slider2']
    yield "Step 3: Generated Point Cloud 2.", 75, angle, point_cloud1, point_cloud2
    time.sleep(0.5)

    # Final step: Complete processing
    yield "Processing complete.", 100, angle, point_cloud1, point_cloud2

# Streamlit app UI components
st.title('Point Cloud Processing Interface')

slider1 = st.slider('Slider 1', min_value=0, max_value=100, value=50)
slider2 = st.slider('Slider 2', min_value=0, max_value=100, value=50)
checkbox1 = st.checkbox('Checkbox 1', value=True)
checkbox2 = st.checkbox('Checkbox 2', value=False)

progress_bar = st.progress(0)

if st.button('Start Processing'):
    input_data = {
        'slider1': slider1,
        'slider2': slider2,
        'checkbox1': checkbox1,
        'checkbox2': checkbox2
    }

    with open('user_inputs.json', 'w') as f:
        json.dump(input_data, f)

    # Initialize variables for final output
    angle = None
    point_cloud1 = None
    point_cloud2 = None

    # Iterate through generator to update progress bar and display results
    for message, progress, angle, point_cloud1, point_cloud2 in main_process(input_data):
        st.write(message)
        progress_bar.progress(progress)
        time.sleep(0.5)

    if angle is not None:
        st.write(f'Final Angle Value: {angle}')
    else:
        st.error("Processing failed.")
