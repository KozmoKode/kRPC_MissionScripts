"""
- KebalX (stock) to orbit script -
* Prelaunch checks
* Launch
* Ascent
* Gravity turn
* Orbital circularization
* Orbit
"""
import krpc
import math
import time

conn = krpc.connect(name='Main')
KSC = conn.space_center
vessel = KSC.active_vessel
print("")
print(f"{vessel.name} is online!")
