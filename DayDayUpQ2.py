"""
DayDayUpQ2.py
Created in 2024/03/08/16:02 UTC+08
"""
dayFactor=float(input("Please enter a number:"))
dayUp=pow(1+dayFactor,365)
dayDown=pow(1-dayFactor,365)
print("向上：{:.2f},向下：{:.2f}".format(dayUp,dayDown))