# Windchill-Calculator
"""
Overview:
When it's cold outside and the wind is blowing, it feels even colder!

To try to quantify how cold it feels outside, instead of using temperature, a calculation for "wind chill" has been developed that takes into account both the temperature and the wind speed.

The U.S. National Weather Service defines the following formula to calculate wind chill in degrees Fahrenheit from a temperature in degrees Fahrenheit and wind speed in miles per hour:


Wind Chill Chart and Formula:
(To find the formula, follow the site (https://www.weather.gov/media/safety/windchillchart3.pdf) and look for the formula at the bottom of the chart.)


Keep in mind that:

T is the temperature in degrees Fahrenheit

V is the wind speed in miles per hour

V^0.16 means V to the power of 0.16, which can be found in Python using the ** operator.


Assignment:
My assignment is to write a program that asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.

My program compute and display the wind chill for wind speeds of 5, 10, 15, ..., 60 miles per hour, just like the National Weather Service chart does. To help users who are more familiar with Celsius, your program should allow temperature to be entered in either Celsius or Fahrenheit, and if needed, convert the Celsius temperature to Fahrenheit before using the formula.
"""
