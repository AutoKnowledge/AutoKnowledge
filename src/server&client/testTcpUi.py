from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QCoreApplication
import sys


class ToolsUi(QDialog):
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    signal_ui_change = QtCore.pyqtSignal()
    signal_write_msg = QtCore.pyqtSignal(str)
    signal_write_question = QtCore.pyqtSignal(list)
    signal_question_end = QtCore.pyqtSignal(list)
    signal_profession_error = QtCore.pyqtSignal()
    signal_connect_error = QtCore.pyqtSignal()

    def __init__(self, num):

        super(ToolsUi, self).__init__()
        self.num = num
        self._translate = QtCore.QCoreApplication.translate

        self.setObjectName("TCP-UDP")
        self.resize(640, 480)
        self.setAcceptDrops(False)
        self.setSizeGripEnabled(False)

        # 初始界面
        # 初始界面控件

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('kg')

        # 初始界面
        self.pushButton1_1 = QtWidgets.QPushButton('submit')
        self.pushButton1_2 = QtWidgets.QPushButton('delete')
        self.label1_1 = QtWidgets.QLabel('你的职业是什么？')
        self.lineEdit1_1 = QtWidgets.QLineEdit()
        #self.label2_1 = QtWidgets.QLabel()
        self.label3_1 = QtWidgets.QLabel()
        # 确认答题界面
        self.pushButton2_1 = QtWidgets.QPushButton('yes')
        self.pushButton2_2 = QtWidgets.QPushButton('exit')

        # 答题界面

        self.label3_1 = QtWidgets.QLabel('问题:')

        self.cb_A = QtWidgets.QCheckBox('A:')
        self.cb_B = QtWidgets.QCheckBox('B:')
        self.cb_C = QtWidgets.QCheckBox('C:')
        self.cb_D = QtWidgets.QCheckBox('D:')

        self.pushButton3_1 = QtWidgets.QPushButton('answer')
        self.pushButton3_2 = QtWidgets.QPushButton('skip')

        # 答题完毕
        self.pushButton4_1 = QtWidgets.QPushButton('exit')

        # 设置控件初始属性

        # self.label2_1.hide()
        self.pushButton2_1.hide()
        self.pushButton2_2.hide()

        self.cb_A.hide()
        self.cb_B.hide()
        self.cb_C.hide()
        self.cb_D.hide()
        self.label3_1.hide()
        self.pushButton3_1.hide()
        self.pushButton3_2.hide()

        self.pushButton4_1.hide()

        # self.lineEdit3_1.hide()

        # 初始界面布局
        self.h_box1_1 = QHBoxLayout()
        self.v_box1 = QVBoxLayout()

        self.layout_ui()
        self.connect()

    def layout_ui(self):

        self.h_box1_1.addWidget(self.pushButton1_1)
        self.h_box1_1.addWidget(self.pushButton1_2)
        self.h_box1_1.addWidget(self.pushButton2_1)
        self.h_box1_1.addWidget(self.pushButton2_2)
        self.h_box1_1.addWidget(self.pushButton3_1)
        self.h_box1_1.addWidget(self.pushButton3_2)
        self.h_box1_1.addWidget(self.pushButton4_1)

        self.v_box1.addWidget(self.label3_1)
        self.v_box1.addWidget(self.label1_1)
        # self.v_box1.addWidget(self.label2_1)

        self.v_box1.addWidget(self.cb_A)
        self.v_box1.addWidget(self.cb_B)
        self.v_box1.addWidget(self.cb_C)
        self.v_box1.addWidget(self.cb_D)

        self.v_box1.addWidget(self.lineEdit1_1)
        # self.v_box1.addWidget(self.lineEdit3_1)
        self.v_box1.addLayout(self.h_box1_1)

        self.setLayout(self.v_box1)

    def connect(self):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        self.signal_ui_change.connect(self.ui_change_1)
        self.signal_write_msg.connect(self.write_msg)
        self.signal_write_question.connect(self.write_question)
        self.signal_question_end.connect(self.question_end)
        self.signal_profession_error.connect(self.profession_error)
        self.signal_connect_error.connect(self.connect_error)

        # self.comboBox_tcp.currentIndexChanged.connect(self.combobox_change)
        self.pushButton1_1.clicked.connect(self.ui_change)
        self.pushButton1_2.clicked.connect(self.ui_change)

        self.pushButton2_1.clicked.connect(self.ui_change)
        self.pushButton2_2.clicked.connect(self.exit_exit)

        # self.pushButton3_1.clicked.connect(self.reset_cb)
        # self.pushButton3_2.clicked.connect(self.write_msg)

        self.pushButton4_1.clicked.connect(self.exit_exit)

    def ui_change_1(self):
        self.lineEdit1_1.hide()
        self.pushButton1_1.hide()
        self.pushButton1_2.hide()

        self.pushButton2_1.show()
        self.pushButton2_2.show()

        self.pushButton3_1.hide()
        self.pushButton3_2.hide()

    def ui_change(self):

        sender = self.sender()
        if sender.text() == 'submit_no':
            # self.label1_1.setText('hi')

            # self.label1_1.hide()
            # self.label2_1.show()

            self.lineEdit1_1.hide()
            self.pushButton1_1.hide()
            self.pushButton1_2.hide()

            self.pushButton2_1.show()
            self.pushButton2_2.show()

            self.pushButton3_1.hide()
            self.pushButton3_2.hide()

        elif sender.text() == 'delete':
            self.lineEdit1_1.clear()

        elif sender.text() == 'yes':

            # self.label2_1.hide()
            # self.label3_1.show()

            self.pushButton1_1.hide()
            self.pushButton1_2.hide()

            self.pushButton2_1.hide()
            self.pushButton2_2.hide()

            self.pushButton3_1.show()
            self.pushButton3_2.show()

            self.cb_A.show()
            self.cb_B.show()
            self.cb_C.show()
            self.cb_D.show()

    def write_msg(self, msg):

        self.label1_1.setText(msg)
        # 滚动条移动到结尾
        # self.textBrowser_recv.moveCursor(QtGui.QTextCursor.End)

    def write_question(self, question):
        #print(" ".join(question[2][0]))

        self.label1_1.setText(question[2][0])
        self.cb_A.setText(str(question[2][1][0]))
        self.cb_B.setText(str(question[2][1][1]))
        self.cb_C.setText(str(question[2][1][2]))
        self.cb_D.setText(str(question[2][1][3]))

    def question_end(self, msg):

        self.cb_A.hide()
        self.cb_B.hide()
        self.cb_C.hide()
        self.cb_D.hide()
        self.label3_1.hide()
        self.pushButton3_1.hide()
        self.pushButton3_2.hide()
        self.pushButton4_1.show()

        self.label1_1.setText(str(msg[1]))

    def connect_error(self):

        self.box = QMessageBox.warning(self, "error", "连接服务器失败,程序即将退出！")

    def profession_error(self):

        self.box = QMessageBox.warning(self, "error", "无法找到匹配的职业，请重新输入！")

    def exit_exit(self):
        self.tcp_socket.close()
        self.close()

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        self.tcp_socket.close()
        self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = ToolsUi(1)
    ui.show()
    sys.exit(app.exec_())
