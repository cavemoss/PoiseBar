from stats import Stats


class Action:

    current_hp = 0
    stun_timer = 0
    recovery_rate = Stats.recovery_rate
    hits = 0
    attacks = dict()
    is_crit = False
    stagger = False

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
