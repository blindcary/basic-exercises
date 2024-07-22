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
    
#15
import math
def sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
if __name__ == "__main__":
    radius = 6
    volume = sphere(radius)
    print(f"The volume of the shphere is {volume:.2f}")
    
#16
def difference(n):
    diff = n-17
    if n > 17:
        return 2 * abs(diff)
    else:
        return abs(diff)
if __name__ == "__main__":
    n = int(input("Enter a number:"))
    result = difference(n)
    print(f"the result is: {result}")

#17
def within_100(m):
    return abs(1000-m) <= 100 or abs(2000-m) <= 100
if __name__=="__main__":
    m = int(input("Enter a number:"))
    if within_100(m):
        print(f"The nuber {m} is within 100 of 1000 or 2000")
    else:
        print(f"The number {m} is not within 100 or 1000 or 2000")

#18
def sum(a,b,c):
    total_sum = a+b+c
    if a==b==c:
        return 3*total_sum
    else:
        return total_sum
if __name__ == "__main__":
    a = int(input("Enter a number for a:"))
    b = int(input("Enter a number for b:"))
    c = int(input("Enter a number for c:"))
    result = sum(a,b,c)
    print(f"The sum is: {result}")

#21
def even_or_odd(number):
    if number %2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
if __name__=="__main__":
    number = int(input("Enter a number of your choice:"))
    result = even_or_odd(number)
    print(result)

#25
def is_value_in_group(value, group):
    return value in group
if __name__=="__main__":
    test_value1 = int(input("Enter value 1:"))
    test_value2 = int(input("Enter value 2:"))
    test_group = [1,5,8,3]
    result1 = is_value_in_group(test_value1,test_group)
    result2 = is_value_in_group(test_value2,test_group)
    print(f"{test_value1} > {test_group} {result1}")
    print(f"{test_value2} > {test_group} {result2}")

#30
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area
if __name__=="__main__":
    base = int(input("Enter a a base value:"))
    height = int(input("Enter height value:"))
    area = area_of_triangle(base, height)
    print(f"The area of the triangle of base {base} and height {height} is {area:.2f}")

