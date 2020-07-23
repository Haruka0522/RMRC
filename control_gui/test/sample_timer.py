from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Main(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self._check_timer = QTimer()
        self._check_timer.timeout.connect(self._check)
        self._check_timer.setInterval(20000)

        self._layout = QVBoxLayout()

        self._start_button = QPushButton('start')
        self._layout.addWidget(self._start_button)
        self._start_button.pressed.connect(
            lambda: QTimer.singleShot(0, self._check)
        )

        self._stop_button = QPushButton('stop')
        self._layout.addWidget(self._stop_button)
        self._stop_button.pressed.connect(self._check_timer.stop)

        self.setLayout(self._layout)


    def _check(self):
        def check_n_times(n):
            if n == 0:
                print()
                return

            print(f'{datetime.now().strftime("%M.%S.%f")} check once')
            QTimer.singleShot(1000, lambda: check_n_times(n-1))

        check_n_times(10)
        self._check_timer.start()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    m = Main()
    m.show()

    sys.exit(app.exec_())
