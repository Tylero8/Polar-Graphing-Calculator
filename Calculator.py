import numpy as np
import matplotlib.pyplot as plt
import re


def plot_polar_graph(equation):
    # Extend the theta range to 4*pi to accommodate more complex patterns
    theta = np.linspace(0, 4 * np.pi, 2000)

    # Preprocess the equation
    equation_processed = re.sub(r'r\s*=\s*', '', equation).strip()

    # Safely evaluate the r equation
    safe_dict = {'theta': theta, 'np': np, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan}

    # Initialize r array
    r = np.zeros_like(theta)

    try:
        # Check if the equation is a simple constant (e.g., "2")
        if re.match(r'^[\d.]+$', equation_processed):
            r.fill(float(equation_processed))  # Fill r with the constant value
        else:
            # Evaluate the equation for theta
            r = eval(equation_processed, {"__builtins__": None}, safe_dict)

        # Adjust for negative radii
        for i in range(len(theta)):
            if r[i] < 0:
                r[i] = -r[i]  # Make radius positive
                theta[i] = theta[i] + np.pi  # Reflect the angle

    except Exception as e:
        print(f"Error evaluating the equation: {e}")
        return

    # Create polar plot with adjustments
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)

    # Set the title and show the plot
    ax.set_title('Polar Graph of ' + equation)
    plt.show()


# Example use
equation = input("Enter your polar equation in the form of 'r = ...' using 'theta' for θ: ")
plot_polar_graph(equation)
