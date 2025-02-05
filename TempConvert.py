#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter a farenheit temperature")
  tempF = int(tempF)
  tempC = (tempF - 32) / 1.8
  num = tempC
  rounded_number = round(num, 1)

  print(tempF, "is ", rounded_number, "degrees celsius.")
if __name__ == '__main__':
  main()
