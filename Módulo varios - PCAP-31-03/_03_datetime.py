from datetime import date, time, datetime

d = date(2023, 1, 14)
print(d.strftime('%d/%m/%Y')) # 14/01/2023

t = time(3, 51)
print(t.strftime("%H:%M:%S")) # 03:51:00

dt = datetime(2023, 3, 22, 20, 51)
print(dt.strftime("%d/%m/%Y %H:%M:%S")) # 22/03/2023 20:51:00