from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import testTcpLogic
import socket
import sys


class MainWindow(testTcpLogic.TcpLogic):
    def __init__(self, num):
        super(MainWindow, self).__init__(num)
        self.client_socket_list = list()
        self.another = None
        self.link = False

    def connect(self, ):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        # 如需传递参数可以修改为connect(lambda: self.click(参数))
        super(MainWindow, self).connect()
        self.pushButton1_1.clicked.connect(self.click_link_send)
        self.pushButton2_1.clicked.connect(self.click_send)
        self.pushButton3_1.clicked.connect(self.click_send)
        self.pushButton3_2.clicked.connect(self.click_send)

    def click_link_send(self):
        """
        pushbutton_link控件点击触发的槽
        :return: None
        """

        if self.tcp_client_start() == -1:

            print("start no")
            # self.close()
            sys.exit(app.exec_())

        else:
            print("start ok")

        send_msg = (str(self.lineEdit1_1.displayText()))

        self.tcp_send(send_msg)

        print('send ok')
        self.link = True
        # self.pushButton_unlink.setEnabled(True)
        # self.pushButton_link.setEnabled(False)

    def click_send(self):
        """
        pushbutton_link控件点击触发的槽
        :return: None
        """
        sender = self.sender()
        if sender.text() == 'yes':
            send_msg = 'yes'
            self.tcp_send(send_msg)

        elif sender.text() == 'answer':
            send_flag = 0
            send_msg = ''
            if self.cb_A.isChecked():
                send_flag = 1
                send_msg = send_msg + 'A'
            if self.cb_B.isChecked():
                send_flag = 1
                send_msg = send_msg + 'B'
            if self.cb_C.isChecked():
                send_flag = 1
                send_msg = send_msg + 'C'
            if self.cb_D.isChecked():
                send_flag = 1
                send_msg = send_msg + 'D'
            if send_flag == 1:
                self.tcp_send(send_msg)
                self.cb_A.setCheckState(Qt.Unchecked)
                self.cb_B.setCheckState(Qt.Unchecked)
                self.cb_C.setCheckState(Qt.Unchecked)
                self.cb_D.setCheckState(Qt.Unchecked)

        elif sender.text() == 'skip':
            send_msg = 'F'
            self.tcp_send(send_msg)
            self.cb_A.setCheckState(Qt.Unchecked)
            self.cb_B.setCheckState(Qt.Unchecked)
            self.cb_C.setCheckState(Qt.Unchecked)
            self.cb_D.setCheckState(Qt.Unchecked)

        # self.pushButton_unlink.setEnabled(True)
        # self.pushButton_link.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow(1)
    ui.show()
    sys.exit(app.exec_())
