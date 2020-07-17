
from PyQt5 import QtWidgets
import testTcpUi
import socket
import threading
import json
import sys
#import stopThreading


class TcpLogic(testTcpUi.ToolsUi):
    def __init__(self, num):
        super(TcpLogic, self).__init__(num)
        self.tcp_socket = None
        self.sever_th = None
        self.client_th = None
        self.client_socket_list = list()

        self.link = False  # 用于标记是否开启了连接

    def tcp_client_start(self):
        """
        功能函数，TCP客户端连接其他服务端的方法
        :return:
        """
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        address = ('127.0.0.1', 9999)

        try:
            self.tcp_socket.connect(address)

        except Exception:
            self.signal_connect_error.emit()
            return -1

        else:
            self.client_th = threading.Thread(
                target=self.tcp_client_concurrency, args=(address,))
            self.client_th.start()

    def tcp_client_concurrency(self, address):

        while True:
            recv_msg = self.tcp_socket.recv(1024)

            if recv_msg:

                msg = json.loads(recv_msg.decode('utf-8'))

                if msg[0] == 'question':
                    print('msg==question')

                    self.signal_write_question.emit(msg)

                elif msg[0] == 'pass' or msg[0] == 'fail':
                    print('msg==pass or fail')
                    self.signal_question_end.emit(msg)
                elif msg[0] == 'profession error':
                    print('msg==profession error')
                    self.signal_profession_error.emit()
                elif msg[0] == 'profession ok':
                    print('msg==profession ok')
                    self.signal_ui_change.emit()
                elif msg[0] == 'confirm':
                    print('msg==confirm')
                    self.signal_write_msg.emit(str(msg[1]))
            else:
                self.tcp_socket.close()
                break

    def tcp_send(self, msg):

        print(msg)
        self.tcp_socket.send(msg.encode('utf-8'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = TcpLogic(1)
    ui.show()
    sys.exit(app.exec_())
