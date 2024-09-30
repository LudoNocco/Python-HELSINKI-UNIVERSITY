def get_station_data(filename: str) -> dict:
    stations = {}
    with open(filename, 'r') as file:
        next(file) 
        for line in file:
            parts = line.strip().split(';')
            name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])
            stations[name] = (longitude, latitude)
    return stations

import math

def distance(stations: dict, station1: str, station2: str) -> float:
    lon1, lat1 = stations[station1]
    lon2, lat2 = stations[station2]
    
    x_km = (lon1 - lon2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict) -> tuple:
    max_distance = 0
    station_pair = ("", "")
    
    station_names = list(stations.keys())
    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            station1 = station_names[i]
            station2 = station_names[j]
            dist = distance(stations, station1, station2)
            if dist > max_distance:
                max_distance = dist
                station_pair = (station1, station2)
    
    return station_pair[0], station_pair[1], max_distance
