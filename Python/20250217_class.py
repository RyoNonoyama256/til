class Employee():
    def __init__(self, emp_id: int, name: str, salary: int):
        self.__emp_id: int = emp_id
        self.__name: str = name
        self.__salary: int = salary
    
    def _work(self) -> None:
        print("動きます")
    
    # def get_salary(self) -> int:
    #     return self.__salary
    
    # def set_salary(self, salary: int) -> None:
    #     self.__salary = salary

    @property
    def salary(self) -> int:
        return self.__salary
    
    @salary.setter
    def salary(self, salary: int) -> None:
        self.__salary = salary


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calc_area(self) -> int:
        pass

class Client:
    def __init__(self, shape: Shape):
        self.shape = shape

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def calc_area(self) -> int:
        return self.__width * self.__height
    
class Square(Shape):
    def __init__(self, length: int):
        self.__length = length
    
    def calc_area(self):
        return self.__lenght ** 2

