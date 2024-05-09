import streamlit as st
import numpy as np
import pyvista as pv
from pyvista import examples
import tempfile
import json

def main_process(data):
    # Define paths for the point clouds
    point_cloud1_path = '/tmp/point_cloud1.ply'
    point_cloud2_path = '/tmp/point_cloud2.ply'

    # Download and save point clouds
    examples.download_saddle_surface().save(point_cloud1_path)
    examples.load_random_hills().save(point_cloud2_path)

    # Calculate angle
    angle = data['slider1'] + data['slider2'] * 10 if data['checkbox1'] else data['slider2']
    yield angle, point_cloud1_path, point_cloud2_path

def load_and_display_point_cloud(path):
    # Load and display the point cloud
    mesh = pv.read(path)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color=True)
    plotter.show(jupyter_backend='panel')

st.title('Point Cloud Processing Interface')

slider1 = st.slider('Slider 1', min_value=0, max_value=100, value=50)
slider2 = st.slider('Slider 2', min_value=0, max_value=100, value=50)
checkbox1 = st.checkbox('Checkbox 1', value=True)
checkbox2 = st.checkbox('Checkbox 2', value=False)

if st.button('Process Data'):
    input_data = {
        'slider1': slider1,
        'slider2': slider2,
        'checkbox1': checkbox1,
        'checkbox2': checkbox2
    }
    
    with open('user_inputs.json', 'w') as f:
        json.dump(input_data, f)

    terminal_output = ""  # Initialize terminal content
    process_generator = main_process(input_data)
    for output in process_generator:
        if isinstance(output, tuple):
            angle, point_cloud1_path, point_cloud2_path = output
            st.write(f'Angle Value: {angle}')
            with st.expander("Point Cloud 1"):
                load_and_display_point_cloud(point_cloud1_path)
            with st.expander("Point Cloud 2"):
                load_and_display_point_cloud(point_cloud2_path)
        else:
            terminal_output += f"{output}\n"

    with st.expander("See terminal output"):
        st.text_area("Terminal", value=terminal_output, height=300, key="terminal")
