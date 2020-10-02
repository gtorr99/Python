import time

# gets current time
t = "03:56:13"   # time.strftime("%X")
a = t[0:2]

if int(a) > 12:
    a = int(a) - 12
    t = str(a) + t[2:] + " PM"
else:
    t += " AM"

print(t)
