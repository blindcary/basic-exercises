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

 #7
def file_ext():
    file_name = input("Enter file name:")
    parts = file_name.split('.')
    if len(parts) > 1:
        ext = parts[-1].lower()
        print("Ext:",ext)
    else:
        print("No extension found")
if __name__ == "__main__":
    file_ext()

#9
def exam_schedule(exam_st_date):
    day, month, year = exam_st_date
    date = f"{day}/{month}/{year}"
    print(f"The examination will start from: {date}")
if __name__ == "__main__":
    exam_st_date = (11,12,2014)
    exam_schedule(exam_st_date)
    
#10
def value(n):
    n_str = str(n)
    nn = int(n_str * 2)
    nnn = int(n_str * 3)
    result = n + nn + nnn
    print("The value is = ",result)
if __name__ == "__main__":
    n = int(input("Enter a number:"))
    value(n)

#14
from datetime import date
def days(date1,date2):
    d1 = date(date1[2],date1[1],date1[0])
    d2 = date(date2[2],date2[1],date2[0])
    delta = d2-d1
    print(f"The number of days between {d1} and {d2} is: {delta.days} days")
if __name__ == "__main__":
    date1 = (2,7,2014)
    date2 = (11,7,2014)
    days(date1,date2)