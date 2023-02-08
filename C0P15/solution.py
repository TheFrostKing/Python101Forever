
def gas_stations(distance, tank_size, stations):
    result = []
    next_gas = 0
    sort_stations = sorted(stations)
    remaining = tank_size
  
    last_gas = sort_stations[len(sort_stations)-1]

    difference = distance - last_gas

    for x in range(len(sort_stations)):

        if sort_stations[x] == sort_stations[0]:
            if remaining > sort_stations[x]:
                remaining -= sort_stations[x]
                next_gas = sort_stations[x+1] - sort_stations[x]

                       
        if sort_stations[x] != sort_stations[0]:
            next_gas = sort_stations[x] - sort_stations[x-1]
            remaining-= next_gas
        
        
            if sort_stations[x] > distance:
                return result
           

        if remaining == 0 or remaining <= next_gas:
            remaining = tank_size
            result.append(sort_stations[x])

        if  last_gas == sort_stations[x]:
            if next_gas > remaining:
                return []
            
       
            
        

    return result
        





tests = [
    ((320, 90, [50, 80, 140, 180, 220, 290]), [80, 140, 220, 290]),
    ((390, 80, [70, 90, 140, 210, 240, 280, 350]), [70, 140, 210, 280, 350]),
    ((100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]), [40, 80]),
    ((100, 101, [200]), []),
    ((100, 50, [200]), []),
    ((100, 50, [10, 90]), []),
    ((70, 50, [10, 24, 30]), [])
]

for args, expected in tests:
    result = gas_stations(*args)

    passing = result == expected

    if passing:
        print(passing)
    else:
        print(passing, result, expected)