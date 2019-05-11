from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QApplication, QPushButton
from PyQt5.QtCore import pyqtSignal

from Client.tabView.globalLayoutFun import SET_UI_POLICY
from Client.tabView.shipinQss import shipinQss
from Client.tabView.xiazaiQss import xiazaiQss
from Client.tabView.tupianQss import tupianQss
from Client.tabView.meinvQss import meinvQss
from Client.tabView.xiaoshuoQss import xiaoshuoQss
from Client.tabView.youshengQss import youshengQss
from Client.tabView.qqtuQss import qqtuQss

class mainWidget(QWidget):
    signal_shipin = pyqtSignal()
    signal_xiazai = pyqtSignal()
    signal_tupian = pyqtSignal()
    signal_meinv = pyqtSignal()
    signal_xiaoshuo = pyqtSignal()
    signal_yousheng = pyqtSignal()
    signal_qqtu = pyqtSignal()

    def __init__(self, parent=None):
        super(mainWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.toolbar = QWidget()
        self.main_win = QWidget()

        SET_UI_POLICY(self.toolbar)
        SET_UI_POLICY(self.main_win)

        self.__main_v_layout = QVBoxLayout(self)
        self.__main_v_layout.addWidget(self.toolbar)
        self.__main_v_layout.addWidget(self.main_win)
        self.__main_v_layout.setStretch(1, 10)

        self.__toolbar_h_layout(self.toolbar)
        self.__main_win_v_layout(self.main_win)


    def slot_signal_connect(self):
        self.signal_shipin.connect()
        self.signal_xiazai.connect()
        self.signal_tupian.connect()
        self.signal_meinv.connect()
        self.signal_xiaoshuo.connect()
        self.signal_yousheng.connect()
        self.signal_qqtu.connect()


    def __toolbar_h_layout(self, parent):
        self.__h_layout = QHBoxLayout(parent)

        self.btn_shipin = QPushButton(u'在线电影')
        self.btn_xiazai = QPushButton(u'手机下载')
        self.btn_tupian = QPushButton(u'激情图区')
        self.btn_meinv = QPushButton(u'撸撸图区')
        self.btn_xiaoshuo = QPushButton(u'情色小说')
        self.btn_yousheng = QPushButton(u'有声小说')
        self.btn_qqtu = QPushButton('QQ动态图')

        SET_UI_POLICY(self.btn_shipin)
        SET_UI_POLICY(self.btn_xiazai)
        SET_UI_POLICY(self.btn_tupian)
        SET_UI_POLICY(self.btn_meinv)
        SET_UI_POLICY(self.btn_xiaoshuo)
        SET_UI_POLICY(self.btn_yousheng)
        SET_UI_POLICY(self.btn_qqtu)

        self.__h_layout.addWidget(self.btn_shipin)
        self.__h_layout.addWidget(self.btn_xiazai)
        self.__h_layout.addWidget(self.btn_tupian)
        self.__h_layout.addWidget(self.btn_meinv)
        self.__h_layout.addWidget(self.btn_xiaoshuo)
        self.__h_layout.addWidget(self.btn_yousheng)
        self.__h_layout.addWidget(self.btn_qqtu)


    def __main_win_v_layout(self, parent):
        self.__v_layout = QVBoxLayout(parent)

        parent.resize(500,1000)

        self.mShipin = shipinQss()
        self.mXiazai = xiazaiQss()
        self.mTupian = tupianQss()
        self.mMeinv = meinvQss()
        self.mQqtu = qqtuQss()
        self.mXiaoshuo = xiaoshuoQss()
        self.mYousheng = youshengQss()










if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainQss = mainWidget()
    mainQss.show()
    app.exec_()