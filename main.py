import subprocess
import sys

from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout


def download_on_mac():
    subprocess.run(["ffdl", "install", "snapshot", "-y"])


def download_on_mac_two():
    subprocess.run(["python", "-m", "ffmpeg_downloader", "install", "snapshot", "-y"])


def uninstall():
    subprocess.run(["ffdl", "uninstall", "-y"])


def uninstall_two():
    subprocess.run(["python", "-m", "ffmpeg_downloader", "uninstall", "-y"])


if __name__ == "__main__":
    app = QApplication()

    dialog = QDialog()
    layout = QVBoxLayout(dialog)
    dialog.setLayout(layout)

    mac_btn = QPushButton(parent=dialog, text="Download on mac")
    mac_btn_two = QPushButton(parent=dialog, text="Download on mac 2")
    uninstall_btn = QPushButton(parent=dialog, text="Uninstall")
    uninstall_btn_two = QPushButton(parent=dialog, text="Uninstall 2")

    layout.addWidget(mac_btn)
    layout.addWidget(mac_btn_two)
    layout.addWidget(uninstall_btn)
    layout.addWidget(uninstall_btn_two)

    dialog.show()

    mac_btn.clicked.connect(download_on_mac)
    mac_btn_two.clicked.connect(download_on_mac_two)
    uninstall_btn.clicked.connect(uninstall)
    uninstall_btn_two.clicked.connect(uninstall_two)

    sys.exit(app.exec())
