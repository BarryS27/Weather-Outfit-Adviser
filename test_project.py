from project import get_temp_advice, get_cond_advice, format_report
import pytest


def test_get_temp_advice():
    assert get_temp_advice(-10) == "Wear a heavy coat or down jacket"

    assert get_temp_advice(0) == "Wear a hoodie or sweater"
    assert get_temp_advice(10) == "Wear a hoodie or sweater"

    assert get_temp_advice(15) == "Wear a light jacket"
    assert get_temp_advice(24) == "Wear a light jacket"

    assert get_temp_advice(25) == "Wear a t-shirt"
    assert get_temp_advice(30) == "Wear a t-shirt"


def test_get_cond_advice():
    rain_msg = "Wear a waterproof jacket (Hoodie up!) 🧥"
    assert get_cond_advice("Light Rain", 20) == rain_msg
    assert get_cond_advice("Drizzle", 10) == rain_msg

    snow_msg = "Wear winter boots ❄️"
    assert get_cond_advice("Heavy Snow", -15) == snow_msg

    sun_msg = "Don't forget sunglasses ☀️"
    assert get_cond_advice("Sunny", 30) == sun_msg
    assert get_cond_advice("Clear", 26) == sun_msg

    default_msg = "Enjoy your day!"
    assert get_cond_advice("Sunny", 10) == default_msg

    assert get_cond_advice("Cloudy", 20) == default_msg


def test_format_report():
    city = "Boston"
    temp = 12.0
    condition = "Rain"
    suggestion = "Wear a hoodie"

    result = format_report(city, temp, condition, suggestion)

    assert "Boston" in result
    assert "12.0" in result
    assert "Rain" in result
    assert "Wear a hoodie" in result
    assert "Location" in result
    assert "Suggestion" in result
