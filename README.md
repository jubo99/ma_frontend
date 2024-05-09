# Point Cloud Processing Interface

Welcome to the Point Cloud Processing Interface! This Streamlit-based application allows you to process and visualize point clouds by manipulating input sliders and checkboxes while providing a step-by-step progress update.

## Key Features

1. **Interactive Controls:**
   - **Sliders:** Adjust two slider controls to define the parameters used in processing.
   - **Checkboxes:** Choose whether to apply a specific multiplier to one of the sliders during angle calculation.
   - **Progress Bar:** Track the progress of the data processing.

2. **Step-by-Step Processing:**
   - The `main_process` generator function processes the data in stages:
     - **Step 1:** Calculate an angle based on the slider and checkbox inputs.
     - **Step 2:** Generate the first point cloud.
     - **Step 3:** Generate the second point cloud.
   - Progress updates are shown at each stage.

## Installation

Make sure you have Python 3.7+ and the required libraries.

1. Clone the repository or copy the source code.
2. Install the dependencies:
   ```bash
   pip install streamlit numpy
   ```
   
## How to Use

1. Run the Streamlit application:
   ```bash
   streamlit run <filename.py>
   ```
   Replace `<filename.py>` with the name of your file.

2. Access the user interface in your web browser at the address shown in your terminal.

3. Adjust the sliders and checkboxes to desired values.

4. Click on the "Start Processing" button to initiate the process. You will see progress updates as each step completes.

5. At the end, view the final angle value calculated and optionally inspect the generated point clouds.

## Details of the Code

- **`main_process` Generator Function:** This function performs data processing in stages and yields progress messages with updated values:
  - **Step 1:** Calculates the angle using the input sliders and checkbox.
  - **Step 2:** Generates the first point cloud using a random generator and the value of `slider1`.
  - **Step 3:** Generates the second point cloud with `slider2`.
  
- **Streamlit UI:** The UI comprises sliders, checkboxes, a progress bar, and buttons, which provide the input parameters and visualize progress.

## Troubleshooting

- Ensure that Python and required packages are installed correctly.
- If the app does not start, check for any error messages in your terminal and resolve the indicated issues.
  
Feel free to modify or extend the application to better suit your needs. Enjoy processing your point clouds!
