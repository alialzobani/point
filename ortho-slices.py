"""
Orthogonal Slices
~~~~~~~~~~~~~~~~~

View three orthogonal slices from a mesh.

Use the :func:`pyvista.DataSetFilters.slice_orthogonal` filter to create these
slices simultaneously.
"""
# sphinx_gallery_thumbnail_number = 2
import numpy as np
import pyvista as pv
from pyvista import examples

mesh = examples.download_embryo()
mesh.bounds

##############################################################################
# Create three slices. Easily control their locations with the ``x``, ``y``,
# and ``z`` arguments.
slices = mesh.slice_orthogonal(x=100, z=75)

##############################################################################
cpos = [(540.9115516905358, -617.1912234499737, 180.5084853429126),
        (128.31920055083387, 126.4977720785509, 111.77682599082095),
        (-0.1065160140819035, 0.032750075477590124, 0.9937714884722322)]
dargs = dict(cmap='gist_ncar_r')

'''
p = pv.Plotter()
p.add_mesh(slices, **dargs)
p.show_grid()
p.show(cpos=cpos)'''


##################################
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

p = pv.Plotter()
p.add_mesh(slices, **dargs)
p.show_grid()
p.show(cpos=cpos)

mesh = cpos

p = pv.Plotter(notebook=False)
p.add_mesh(mesh, show_edges=True, color='w')

picker = Picker(p, mesh)
p.track_click_position(picker, side='right')
p.add_text('Use right mouse click to pick points')

p.show()
##############################################################################
"""
p = pv.Plotter(shape=(2,2))
# XYZ - show 3D scene first
p.subplot(1,1)
p.add_mesh(slices, **dargs)
p.show_grid()
p.camera_position = cpos
# XY
p.subplot(0,0)
p.add_mesh(slices, **dargs)
p.show_grid()
p.camera_position = 'xy'
p.enable_parallel_projection()
# ZY
p.subplot(0,1)
p.add_mesh(slices, **dargs)
p.show_grid()
p.camera_position = 'zy'
p.enable_parallel_projection()
# XZ
p.subplot(1,0)
p.add_mesh(slices, **dargs)
p.show_grid()
p.camera_position = 'xz'
p.enable_parallel_projection()

p.show()
"""
