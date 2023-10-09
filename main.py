from stats import Stats
# set enemy stats here
Stats.set_max_hp()  # default of 1000 hp
Stats.set_rec_rate()  # default of 200 hp/sec


import threading
from main_threads import Recovery, Pressure, Stun, AnimationArrows, AnimationFlash
from main_display import Window, StatsWindow
threading.Thread(target=Recovery.start).start()
threading.Thread(target=Pressure.start).start()
threading.Thread(target=Stun.start).start()
threading.Thread(target=AnimationArrows.start).start()
threading.Thread(target=AnimationFlash.start).start()


from main_threads import Attack
# add custom attacks here
critical_atk = Attack()  # default critical attack
standard_atk = Attack(atk=100, dmg=1.06, stun=0.6, trig='space')
poised_through = Attack(atk=40, trig='2')
heavy_blow = Attack(atk=140, dmg=1.12, stun=1.2, trig='1')


Window.refresh()
StatsWindow.refresh()
Window.root.mainloop()
