# put your python code here
MAX_AMPERAGE = 100


def print_readings(readings):
    for reading in readings:
        print(reading)


def blow_fuse():
    global fuse_blown
    fuse_blown = True
    return


def ammeter(current):
    if current > MAX_AMPERAGE:
        blow_fuse()


fuse_blown = False
current_measurements = []

while not fuse_blown:
    amperage_reading = int(input())
    ammeter(amperage_reading)
    if amperage_reading >= 10 and not fuse_blown:
        current_measurements.append(amperage_reading)

print_readings(current_measurements)
