from tkinter import *
added_files = [('Animation/arrows/*png', 'Animation/arrows'),
               ('Animation/bar/*png', 'Animation/bar'),
               ('Animation/flash/*png', 'Animation/flash'),
               ('Animation/flash red/*png', 'Animation/flash red'),
               ('Animation/*.png', 'Animation')]


class Asset:

    arrows_index = 0
    flash_index = 0

    @staticmethod
    def index_format(index):
        long = len(str(index))
        return '0' * (4 - long) + str(index)

    def __init__(self):

        self.none_img = PhotoImage(file='Animation\\none.png')

        self.shadow = PhotoImage(file='Animation\\shadow.png')

        self.sprites_bar = []
        for index in range(0, 100 + 1):
            self.sprites_bar.append(PhotoImage(file='Animation\\bar\\bar{}.png'.
                                               format(Asset.index_format(index))))

        self.sprites_arrows = []
        for index in range(100, 115 + 1):
            self.sprites_arrows.append(PhotoImage(file='Animation\\arrows\\arrows{}.png'.
                                                  format(Asset.index_format(index))))

        self.sprites_flash_regular = []
        for index in range(80, 100 + 1):
            self.sprites_flash_regular.append(PhotoImage(file='Animation\\flash\\flash{}.png'.
                                                         format(Asset.index_format(index))))

        self.sprites_flash_critical = []
        for index in range(80, 100 + 1):
            self.sprites_flash_critical.append(PhotoImage(file='Animation\\flash red\\flash{}.png'.
                                                          format(Asset.index_format(index))))
