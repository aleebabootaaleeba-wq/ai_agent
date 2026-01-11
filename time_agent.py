# Time Agent - Offline Version

print("Time Agent is running (type 'exit' to stop)")

def get_time(city):
    times = {
        "lahore": "10:00 AM",
        "peshawar": "10:00 AM",
        "new york": "12:00 AM"
    }
    city = city.lower()
    if city not in times:
        return "Sorry, I don't know this city."
    return f"Current time in {city.title()} is {times[city]}"

while True:
    user_input = input("Ask time: ").strip()
    if user_input.lower() == "exit":
        print("Exiting Time Agent...")
        break

    if "time" in user_input.lower():
        found = False
        for city in ["lahore", "peshawar", "new york"]:
            if city in user_input.lower():
                print(get_time(city))
                found = True
                break
        if not found:
            print("Please mention a supported city (Lahore, Peshawar, New York).")
    else:
        print("Please ask a question about the time.")
