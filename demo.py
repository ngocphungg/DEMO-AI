
# import cv2
# import pytesseract
# import numpy as np
# import os
# from PIL import Image
# import pyocr
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # Đọc ảnh biển số xe
# img = cv2.imread('biensoxe.jpg')

# # Chuyển đổi ảnh sang độ xám
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Áp dụng bộ lọc Gauss để giảm nhiễu
# gray = cv2.GaussianBlur(gray, (7, 7), 0)

# # Áp dụng phép toán đóng để loại bỏ các lỗ hổng và giảm độ nổi bật của các đặc trưng không mong muốn
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# closed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# # Tính toán các cạnh của ảnh
# edged = cv2.Canny(closed, 50, 150)

# # Tìm kiếm các contour có thể là biển số xe
# contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Sắp xếp các contour theo thứ tự từ trái sang phải
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# # Tìm kiếm biển số xe
# for contour in contours:
#     # Xác định hình dạng của contour
#     peri = cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

#     # Nếu contour có 4 đỉnh, có thể là biển số xe
#     if len(approx) == 4:
#         # Tạo một maske để cắt ảnh biển số xe
#         mask = np.zeros(gray.shape, np.uint8)
#         cv2.drawContours(mask, [approx], -1, 255, -1)
#         mask = cv2.bitwise_and(gray, gray, mask=mask)

#         # Xử lý ảnh để tăng cường chữ số trên biển số xe
#         thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#         thresh = cv2.erode(thresh, None, iterations=2)
#         thresh = cv2.dilate(thresh, None, iterations=2)

#         # Nhận dạng biển số xe bằng PyTesseract
#         text = pytesseract.image_to_string(thresh, config='--psm 11')
#         print('Biển số xe: ', text)

# name = input("heloo");
# print("hlee " +name + "!") 

# import cv2
# import pytesseract
# import os
# from PIL import Image
# import pyocr

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # Đọc ảnh từ file
# img = cv2.imread('biensoxe.jpg')

# # Chuyển đổi ảnh sang định dạng xám
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Áp dụng bộ lọc Gaussian để làm mờ ảnh
# gray = cv2.GaussianBlur(gray, (5, 5), 0)

# # Sử dụng pytesseract để quét số trong ảnh
# text = pytesseract.image_to_string(gray, lang='eng', config='--psm 11')

# # Hiển thị kết quả
# print('Biển số xe: ',text)


# import cv2
# import pytesseract
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QFileDialog

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Thiết lập kích thước cửa sổ và tiêu đề
#         self.setGeometry(100, 100, 800, 600)
#         self.setWindowTitle("Phần mềm nhận diện biển số xe")

#         # Tạo một nút để chọn ảnh
#         self.select_image_button = QPushButton("Chọn ảnh", self)
#         self.select_image_button.setGeometry(10, 10, 100, 30)
#         self.select_image_button.clicked.connect(self.select_image)

#         # Tạo một đối tượng QLabel để hiển thị ảnh
#         self.image_label = QLabel(self)
#         self.image_label.setGeometry(10, 50, 400, 400)

#         # Tạo một đối tượng QLabel để hiển thị kết quả quét
#         self.result_label = QLabel(self)
#         self.result_label.setGeometry(420, 50, 370, 400)

#     def select_image(self):
#         # Hiển thị hộp thoại chọn tệp ảnh
#         file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

#         # Nếu người dùng đã chọn một tệp ảnh
#         if file_path:
#             # Hiển thị ảnh trên đối tượng QLabel
#             pixmap = QPixmap(file_path)
#             self.image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))

#             # Đọc ảnh từ file
#             img = cv2.imread(file_path)

#             # Chuyển đổi ảnh sang định dạng xám
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#             # Áp dụng bộ lọc Gaussian để làm mờ ảnh
#             gray = cv2.GaussianBlur(gray, (5, 5), 0)

#             # Sử dụng pytesseract để quét số trong ảnh
#             text = pytesseract.image_to_string(gray, lang='eng', config='--psm 11')

#             # Hiển thị kết quả quét trên đối tượng QLabel
#             self.result_label.setText(text)


# if __name__ == '__main__':
#     app = QApplication()
#     window = MainWindow()
#     window.show()
#     app.exec_()


