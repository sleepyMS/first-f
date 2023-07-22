def strTime(result):
    return str(result // 60).rjust(2,'0') + ':' + str(result % 60).rjust(2,'0')

def solution(n, t, m, timetable):
    time_m = [int(min[:2]) * 60 + int(min[3:]) for min in timetable]
    time_m.sort()
    f_time = 540
    last_crew = 1
    for i in range(n):
        bus_time = i * t
        current_time = f_time + bus_time
        count = 0
        for time in time_m:
            if count >= m:
                break
            if time <= current_time:
                count += 1
                last_crew = time
            else:
                break
        time_m = time_m[count:]
    else:
        if count < m:
            return strTime(current_time)
    
    return strTime(last_crew - 1)