# coding = utf-8
from app.controller import *
from app.model import Users


class TestController():
    def __init__(self):
        app.global_list.TOTAL_PLAYER = 3
        self.wolf = Users(1, 'wolf')
        self.god = Users(2, 'god', {self.wolf: -5})
        self.human = Users(3, 'human',
                           {self.wolf: 1, self.god: -1},
                           [('support', self.wolf)])

if __name__ == '__main__':
    import sys

    TestController()
    win = QtWidgets.QApplication(sys.argv)
    main_window = ControlMainWindow()
    main_window.show()
    sys.exit(win.exec_())