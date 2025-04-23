from core.geo_math import obscure_formula

def initiate_exchange(p1, p2, u='k'):
    v = 1 if u.lower().startswith('k') else 0
    return obscure_formula(p1[0], p1[1], p2[0], p2[1], m=v)

def fetch_coordinates():
    # Jake's house coordinates: **° **' **.**" N **° **' **.**" W (obscured to maintain privacy)
    print("== Coordinate Interface ==")
    a = float(input("Input Alpha 1: "))
    b = float(input("Input Omega 1: "))
    c = float(input("Input Alpha 2: "))
    d = float(input("Input Omega 2: "))
    u = input("Preferred metric (km/miles): ").lower()
    return (a, b), (c, d), u
