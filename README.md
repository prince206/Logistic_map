# Logistic Map Visualizer

This is a Python program that visualizes the logistic map, a mathematical function that is used to model population growth. The program uses the tkinter library to create a graphical user interface (GUI) and the matplotlib library to create the plot.

## Requirements

- Python 3.x
- tkinter
- matplotlib

## Usage

To use this program, run the following command in your terminal:

```
git clone https://github.com/prince206/Logistic_map.git
cd Logistic_map
python logistic_map_visualizer.py
```

This will launch the GUI window. Enter the initial value of x (x0), growth rate (r), and number of iterations in their respective fields. Then click on the "Update" button to generate the plot.

The plot will be displayed on a canvas in the GUI window. It will also be saved as a PNG file named "logistic_map.png" in the same directory as your script.

## Class Structure

### LogisticMapVisualizer

This is the main class of our program. It creates and manages all GUI elements, including labels, text fields, buttons, and canvas. It also handles user input and generates plots based on that input.

#### Methods

- `__init__(self)`: Initializes an instance of `LogisticMapVisualizer`. Creates a new tkinter window with a title "Logistic Map Visualizer". Initializes class variables for text fields (`x0_entry`, `r_entry`, `n_iterations_entry`), controls frame (`controls_frame`), and plot canvas (`plot_canvas`). Calls `draw_widgets()` method to draw all GUI elements.
- `draw_widgets(self)`: Draws all GUI elements using tkinter widgets such as labels, text fields, buttons, and canvas.
- `draw_plot(self)`: Generates a plot based on user input. Reads values from text fields (`x0_entry`, `r_entry`, `n_iterations_entry`). Calculates x values using logistic map formula for each iteration. Plots x values on a matplotlib figure. Saves the plot as a PNG file named "logistic_map.png". Displays the plot on the plot canvas.
- `run(self)`: Runs the tkinter mainloop to display the GUI window.

## License

This program is licensed under the MIT License. See LICENSE file for more information.
