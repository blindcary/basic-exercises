#2
# from datetime import datetime
# now = datetime.now()
# formatted_date_time=now.strftime("%d-%m-%Y %H:%M:%S")
# print("date:",formatted_date_time)

#3
import math
def calculate_area_of_circle(radius):
    area = math.pi * (radius ** 2)
    return area
def main():
    radius = float(input("radius:"))
    area = calculate_area_of_circle(radius)
    print("radius:",radius,"area:",area)
if __name__ == "__main__":
    main()