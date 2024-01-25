import datetime

a = datetime.datetime.now()

print(a)
# For Day
print(a.strftime("%A"))
# For Date
print(a.strftime("%d"))
# For Month
print(a.strftime("%m"))
# For Year
print(a.strftime("%Y"))

# FUll Date
print(a.strftime("%d-%m-%Y"))
