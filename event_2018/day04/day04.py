from datetime import datetime
import os
input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_path) as input_list:
    formatted_list = [line.rstrip() for line in input_list]
formatted_list.sort()

guard_sleep_time = {}
guard_minutes_asleep = {}
for line in formatted_list:
    date_string = line.split(' ')[0][1:]
    year, month, day = [int(i) for i in date_string.split('-')]
    time_string = line.split(']')[0].split(' ')[1]
    hour, minute = [int(i) for i in time_string.split(':')]
    row_datetime = datetime(year=year, month=month,
                            day=day, hour=hour, minute=minute)

    action = ' '.join(line.split(' ')[-2:])

    if action == 'begins shift':
        guard = int(line.split('#')[1].split(' ')[0])
        if guard not in guard_sleep_time:
            guard_sleep_time[guard] = 0
            guard_minutes_asleep[guard] = []
    elif action == 'falls asleep':
        asleep_start = row_datetime
        first_asleep_minute = minute
    elif action == 'wakes up':
        sleep_time = int(
            (row_datetime - asleep_start).total_seconds() // 60)
        guard_sleep_time[guard] += sleep_time
        minutes_asleep = range(first_asleep_minute, minute)
        guard_minutes_asleep[guard] += list(minutes_asleep)
else:
    sleepiest_guard = max(guard_sleep_time, key=guard_sleep_time.get)
    sleepiest_minute = max(guard_minutes_asleep[sleepiest_guard],
                           key=guard_minutes_asleep[sleepiest_guard].count)
    print("Part 1:", sleepiest_guard * sleepiest_minute)

guard_sleepiest_minutes = []
guard_minutes_asleep_use = {
    guard_id: guard_minutes for guard_id,
    guard_minutes in guard_minutes_asleep.items() if guard_minutes != []}
for guard_id, guard_minutes in guard_minutes_asleep_use.items():
    sleepiest_minute = max(guard_minutes, key=guard_minutes.count)
    sleepiest_minute_freq = len([
        minute for minute in guard_minutes if minute == sleepiest_minute])
    guard_sleepiest_minutes.append(
        (guard_id * sleepiest_minute, sleepiest_minute_freq))
else:
    print("Part 2:", max(guard_sleepiest_minutes, key=lambda item: item[1])[0])
