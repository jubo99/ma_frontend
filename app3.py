import streamlit as st
import json
import numpy as np
import time

# Generator function that processes data in stages and yields progress updates
def main_process(data):
    yield "Starting processing..."
    time.sleep(0.5)

    angle = data['slider1'] + data['slider2'] * 10 if data['checkbox1'] else data['slider2']
    yield f"Calculated angle: {angle}"
    time.sleep(0.5)

    size = 5
    point_cloud1 = np.random.rand(size, 3) * data['slider1']
    yield "Generated Point Cloud 1."
    time.sleep(0.5)

    point_cloud2 = np.random.rand(size, 3) * data['slider2']
    yield "Generated Point Cloud 2."
    time.sleep(0.5)

    yield "Processing complete."

# Initialize Streamlit UI components
st.title('Point Cloud Processing Interface')

slider1 = st.slider('Slider 1', min_value=0, max_value=100, value=50)
slider2 = st.slider('Slider 2', min_value=0, max_value=100, value=50)
checkbox1 = st.checkbox('Checkbox 1', value=True)
checkbox2 = st.checkbox('Checkbox 2', value=False)

progress_bar = st.progress(0)
terminal_output = st.empty()  # Placeholder for terminal output

# Initialize a list for cumulative logs if it doesn't exist
if 'terminal_logs' not in st.session_state:
    st.session_state['terminal_logs'] = []

if st.button('Start Processing'):
    input_data = {
        'slider1': slider1,
        'slider2': slider2,
        'checkbox1': checkbox1,
        'checkbox2': checkbox2
    }
    with open('user_inputs.json', 'w') as f:
        json.dump(input_data, f)

    st.session_state['terminal_logs'] = []  # Clear previous logs
    progress = 0
    steps = 5  # Number of steps to evenly distribute progress

    for log in main_process(input_data):
        st.session_state['terminal_logs'].append(log)
        progress += 100 // steps
        progress_bar.progress(min(progress, 100))
        terminal_output.text_area("Live Terminal Logs", "\n".join(st.session_state['terminal_logs']), height=300, key="live_logs_area")
        time.sleep(0.5)

# Allow users to view logs after processing only if they exist
if st.session_state['terminal_logs']:
    with st.expander("View detailed logs"):
        st.text_area("Final Logs", "\n".join(st.session_state['terminal_logs']), height=300, key="final_logs_area")
