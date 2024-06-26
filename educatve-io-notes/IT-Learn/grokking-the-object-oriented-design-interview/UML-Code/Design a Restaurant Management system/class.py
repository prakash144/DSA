# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
  def __init__(self, id, password, address, status=AccountStatus.Active):
    self.__id = id
    self.__password = password
    self.__address = address
    self.__status = status

  def reset_password(self):
    None


# from abc import ABC, abstractmethod
class Person(ABC):
  def __init__(self, name, email, phone):
    self.__name = name
    self.__email = email
    self.__phone = phone


# from abc import ABC, abstractmethod
class Employee(ABC, Person):
  def __init__(self, id, account, name, email, phone):
    super().__init__(name, email, phone)
    self.__employee_id = id
    self.__date_joined = datetime.date.today()
    self.__account = account


class Receptionist(Employee):
  def __init__(self, id, account, name, email, phone):
    super().__init__(id, account, name, email, phone)

  def create_reservation(self):
    None

  def search_customer(self, name):
    None


class Manager(Employee):
  def __init__(self, id, account, name, email, phone):
    super().__init__(id, account, name, email, phone)

  def add_employee(self):
    None


class Chef(Employee):
  def __init__(self, id, account, name, email, phone):
    super().__init__(id, account, name, email, phone)

  def take_order(self):
    None