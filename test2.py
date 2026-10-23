import math
import matrix as mt
angle = [
    0,
    mt.pi/6,
    mt.pi/4,
    mt.pi/3,
    mt.pi/2,
    mt.pi,
    10 * mt.pi,
    1000* mt.pi
]
for i in angle:
    print(
        f"x=:{i},"
        f"sin error:={abs(mt.rsin(i)-math.sin(i)):.3e},"
        f"cos error:={abs(mt.rcos(i)-math.cos(i)):.3e}"
    )