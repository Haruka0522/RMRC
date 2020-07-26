import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QImage, QPixmap

import vtk
from vtk.util.colors import tomato
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class MouseInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, parent=None):
        self.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent)

    def leftButtonPressEvent(self, obj, event):
        self.OnLeftButtonDown()


# class ModeToggleSwitch():


class Robot3DModel(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.create_3Dmodel()
        self.now_FL = 0
        self.now_FR = 0

    def create_3Dmodel(self):

        def setup_model(vtk_obj):
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(vtk_obj.GetOutputPort())

            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.GetProperty().SetColor(tomato)

            actor.RotateWXYZ(-90, 0, 0, 1)

            return actor

        flipper_FL = vtk.vtkSTLReader()
        flipper_FL.SetFileName("ver3fliper.stl")
        flipper_FL.Update()
        self.actor_FL = setup_model(flipper_FL)
        self.actor_FL.SetPosition(195, 0, 0)

        flipper_FR = vtk.vtkSTLReader()
        flipper_FR.SetFileName("ver3fliper.stl")
        flipper_FR.Update()
        self.actor_FR = setup_model(flipper_FR)
        self.actor_FR.SetPosition(0, 0, 0)

        flipper_BL = vtk.vtkSTLReader()
        flipper_BL.SetFileName("ver3fliper.stl")
        flipper_BL.Update()
        self.actor_BL = setup_model(flipper_BL)
        self.actor_BL.SetPosition(195, 0, 115)

        flipper_BR = vtk.vtkSTLReader()
        flipper_BR.SetFileName("ver3fliper.stl")
        flipper_BR.Update()
        self.actor_BR = setup_model(flipper_BR)
        self.actor_BR.SetPosition(0, 0, 115)

        ren = vtk.vtkRenderer()
        ren.AddActor(self.actor_FL)
        ren.AddActor(self.actor_FR)
        ren.AddActor(self.actor_BL)
        ren.AddActor(self.actor_BR)
        ren.SetBackground(0.1, 0.2, 0.4)

        frame = QFrame()
        inter = QVTKRenderWindowInteractor(frame)
        inter.SetInteractorStyle(MouseInteractorStyle())

        ren_win = inter.GetRenderWindow()
        ren_win.AddRenderer(ren)
        ren_win.SetSize(500, 500)

        ren.ResetCamera()
        ren.GetActiveCamera().Zoom(1.0)

        ren_win.Render()
        inter.Initialize()

        self.addWidget(frame)

    def update_FL(self, angle):
        self.actor_FL.RotateWXYZ(self.now_FL - angle, 0, 0, 1)
        self.now_FL = angle

    def update_FR(self, angle):
        self.actor_FR.RotateWXYZ(self.now_FR - angle, 0, 0, 1)
        self.now_FR = angle


class Slider4Flipper(QWidget):
    def __init__(self):
        super().__init__()
        self.create_sliders()

    def create_sliders(self):
        self.layout = QHBoxLayout()
        self.slider_FL = QSlider(Qt.Vertical, self)
        self.slider_FL.setMinimum(-180)
        self.slider_FL.setMaximum(180)
        self.layout.addWidget(self.slider_FL)
        self.slider_FR = QSlider(Qt.Vertical, self)
        self.slider_FR.setMinimum(-180)
        self.slider_FR.setMaximum(180)
        self.layout.addWidget(self.slider_FR)
        self.slider_BL = QSlider(Qt.Vertical, self)
        self.slider_BL.setMinimum(-180)
        self.slider_BL.setMaximum(180)
        self.layout.addWidget(self.slider_BL)
        self.slider_BR = QSlider(Qt.Vertical, self)
        self.slider_BR.setMinimum(-180)
        self.slider_BR.setMaximum(180)
        self.layout.addWidget(self.slider_BR)

        self.setLayout(self.layout)

    def update_FL(self, angle):
        self.slider_FL.setValue(angle)

    def update_FR(self, angle):
        self.slider_FR.setValue(angle)

    def update_BL(self, angle):
        self.slider_BL.setValue(angle)

    def update_BR(self, angle):
        self.slider_BR.setValue(angle)


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "TEST GUI"
        self.width = 1280
        self.height = 720
        self.counter = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        self.main_layout = QGridLayout()
        self.slider = Slider4Flipper()
        self.model = Robot3DModel()
        self.main_layout.addLayout(self.model, 0, 0)
        self.main_layout.addWidget(self.slider, 0, 1)
        self.setLayout(self.main_layout)

        self.run()
        self.show()

    def run(self):
        if self.counter == 360:
            self.counter = 0
        else:
            self.counter += 1

        self.slider.update_FL(self.counter - 180)
        self.slider.update_FR(self.counter - 90)
        self.model.update_FL(self.counter - 180)
        self.model.update_FR(self.counter - 90)
        QTimer.singleShot(100, self.run)


def main():
    app = QApplication(sys.argv)
    gui = UiMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
