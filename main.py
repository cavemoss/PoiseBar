import threading

from main_threads import Recovery, Pressure, Stun, AnimationArrows, AnimationFlash
from main_display import Window, StatsWindow

from stats import Stats
from main_threads import Attack

threading.Thread(target=Recovery.start).start()
threading.Thread(target=Pressure.start).start()
threading.Thread(target=Stun.start).start()
threading.Thread(target=AnimationArrows.start).start()
threading.Thread(target=AnimationFlash.start).start()


# set enemy stats here
Stats.set_max_hp()  # default of 1000 hp
Stats.set_rec_rate()  # default of 200 hp/sec

Attack().add()  # default critical attack
Attack(tag='standard_atk', atk=100, dmg=1.06, stun=0.6, trig='space').add()
Attack(tag='poised_through', atk=100, dmg=1.04, stun=0, trig='space').add()
Attack(tag='heavy_blow', atk=140, dmg=1.12, stun=1.2, trig='space').add()


Window.refresh()
StatsWindow.refresh()
Window.root.mainloop()
