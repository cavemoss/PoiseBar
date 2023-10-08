

class Stats:

    max_hp = None
    recovery_rate = None

    @classmethod
    def set_max_hp(cls, value=1000):
        cls.max_hp = value
        cls.recovery_rate = value * 0.2

    @classmethod
    def set_rec_rate(cls, value=None):
        if value is not None:
            cls.recovery_rate = value
