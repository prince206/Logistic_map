import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class LogisticMapVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Logistic Map Visualizer")
        self.x0_entry = None
        self.r_entry = None
        self.n_iterations_entry = None
        self.controls_frame = None
        self.plot_canvas = None
        self.draw_widgets()

    def draw_widgets(self):
        # x0 widget
        x0_label = tk.Label(self.root, text="Initial value of x (x0)")
        x0_label.pack(side="top", pady=5)
        self.x0_entry = tk.Entry(self.root, width=5)
        self.x0_entry.insert(0, "0.5")
        self.x0_entry.pack(side="top", pady=5)

        # r widget
        r_label = tk.Label(self.root, text="Growth rate (r)")
        r_label.pack(side="top", pady=5)
        self.r_entry = tk.Entry(self.root, width=5)
        self.r_entry.insert(0, "3.5")
        self.r_entry.pack(side="top", pady=5)

        # Number of iterations widget
        n_iterations_label = tk.Label(self.root, text="Number of iterations")
        n_iterations_label.pack(side="top", pady=5)
        self.n_iterations_entry = tk.Entry(self.root, width=5)
        self.n_iterations_entry.insert(0, "100")
        self.n_iterations_entry.pack(side="top", pady=5)

        # Update button
        update_button = tk.Button(self.root, text="Update", command=self.draw_plot)
        update_button.pack(side="top", pady=10)

        # Controls frame
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(side="top")

        # Plot canvas
        self.plot_canvas = tk.Canvas(self.root, width=500, height=400)
        self.plot_canvas.pack(side="top", pady=10)

    def draw_plot(self):
        # Get the user input
        x0 = float(self.x0_entry.get())
        r = float(self.r_entry.get())
        n_iterations = int(self.n_iterations_entry.get())

        # Initialize the arrays for r and x values
        rs = []
        xs = []

        # Calculate the x values for each iteration
        x = x0
        for i in range(n_iterations):
            xs.append(x)
            rs.append(r)
            x = r * x * (1 - x)

        # Create a new figure
        fig = Figure(figsize=(5, 4), dpi=100)

        # Add a subplot to the figure
        ax = fig.add_subplot(111)

        # Plot the x values
        ax.plot(xs)

        # Set the x-axis label
        ax.set_xlabel("Iteration")

        # Set the y-axis label
        ax.set_ylabel("x")

        # Set the plot title
        ax.set_title("Logistic Map")

        # Save the plot to a PNG file
        fig.savefig("logistic_map.png")

        # Show the plot on the plot canvas
        plot_img = tk.PhotoImage(file="logistic_map.png")
        self.plot_canvas.create_image(0, 0, anchor="nw", image=plot_img)
        self.plot_canvas.image = plot_img

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    visualizer = LogisticMapVisualizer()
    visualizer.run()
