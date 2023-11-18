# WeatherApp
Window Size: Set a fixed window size (geometry("400x300")) for a more defined layout.
Padding: Added padding (pady) to provide space between widgets for better readability.
Button Styling: Styled the "Get Weather Info" button with a blue background and white text.
Font and Wrap Length: Used a larger font for the weather information display (font=("Helvetica", 12)) and set wraplength to limit the line length for better formatting.
--------------------------
Program Overview:
----------------
Import Statements:

The program begins by importing the necessary libraries: requests for making API requests and tkinter for creating the GUI.
API Key and Functions:

The get_weather function takes an OpenWeatherMap API key and a city as parameters and makes an API request to fetch weather data for the specified city.
The display_weather function formats and displays the weather information obtained from the API.
GUI Setup:

The Tkinter GUI is initialized using tk.Tk().
The program sets the window title to "Weather App" and fixes the window size to 400x300 pixels (app.geometry("400x300")).
Widgets:

Entry widgets are used to get the OpenWeatherMap API key and the city name from the user.
Labels are added to provide instructions for each entry field.
A Button widget triggers the get_weather_info function when clicked.

Button Styling:

The "Get Weather Info" button is styled with a blue background and white text to enhance visibility.
Weather Information Display:

The weather information is displayed using a Label widget. The result_text variable is updated dynamically based on the API response.

Functions:

The get_weather_info function is called when the user clicks the button. It retrieves the API key and city from the entry widgets, calls the get_weather function, and updates the GUI with the weather information.
Main Loop:

The program enters the Tkinter main loop (app.mainloop()), where it waits for user interactions.
How to Use:

API Key Entry:

Enter your OpenWeatherMap API key in the provided entry field.

City Name Entry:

Enter the name of the city for which you want to check the weather.

Get Weather Info Button:

Click the "Get Weather Info" button to fetch and display the weather information.
Display:
The weather information, including temperature, description, humidity, and wind speed, will be displayed in the window.
----------------------------
NOTE:
----
Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key before running the program.
