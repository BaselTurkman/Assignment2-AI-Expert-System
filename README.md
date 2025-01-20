# Weather Expert System

This project is a simple Python-based weather expert system that predicts tomorrow's weather based on user inputs about various weather conditions today. It applies predefined rules to infer the weather, rainfall, temperature, and sky conditions for the next day.

## Features

- **Weather Prediction**: Predicts tomorrow's weather based on user inputs and applies expert rules to forecast various weather conditions.
- **Certainty Factor**: Uses certainty factors (numeric values between 0 and 1) to quantify the confidence level of the predictions.
- **Rule-Based Inference**: Applies predefined rules based on user inputs to adjust the certainty of weather conditions for the following day.

## How It Works

The system interacts with the user through the command line and asks for information about the current weather conditions:

1. **Weather (Rain or Dry)**: The user specifies whether today's weather is rainy or dry.
2. **Rainfall (Low or High)**: The user rates the certainty of today's rainfall as low or high.
3. **Temperature (Cold or Warm)**: The user provides information on whether today’s temperature is cold or warm.
4. **Sky (Overcast or Clear)**: The user describes the sky condition today (either overcast or clear).

Using these inputs, the system applies predefined rules to compute the probability of various weather conditions for tomorrow.

## Rules

1. **Rule 1 & 2**: If it rains today, there's a 50% chance of dry weather tomorrow.
2. **Rule 3**: If the rainfall is low today and it's raining, this influences the chance of dry weather tomorrow.
3. **Rule 4**: If it's cold and the rainfall is low today, the chance of dry weather tomorrow increases.
4. **Rule 5**: If it's warm and the weather is dry today, the chance of rain tomorrow increases.
5. **Rule 6**: If the sky is overcast and the temperature is warm today, the chance of rain tomorrow increases.

## Getting Started

### Prerequisites

- Python 3.x or higher

### Running the System

1. Clone the repository or download the `weather_expert_system.py` file.
2. Open a terminal or command prompt and navigate to the folder containing the file.
3. Run the script by executing:

    ```bash
    python weather_expert_system.py
    ```

4. The system will prompt you for inputs regarding today's weather conditions, and it will predict tomorrow’s weather based on the predefined rules.

## Example Interaction

Here’s an example of how the system works:

```plaintext
What is the Weather today? (rain / dry)? : rain
What is the rainfall today? (low / high)? : low
To what degree do you believe the rainfall is low? Enter a numeric certainty between 0 and 1.0 inclusive: 0.7
What is the Temperature today? (cold / warm)? : cold
To what degree do you believe the temperature is cold? Enter a numeric certainty between 0 and 1.0 inclusive: 0.8
What is the Sky today? (overcast / clear)? : overcast
To what degree do you believe the sky is overcast? Enter a numeric certainty between 0 and 1.0 inclusive: 0.6

Tomorrow's Forecast: {'rain': 0.65, 'dry': 0.4}
