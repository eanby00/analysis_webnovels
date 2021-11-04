import datetime

start = "2021.07.07 21:00"
last = "2021.11.04 21:00"

start_1 = start.split(" ")[0]
print(start_1)
start_2 = start_1.split(".")
start_3 = list(map(int, start_2))
print(start_3)
print(datetime.datetime(start_3[0], start_3[1], start_3[2]))