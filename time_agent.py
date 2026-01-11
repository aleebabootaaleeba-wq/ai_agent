import requests

def get_time(city):
    city_timezone = {
        "lahore": "Asia/Karachi",
        "peshawar": "Asia/Karachi",
        "new york": "America/New_York"
    }

    city = city.lower()
    if city not in city_timezone:
        return "Sorry, I don't know this city."

    url = f"http://worldtimeapi.org/api/timezone/{city_timezone[city]}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current_time = data["datetime"]
        return f"Current time in {city.title()} is {current_time}"
    else:
        return "Failed to fetch time."

# Loop for user queries
print("Time Agent is running (type 'exit' to stop)")

while True:
    user_input = input("Ask time: ")
    if user_input.lower() == "exit":
        break

    if "time" in user_input.lower():
        for city in ["lahore", "peshawar", "new york"]:
            if city in user_input.lower():
                print(get_time(city))
                break
        else:
            print("Please mention a supported city.")
