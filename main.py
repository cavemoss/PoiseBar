import threading

from main_threads import Recovery, Push, OffGuard, Stun, AnimationArrows, AnimationFlash
from main_display import Window, StatsWindow

from stats import Stats
from main_threads import Attack

threading.Thread(target=Recovery.start).start()
threading.Thread(target=Push.start).start()
threading.Thread(target=OffGuard.start).start()
threading.Thread(target=Stun.start).start()
threading.Thread(target=AnimationArrows.start).start()
threading.Thread(target=AnimationFlash.start).start()

# set enemy stats here
Stats.set_max_hp()  # default of 1000 hp
Stats.set_max_hp()  # default of 200 hp/sec

# default critical attack
critical_attack = Attack()
critical_attack.add()

# add custom attacks here
standard_atk = Attack(atk=100, dmg=1.06, stun=0.6, trig='space')
standard_atk.add()

Window.refresh()
StatsWindow.refresh()
Window.root.mainloop()
