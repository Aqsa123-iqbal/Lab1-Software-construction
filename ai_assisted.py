# CSE325-2026-L01-K7QX-T2
"""Lab 01 Task 2: AI-assisted converter (branch: ai-build)."""

RUN_PROFILE = {"ratio": 9 / 5, "offset": 32}


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * RUN_PROFILE["ratio"] + RUN_PROFILE["offset"]


def read_celsius(prompt: str = "Celsius: ") -> float:
    """Ask until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value, e.g. 36.6")


if __name__ == "__main__":
    value = read_celsius()
    print(f"{value}C = {celsius_to_fahrenheit(value)}F")
