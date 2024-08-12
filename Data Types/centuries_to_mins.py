centuries = int(input("Centurie/s: "))

years = centuries * 100
days = years * 365 + centuries * 24
hours = days * 24
mins = hours * 60

print(f"{centuries} centurie/s = {years} years = {days} days = {hours} hours = {mins} mins")