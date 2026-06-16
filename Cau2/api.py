import sys
from PyQt6.QtWidgets import QApplication

from ui.transposition import TranspositionUI

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TranspositionUI()
    window.show()

    sys.exit(app.exec())