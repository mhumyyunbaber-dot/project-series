def miles_to_kilometer(miles):
    return miles * 1.6  

def kilometer_to_meters(km):
    return km * 1000

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_seconds(minutes):
    return minutes * 60


print("Distance Conversion")

miles = int(input("Enter Miles: "))
km = miles_to_kilometer(miles)
print(f"{miles} miles = {km} km")


kilometer=int(input("Enter kilometers: "))
meters = kilometer_to_meters(kilometer)

print(f"{km} km = {meters} meters")

print("\nTime Conversion")

hours = int(input("Enter Hours: "))
minutes = hours_to_minutes(hours)
print(f"{hours} hours = {minutes} minutes")

min=int(input("Enter Time in Min:  "))
seconds = minutes_to_seconds(min)

print(f"{minutes} minutes = {seconds} seconds")
