def calculate_windchill(T, V):
    return 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)

def calculate_c_f(C):
    return (C * 9/5) + 32

def main():
    temperature = float(input("What is the temperature? "))
    measured = input("Fahrenheit or Celsius (F/C)? ")
    if measured == "C":
        temperature = calculate_c_f(temperature)  

    for wind_speed in range(5,65,5):
        windchill = calculate_windchill(temperature, wind_speed)
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F")

if __name__ == "__main__":
    main()

    
