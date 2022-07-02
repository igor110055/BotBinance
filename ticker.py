intervals = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1d", "1W", "1M"]
switcher = {
    0: 60,
    1: 60,
    2: 60,
    3: 60,
    4: 3600,
    5: 3600,
    6: 3600,
    7: 86400,
    8: 604800,
    9: 2592000
}
for i in intervals:
    t = i[:-1]
    print(switcher[intervals.index(i)]*int(t))
