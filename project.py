import requests
import sys


def main():
    print("Tip: For US cities, you can add state code (e.g., 'Boston, MA')")
    city = input("City: ").strip()
    temp,condition = get_weather(city)
    if (temp is None) or (condition is None):
        sys.exit("Could not find city or connection error.")

    temp_msg = get_temp_advice(temp)
    cond_msg = get_cond_advice(condition, temp)
    suggestion = f"{temp_msg}, {cond_msg}"
    report = format_report(city,temp,condition,suggestion)
    print(report)


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1&lang=en"
    try:
        response = requests.get(url)
        data = response.json()
        temp = float(data['current_condition'][0]['temp_C'])
        condition = data['current_condition'][0]['weatherDesc'][0]['value']
        return temp,condition
    except (IndexError, requests.RequestException, ValueError):
        return None,None


def get_temp_advice(temp):
    if temp < 0:
        return "Wear a heavy coat or down jacket"
    elif 0 <= temp < 15:
        return "Wear a hoodie or sweater"
    elif 15 <= temp < 25:
        return "Wear a light jacket"
    else:
        return "Wear a t-shirt"


def get_cond_advice(condition,temp):
    cond = condition.lower()
    if "rain" in cond or "drizzle" in cond:
        return "Wear a waterproof jacket (Hoodie up!) 🧥"
    elif "snow" in cond:
        return "Wear winter boots ❄️"
    elif ("clear" in cond or "sunny" in cond) and temp > 25:
        return "Don't forget sunglasses ☀️"
    else:
        return "Enjoy your day!"


def format_report(city,temp,condition,suggestion):
    return (
        f"\n{'-' * 30}\n"
        f"📍 Location:   {city}\n"
        f"🌡️  Temp:       {temp}°C\n"
        f"👀 Condition:  {condition}\n"
        f"{'-' * 30}\n"
        f"💡 Suggestion: {suggestion}\n"
        f"{'-' * 30}\n"
    )


if __name__ == "__main__":
    main()
