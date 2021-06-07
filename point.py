import pyvista as pv
from pyvista import examples
import numpy as np


class Picker:
    def __init__(self, plotter, mesh):
        self.plotter = plotter
        self.mesh = mesh
        self._points = []

    @property
    def points(self):
        """To access all th points when done."""
        return self._points

    def __call__(self, *args):
        picked_pt = np.array(self.plotter.pick_mouse_position())
        direction = picked_pt - self.plotter.camera_position[0]
        direction = direction / np.linalg.norm(direction)
        start = picked_pt - 1000 * direction
        end = picked_pt + 10000 * direction
        point, ix = self.mesh.ray_trace(start, end, first_point=True)

        if len(point) > 0:
            self._points.append(point)
            w = p.add_mesh(pv.Sphere(radius=3, center=picked_pt),
                           color='red')
        return


mesh = examples.load_ant()

p = pv.Plotter(notebook=False)
p.add_mesh(mesh, show_edges=True, color='w')

picker = Picker(p, mesh)
p.track_click_position(picker, side='right')
p.add_text('Use right mouse click to pick points')

p.show()