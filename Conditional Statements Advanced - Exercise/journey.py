budget = float(input())
seasons = input()

destination = ""
place = ""
expenses = 0

if budget <= 100:
    destination = "Bulgaria"
    if seasons == "summer":
        place = "Camp"
        expenses = budget * 0.3
    elif seasons == "winter":
        place = "Hotel"
        expenses = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if seasons == "summer":
        place = "Camp"
        expenses = budget * 0.4
    elif seasons == "winter":
        place = "Hotel"
        expenses = budget * 0.8
else:
    destination = "Europe"
    place = "Hotel"
    expenses = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {expenses:.2f}")

