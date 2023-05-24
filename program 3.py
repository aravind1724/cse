import math
v = float(input("Enter the wind Speed in kilometers/hour : "))
t = float(input("Enter the Temperature in Degrees Celsius : "))
ans = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
res = round(ans, 0)
print("The wind chill index is", res)