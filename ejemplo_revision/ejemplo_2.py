import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
# This HTML approach will be valid too!
label = QLabel("<font color=red size=6>Hello World!</font>")
label.show()
app.exec()