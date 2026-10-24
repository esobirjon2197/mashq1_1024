# 1-m
class Student:
    def __init__(self, fullname, grade):
        self.fullname = fullname
        self.grade = grade

    def __repr__(self):
        return f"Student('{self.fullname}', {self.grade}-sinf o'quvchisi)"


student1 = Student("Ali Karimov", 9)

print(student1)


# 2-m
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'"{self.title}" kitobining muallifi: {self.author}'


book1 = Book("O'tkan kunlar", "Abdulla Qodiriy")

print(book1)



# 3-m
class Phone:
    def __init__(self, brand, madel):
        self.brand = brand
        self.madel = madel

    def __repr__(self):
        return f"{self.brand} kompanyasining {self.madel}  telefoni"


phone = Phone("Samsung", "Galaxy A55")

print(phone)


# 4-m
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __repr__(self):
        return f"Rangi {self.color} bo'lgan avtomobil: {self.brand}"


car1 = Car("Chevrolet Cobalt", "Oq")

print(car1)


# 5-m
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Mahsulot: {self.name}, Narxi: {self.price} so'm"


product1 = Product("Sichqoncha", 85000)

print(product1)

