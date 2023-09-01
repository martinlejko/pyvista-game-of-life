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


def polyline_from_points(points):
    poly = pv.PolyData()
    poly.points = points
    the_cell = np.arange(0, len(points), dtype=np.int_)
    the_cell = np.insert(the_cell, 0, len(points))
    poly.lines = the_cell
    return poly

polyline = polyline_from_points(points)
polyline["scalars"] = np.arange(polyline.n_points)
tube = polyline.tube(radius=0.5)
tube.plot(smooth_shading=True)
