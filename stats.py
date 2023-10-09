class Stats:

    max_hp = None
    recovery_rate = None

    @classmethod
    def set_max_hp(cls, value=1000):
        cls.max_hp = value
        cls.recovery_rate = int(value * 0.2)
        print('max_hp =' + str(cls.max_hp))

    @classmethod
    def set_rec_rate(cls, value=None):
        if value is not None:
            cls.recovery_rate = value
        print('max_hp =' + str(cls.recovery_rate))
