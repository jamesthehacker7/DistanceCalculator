import math

def haversine(lat1, lon1, lat2, lon2, unit='km'):
    # Radius of Earth in km or miles
    R_km = 6371.0
    R_miles = 3958.8

    # Convert coordinates from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate distance
    if unit.lower() == 'miles':
        distance = R_miles * c
    else:
        distance = R_km * c

    return distance

def main():
    print("Distance Calculator")
    lat1 = float(input("Enter latitude of first point: "))
    lon1 = float(input("Enter longitude of first point: "))
    lat2 = float(input("Enter latitude of second point: "))
    lon2 = float(input("Enter longitude of second point: "))
    unit = input("Enter unit (km or miles): ")

    distance = haversine(lat1, lon1, lat2, lon2, unit)
    print(f"Distance: {distance:.2f} {unit.lower()}")

if __name__ == "__main__":
    main()
