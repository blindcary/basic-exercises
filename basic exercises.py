#3
from datetime import datetime
now = datetime.now()
formatted_date_time=now.strftime("%d-%m-%Y %H:%M:%S")
print("date:",formatted_date_time)

#4
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

#5
def revers_name():
    first_name = input("Enter your first name:")
    last_name = input("Enyer last name:")
    print(last_name, "" ,first_name)
if __name__ == "__main__":
    revers_name()

#6
def list_and_tuple():
    input_sequence = input("Enter nums:")
    nums_list = input_sequence.split(',')
    nums_tuple = tuple(nums_list)
    print("List:", nums_list)
    print("Tuple:", nums_tuple)
if __name__ == "__main__":
    list_and_tuple()