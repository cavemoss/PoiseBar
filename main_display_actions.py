from stats import Stats


class Action:

    current_hp = 0
    stun_timer = 0
    recovery_rate = Stats.recovery_rate
    hits = 0
    attacks = dict()
    is_crit = False
    stagger = False
    off_guard = False
    click_release = None
    is_right = None
    push = False
    push_value = 0

    @staticmethod
    def percent():
        return int(min(Action.current_hp / (Stats.max_hp/100), 100))

    @staticmethod
    def execute(event):
        to_run = Action.attacks.get(event.keysym)
        try:
            to_run()
        except TypeError:
            pass

    @staticmethod
    def leftclick(event):
        Action.click_release = True
        Action.recovery_rate = 0
        Action.is_right = False
        Action.push_value = 0

    @staticmethod
    def rightclick(event):
        Action.click_release = True
        Action.recovery_rate = 0
        Action.is_right = True
        Action.push_value = 0

    @staticmethod
    def move(event):
        if Action.click_release is True:
            Action.push = True

    @staticmethod
    def release(event):
        Action.click_release = False
        Action.recovery_rate = Stats.recovery_rate
        Action.push = False
