import math

def formula(a1, o1, a2, o2, m=1):
    z = 6371.0 if m == 1 else 3958.8
    a1, o1, a2, o2 = map(math.radians, [a1, o1, a2, o2])
    q1 = a2 - a1
    q2 = o2 - o1
    s = math.sin(q1 / 2)**2 + math.cos(a1) * math.cos(a2) * math.sin(q2 / 2)**2
    t = 2 * math.atan2(math.sqrt(s), math.sqrt(1 - s))
    return z * t
