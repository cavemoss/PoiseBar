import time

from main_display_actions import Action
from main_display_assets import Asset

from stats import Stats
REFRESH_RATE = 0.01
FRAME_RATE = 0.04


class Recovery:

    @staticmethod
    def start():

        while True:
            if Action.current_hp > 0:
                if Action.stagger is True:
                    break
                elif Action.stun_timer == 0:
                    Action.current_hp = max(Action.current_hp - Action.recovery_rate / (1/REFRESH_RATE), 0)
                    time.sleep(REFRESH_RATE)
                else:
                    time.sleep(REFRESH_RATE)
            else:
                time.sleep(REFRESH_RATE)


class Push:

    @staticmethod
    def start():

        while True:
            if Action.push is True:
                def power():
                    if Action.is_right is True:
                        return (Stats.max_hp * 0.1) * 2
                    else:
                        return Stats.max_hp * 0.1

                if Action.push_value < power():
                    Action.current_hp = min(Action.current_hp + power()/20, Stats.max_hp)
                    Action.push_value += power()/20
                    time.sleep(REFRESH_RATE)
                else:
                    time.sleep(REFRESH_RATE)
            else:
                time.sleep(REFRESH_RATE)


class OffGuard:

    @staticmethod
    def start():

        while True:
            if Action.stagger is True:
                Action.off_guard = None
                break
            elif Action.push is True:
                if Action.current_hp == Stats.max_hp:
                    Action.off_guard = True
                    time.sleep(2.5)
                    Action.off_guard = False
                else:
                    time.sleep(REFRESH_RATE)
            else:
                time.sleep(REFRESH_RATE)


class Stun:

    @staticmethod
    def start():

        while True:
            Action.stun_timer = max(Action.stun_timer - 1*REFRESH_RATE, 0)
            time.sleep(REFRESH_RATE)


class AnimationArrows:

    @staticmethod
    def start():

        while True:
            if Action.stagger is True:
                for index in range(1, 16):
                    Asset.arrows_index = index
                    time.sleep(FRAME_RATE)
                break
            else:
                time.sleep(FRAME_RATE)


class AnimationFlash:

    @staticmethod
    def start():

        while True:
            if Asset.flash_index > 0:
                Asset.flash_index = min(Asset.flash_index + 1, 20)
                time.sleep(FRAME_RATE)
            else:
                time.sleep(FRAME_RATE)


class Attack:

    def __init__(self, atk=None, dmg=1, stun=0, trig='c'):
        self.damage = atk
        self.hurt = dmg
        self.stun_duration = stun
        self.binding = trig

    def add(self):
        if self.damage is None:
            self.damage = Stats.max_hp
        Action.attacks.update({self.binding: self.strike})

    def strike(self):
        if Action.stagger is False:
            if self.binding == 'c':
                Action.is_crit = True
            Action.hits += 1
            Action.current_hp = Action.current_hp + self.damage * (self.hurt ** Action.hits)
            Action.stun_timer = min(Action.stun_timer + self.stun_duration, self.stun_duration)
            Asset.flash_index = 1

        if Action.current_hp >= Stats.max_hp:
            Action.stagger = True
            Action.off_guard = None
