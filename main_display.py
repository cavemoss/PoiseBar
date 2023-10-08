import time
import threading
from tkinter import *

from main_display_actions import Action
from main_display_assets import Asset

from stats import Stats
from main_threads import REFRESH_RATE


def destroy():
    while True:
        if Action.stagger is True:
            time.sleep(1)
            StatsWindow.stats.destroy()
            Window.root.destroy()
        else:
            time.sleep(REFRESH_RATE)


threading.Thread(target=destroy).start()


class Window:

    root = Tk()
    root.title('Poise Bar')
    root.config(background='black')
    root.geometry('700x100+420+250')

    assets = Asset()
    canvas = Canvas(root, height=100, width=700, highlightthickness=0, background='black')
    canvas.pack()

    background = canvas.create_image(0, 0, anchor=NW, image=assets.shadow)
    flash = canvas.create_image(0, 0, anchor=NW)
    bar = canvas.create_image(0, 0, anchor=NW)
    arrows = canvas.create_image(0, 0, anchor=NW)

    root.bind('<Key>', Action.execute)
    root.bind('<Motion>', Action.move)
    root.bind('<Button-1>', Action.leftclick)
    root.bind('<Button-3>', Action.rightclick)
    root.bind('<ButtonRelease>', Action.release)

    @classmethod
    def refresh(cls):
        if Action.stagger is False:
            cls.canvas.itemconfig(cls.bar, image=cls.assets.sprites_bar[Action.percent()])

        else:

            cls.canvas.itemconfig(cls.bar, image=cls.assets.none_img)
            cls.canvas.itemconfig(cls.background, image=cls.assets.none_img)

        def sprites_flash():
            if Action.is_crit is False:
                return cls.assets.sprites_flash_regular[Asset.flash_index]
            else:
                return cls.assets.sprites_flash_critical[Asset.flash_index]

        cls.canvas.itemconfig(cls.flash, image=sprites_flash())
        cls.canvas.itemconfig(cls.arrows, image=cls.assets.sprites_arrows[Asset.arrows_index])

        cls.root.after(10, cls.refresh)


class StatsWindow:

    stats = Toplevel()
    stats.title('Enemy Stats')
    stats.config(background='black')
    stats.geometry('335x130+50+250')
    stats.resizable(False, False)

    Label(stats, text='{:>15}'.format('Hit Points:'), font=('Consolas', 15), bg='black', fg='white').grid(row=1, column=1)
    hp_label = Label(stats, font=('Consolas', 15), bg='black', fg='white', width=10, height=1)
    hp_label.grid(row=1, column=2)
    Label(stats, text='hp', font=('Consolas', 15), bg='black', fg='white').grid(row=1, column=3)

    Label(stats, text='{:>15}'.format('Stun Duration:'), font=('Consolas', 15), bg='black', fg='white').grid(row=2, column=1)
    stun_label = Label(stats, font=('Consolas', 15), bg='black', fg='white', width=10, height=1)
    stun_label.grid(row=2, column=2)
    Label(stats, text='sec', font=('Consolas', 15), bg='black', fg='white').grid(row=2, column=3)

    Label(stats, text='{:>15}'.format('Off Guard:'), font=('Consolas', 15), bg='black', fg='white').grid(row=3, column=1)
    off_label = Label(stats, font=('Consolas', 15), bg='black', fg='white', width=10, height=1)
    off_label.grid(row=3, column=2)

    Label(stats, text='{:>15}'.format('Stagger:'), font=('Consolas', 15), bg='black', fg='white').grid(row=4, column=1)
    stagger_label = Label(stats, font=('Consolas', 15), bg='black', fg='white', width=10, height=1)
    stagger_label.grid(row=4, column=2)

    @classmethod
    def refresh(cls):
        cls.hp_label.config(text=str(int(Action.current_hp)) + '/' + str(Stats.max_hp))
        cls.stun_label.config(text='{:.2f}'.format(Action.stun_timer))
        cls.off_label.config(text=str(Action.off_guard))
        cls.stagger_label.config(text=str(Action.stagger))

        Window.root.after(100, cls.refresh)
