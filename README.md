# 🌤️ Weather & Outfit Advisor

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-red?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)

---

#### 📺 Video Demo:  <[Weather & Outfit Adviser](https://youtu.be/BU2cz8_t_jA)>

---

## 📖 Description

**"Weather & Outfit Advisor"** is a command-line interface (CLI) tool designed to solve a simple but recurring daily problem: checking the weather and figuring out *exactly* what to wear before leaving the house.

### 🧐 The Problem
As a student, I often find myself rushing out in the morning only to realize it is significantly colder than I anticipated, or getting caught in unexpected rain without an umbrella 🥶. While there are countless weather apps available on smartphones, they often feel "heavy" and cluttered with ads or excessive data that I do not need immediately.

### 💡 The Solution
My goal was to build a **lightweight, text-based solution** that runs directly in my terminal. It provides just the essential information—temperature and condition—along with a practical, actionable recommendation.

This project utilizes the **wttr.in** API to fetch real-time weather data 🌍. I selected this specific API because:
1.  It is developer-friendly.
2.  It supports JSON output natively.
3.  It does not require complex authentication keys.

The program parses the JSON response to extract the current temperature (in Celsius) and the weather condition description. Based on these data points, it applies a set of conditional logic rules to generate a user-friendly report.

---

## 📂 Files in the Project

The project is structured into three distinct files to maintain modularity and testability:

### 1. `project.py` 🐍
This file serves as the core entry point of the application. It imports `requests` for HTTP handling and `sys` for system-level operations. The logic is broken down into four main functions to adhere to the **Single Responsibility Principle**:

* **`main()`**: Orchestrates the program flow. It prompts the user for a city name, calls the fetching/processing functions, and prints the result. It also includes a critical check: if the city cannot be found, the program terminates gracefully using `sys.exit`.
* **`get_weather(city)`**: Handles network communication. It constructs the API URL and uses a `try...except` block to manage errors (e.g., timeouts, `IndexError`). It returns a tuple of `(temperature, condition)`.
* **`get_temp_advice(temp)`**: Encapsulates decision logic for clothing based on temperature ranges.
    * ❄️ **< 0°C**: Heavy coat
    * 🧥 **0-15°C**: Hoodie/Sweater
    * 👕 **15-25°C**: Light jacket
    * ☀️ **> 25°C**: T-shirt
* **`get_cond_advice(condition, temp)`**: Refines advice based on weather conditions (e.g., suggesting a raincoat ☔ for "Rain" or sunglasses 🕶️ for "Clear" days).
* **`format_report(...)`**: The "View" layer, formatting raw data into a clean, visually appealing string.

### 2. `test_project.py` 🧪
Testing was a major focus. Using `pytest`, I created a test suite to verify business logic without external API calls.
* `test_get_temp_advice()` checks boundary values to ensure `if/elif` logic flows correctly.
* `test_get_cond_advice()` verifies case-insensitive string matching.
* `test_format_report()` ensures the output string contains all necessary components.

### 3. `requirements.txt` 📦
Lists the dependencies (`requests` and `pytest`) needed to reproduce the environment.

---

## 🧗 Challenges Faced

One significant challenge was **handling invalid user input**. Initially, if a user typed a non-existent city, the `requests` call would return a 404 or text response, causing the JSON parser to crash.

> **Solution:** I implemented a robust `try...except` block in `get_weather`. If any exception occurs during fetching or parsing, the function returns `None`, allowing `main()` to exit cleanly with a helpful error message instead of a crash.

Another challenge was **logic conflict**. I had to ensure that `get_cond_advice` didn't overwrite the advice from `get_temp_advice`, but rather *complemented* it. I solved this by combining the outputs of both functions into a single, cohesive suggestion string.

---

## 🎨 Design Choices

I consciously chose to **separate "fetching" logic from "processing" logic**.

Initially, I considered putting everything in one function, but that made unit testing impossible without mocking the internet connection. By splitting `get_weather` (I/O bound) from `get_temp_advice` (CPU bound), I could write simple, fast unit tests for the logic parts. This structure mimics the **Model-View-Controller (MVC)** pattern, which I learned is a best practice in software engineering.

---

## 🔮 Future Improvements

If I had more time, I would like to add:
* 🌡️ **Unit Conversion:** Support for Fahrenheit/Celsius toggles.
* 🖥️ **Argparse:** Allow passing the city name directly as a command-line argument (e.g., `python project.py London`).