import sys
import cv2
import pytesseract
import os
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QPushButton,QLineEdit,QGridLayout,QWidget,QVBoxLayout
from PyQt5.QtGui import QPixmap,QImage,QFont
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Thiết lập kích thước cửa sổ và tiêu đề
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Phần mềm nhận diện biển số xe")

        # Tạo một nút để chọn ảnh
        self.select_image_button = QPushButton("Chọn ảnh", self)
        self.select_image_button.setGeometry(50, 50, 100, 30)
        self.select_image_button.clicked.connect(self.select_image)

        # Tạo hai đối tượng QLabel để hiển thị ảnh và kết quả quét
        self.image_label = QLabel(self)
        self.result_label = QLabel(self)
        self.result_text = QLabel(self)

        # Tạo một đối tượng QVBoxLayout để chứa nút chọn ảnh và hai QLabel
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.select_image_button)
        self.vertical_layout.addWidget(self.image_label)
        self.vertical_layout.addWidget(self.result_label)

        # Khởi tạo đối tượng QGridLayout và thiết lập vị trí của các đối tượng
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.result_label, 0, 0)
        self.grid_layout.addWidget(self.result_text, 1, 0)

        # Thêm QGridLayout vào QVBoxLayout
        self.vertical_layout.addLayout(self.grid_layout)

        # Khởi tạo đối tượng QWidget để chứa QVBoxLayout và thiết lập nó làm widget trung tâm
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.central_widget)

    def select_image(self):
        # Mở hộp thoại chọn tệp
        filename, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image files (*.jpg *.png *.bmp)")

        if filename:
            # Đọc ảnh từ tệp và hiển thị trên QLabel
            image = cv2.imread(filename)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pixmap = QPixmap.fromImage(QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888))
            self.image_label.setPixmap(pixmap)

            # Nhận diện và hiển thị kết quả quét trên QLabel
            result = pytesseract.image_to_string(image, lang="eng", config="--psm 11")
            self.result_label.setFont(QFont("Arial", 10))
            self.result_label.setText(result)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QTextEdit, QMessageBox,QFileDialog
# from PyQt5.QtGui import QPixmap, QFont,QImage
# from PyQt5.QtCore import Qt
# import cv2
# import pytesseract
# import numpy as np
# import os
# from PIL import Image


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.image_frame = QLabel(self)
#         self.image_frame.setGeometry(20, 70, 400, 400)
#         # Tạo các label và button cho giao diện
#         self.label = QLabel(self)
#         self.label.setGeometry(20, 20, 200, 30)
#         self.label.setText('Đường dẫn ảnh:')
#         self.label.setFont(QFont('Arial', 12))
        
#         self.line_edit = QLineEdit(self)
#         self.line_edit.setGeometry(140, 20, 400, 30)
        
#         self.button = QPushButton(self)
#         self.button.setGeometry(550, 20, 100, 30)
#         self.button.setText('Chọn ảnh')
#         self.button.clicked.connect(self.select_image)

#         self.result_text = QTextEdit(self)
#         self.result_text.setGeometry(370, 70, 330, 150)
#         self.result_text.setFont(QFont('Arial', 12))

#         self.recognize_button = QPushButton(self)
#         self.recognize_button.setGeometry(270, 340, 100, 30)
#         self.recognize_button.setText('Nhận dạng')
#         self.recognize_button.clicked.connect(self.recognize)

#         # Thiết lập kích thước và tiêu đề cho cửa sổ chính
#         self.setGeometry(100, 100, 670, 400)
#         self.setWindowTitle('Nhận dạng biển số xe')

#     def select_image(self):
#         # Gọi hộp thoại để chọn ảnh và hiển thị đường dẫn của ảnh lên line edit
#         filename, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.jpg *.png)")
#         if filename:
#             self.line_edit.setText(filename)

#             # Hiển thị ảnh lên label
#             image = cv2.imread(filename)
#             image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             pixmap = QPixmap.fromImage(QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888))
#             self.image_frame.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
          
#     def recognize(self):
#         # Lấy đường dẫn ảnh từ line edit
#         filename = self.line_edit.text()

#         # Kiểm tra xem đường dẫn ảnh có hợp lệ hay không
#         if not os.path.isfile(filename):
#             QMessageBox.warning(self, 'Lỗi', 'Đường dẫn ảnh không hợp lệ!')
#             return

#         # Đọc ảnh biển số xe
#         img = cv2.imread(filename)

#         # Chuyển đổi ảnh sang độ xám
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # Áp dụng bộ lọc Gauss để giảm nhiễu
#         gray = cv2.GaussianBlur(gray, (7, 7), 0)

#         # Áp dụng phép toán đóng để loại bỏ các lỗ hổng và giảm độ nổi bật của các đặc trưng không mong muốn
#         kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#         closed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

#         # Tính toán các cạnh của ảnh
#         edged = cv2.Canny(closed, 50, 150)

#         # Tìm kiếm các contour có thể là biển số xe
#         contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         # Sắp xếp các contour theo thứ tự từ trái sang phải
#         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:20]

#         # Tìm kiếm biển số xe
#         for contour in contours:
#             # Xác định hình dạng của contour
#             peri = cv2.arcLength(contour, True)
#             approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

#             # Nếu contour có 4 đỉnh, có thể là biển số xe
#             if len(approx) == 4:
#                 # Tạo một maske để cắt ảnh biển số xe
#                 mask = np.zeros(gray.shape[:2], dtype=np.uint8)
#                 cv2.drawContours(mask, [approx], -1, 255, -1)
#                 license_plate = cv2.bitwise_and(gray, gray, mask=mask)

#                 # Xử lý ảnh để tăng cường chữ số trên biển số xe
#                 thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#                 # thresh = cv2.erode(thresh, None, iterations=2)
#                 # thresh = cv2.dilate(thresh, None, iterations=2)
#                 # Nhận dạng biển số xe bằng PyTesseract
#                 text = pytesseract.image_to_string(gray, lang='eng', config='--psm 11')
#                 self.result_text.setText('Biển số xe: ' + text)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())