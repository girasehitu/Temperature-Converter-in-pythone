def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Welcome to Temperature Converter!")
    
    while True:
        print("\nChoose the conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius} Celsius = {celsius_to_fahrenheit(celsius)} Fahrenheit")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius} Celsius = {celsius_to_kelvin(celsius)} Kelvin")
        elif choice == '3':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit = {fahrenheit_to_celsius(fahrenheit)} Celsius")
        elif choice == '4':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit = {fahrenheit_to_kelvin(fahrenheit)} Kelvin")
        elif choice == '5':
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin} Kelvin = {kelvin_to_celsius(kelvin)} Celsius")
        elif choice == '6':
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin} Kelvin = {kelvin_to_fahrenheit(kelvin)} Fahrenheit")
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
