import argparse
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from kakao_hashtag import generate_tag
from kakao_mosaic import mosaic, detect_face

class HashDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowIcon(QIcon('icon.png'))

        parser = argparse.ArgumentParser(description='Classify Tags')
        parser.add_argument('image_url', type=str, nargs='?',
                            default="https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/08.jpg",
                            help='image url to classify')

        args = parser.parse_args()

        result = generate_tag(args.image_url)

        self.button = QPushButton('추천 해시태그 확인')
        self.button.clicked.connect(self.finishButton)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(result)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)

        self.setLayout(self.vbox)

        self.setWindowTitle("HASHTAG")
        self.setGeometry(800, 400, 400, 200)

    def finishButton(self):
        self.close()

class MosDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("MOSAIC")

        parser = argparse.ArgumentParser(description='Mosaic faces.')
        parser.add_argument('image_file', type=str, nargs='?', default="./images/08.jpg",
                            help='image file to hide faces')

        args = parser.parse_args()

        detection_result = detect_face(args.image_file)
        image = mosaic(args.image_file, detection_result)
        image.show()

        self.button = QPushButton('모자이크 처리된 이미지 확인')
        self.button.clicked.connect(self.finishButton)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.button)

        self.setLayout(self.vbox)
        self.setGeometry(800, 400, 300, 100)

    def finishButton(self):
        self.close()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowIcon(QIcon('icon.png'))

        self.lbl = QLabel(self)
        self.lbl.resize(500, 600)
        pixmap = QPixmap("./images/08.jpg")
        self.lbl.setPixmap(QPixmap(pixmap))

        self.button1 = QPushButton('HashTag 추천')
        self.button2 = QPushButton('모자이크 처리하기')
        self.button1.clicked.connect(self.hashButton)
        self.button2.clicked.connect(self.mosButton)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button1)
        self.hbox.addWidget(self.button2)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lbl)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

        self.setWindowTitle("ADproject")
        self.setGeometry(500, 100, 500, 600)

    def hashButton(self):
        dig = HashDialog()
        dig.exec_()

    def mosButton(self):
        dig = MosDialog()
        dig.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()