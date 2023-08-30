import pyvista as pv
import numpy as np

# Parametric equations for a trefoil knot


def trefoil_knot(theta):
    x = np.sin(theta) + 2 * np.sin(2 * theta)
    y = np.cos(theta) - 2 * np.cos(2 * theta)
    z = -np.sin(3 * theta)
    return x, y, z


# Generate points for the trefoil knot
theta_values = np.linspace(0, 2 * np.pi, 1000)
points = np.array([trefoil_knot(theta) for theta in theta_values])


pdata = pv.PolyData(points)
pdata.plot(point_size=100)
