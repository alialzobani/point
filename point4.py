from vtkplotter import datadir, Plotter, Point
import vtk

def onRightClick(mesh):
    vcr = vtk.vtkCoordinate()
    vcr.SetCoordinateSystemToDisplay()
    pt = vcr.GetComputedWorldValue(vp.renderer)
    vp.add(Point(mesh.picked3d, c='black'))
    vp.add(Point(pt, c='white'))
    vp.renderer.ResetCamera()
    print(mesh.picked3d, pt)

vp = Plotter(verbose=0)
vp.load(datadir+"bunny.obj")
vp.mouseRightClickFunction = onRightClick
vp.show()