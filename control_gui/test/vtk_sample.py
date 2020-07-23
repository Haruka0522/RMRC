import vtk
from vtk.util.colors import tomato

# source
cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(20)

# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cylinder.GetOutputPort())

# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(tomato)
actor.RotateX(30.)
actor.RotateY(-45.)

# renderer
ren = vtk.vtkRenderer()
ren.AddActor(actor)
ren.SetBackground(0.1, 0.2, 0.4)

ren_win = vtk.vtkRenderWindow()
ren_win.AddRenderer(ren)
ren_win.SetSize(640, 480)

# interactor
inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(ren_win)

ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)

ren_win.Render()
inter.Initialize()
inter.Start()
