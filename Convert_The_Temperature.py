ans = []

celsiusTemp = float(input("Enter temp in celsius: "))
kelvinTemp = celsiusTemp + 273.15
fahreinheit = (celsiusTemp * 1.8) + 32.00

ans.append(kelvinTemp)
ans.append(fahreinheit)

print(ans)
print(f'Temperature at {celsiusTemp} Celsius converted in Kelvin is {ans[0]} and converted in Fahrenheit is {ans[1]}.')