from abc import ABC, abstractmethod
import datetime

class Order(ABC):
  def __init__(self, id):
    self.__order_id = id
    self.__is_buy_order = False
    self.__status = OrderStatus.OPEN
    self.__time_enforcement = TimeEnforcementType.ON_THE_OPEN
    self.__creation_time = datetime.datetime.now()

    self.__parts = {}

  def set_status(self, status):
    self.status = status

  def save_in_DB(self):
  # save in the database

  def add_order_parts(self, parts):
    for part in parts:
      self.parts[part.get_id()] = part


class LimitOrder(Order):
  def __init__(self):
    self.__price_limit = 0.0