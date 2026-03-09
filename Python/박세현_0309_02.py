from pandas.errors import ValueLabelTypeMismatch


class BlankError(Exception):
  def __init__(self):
    super().__init__("내용을 입력하세요.")

class IsalnumError(Exception):
  def __init__(self):
    super().__init__("상품코드는 영문자 및 숫자로만 구성되어있습니다.")

class SameError(Exception):
  def __init__(self):
    super().__init__("중복된 상품코드입니다.")

class IsalphaError(Exception):
  def __init__(self):
    super().__init__("문자만 입력가능합니다.")

class IsdigitError(Exception):
  def __init__(self):
    super().__init__("숫자(정수)만 입력가능합니다.")

class RangeError(Exception):
  def __init__(self):
    super().__init__("1 ~ 6사이의 숫자를 입력하세요.")

class Sangpum:
  def __init__(self):
    self._code = ""
    self._name = ""
    self._su = 0
    self._pri = 0
    self._price = 0

  def get_code(self):
    return self._code
  def set_code(self, code):
    self._code = code
  code = property(get_code, set_code)

  def get_name(self):
    return self._name
  def set_name(self, name):
    self._name = name
  name = property(get_name, set_name)

  def get_su(self):
    return self._su
  def set_su(self, su):
    self._su = su
  su = property(get_su, set_su)

  def get_pri(self):
    return self._pri
  def set_pri(self, pri):
    self._pri = pri
  pri = property(get_pri, set_pri)

  def get_price(self):
    return self._price
  def set_price(self, price):
    self._price = price
  price = property(get_price, set_price)


  def input_Sangpum_info(self, lst):
    while True:
      try:
        self._code = input("상품코드 입력(돌아가기 => 'exit' 입력) => ").strip()

        if self._code == "exit":
            print()
            return "menu"

        if self._code == "":
          raise BlankError()

        elif not self._code.isascii() and self._code.isalnum():
          raise IsalnumError()

        for item in lst:
          if item._code == self._code:
            raise SameError()

      except Exception as e:
        print(f"\nError : {e}\n")
        continue

      else:
        break

    while True:
      try:
        self._name = input("상품명 입력(돌아가기 => 'exit' 입력) => ").strip()

        if self._name == "exit":
            print()
            return "menu"

        if self._name == "":
          raise BlankError()

        elif not self._name.isalpha():
          raise IsalphaError()

      except Exception as e:
        print(f"\nError : {e}\n")

      else:
        break

  def __input_su_pri(self, num):
    while True:
        try:
            num = input(f"{num} 입력하세요(돌아가기 => 'exit' 입력) => ")

            if num == "exit":
                print()
                return "exit"

            elif not num.isdigit():
                raise IsdigitError()

            return int(num)

        except Exception as e:
            print(e)

  def update_price(self):
      result = self.__input_su_pri("수량을")
      if result == "exit":
          return "menu"
      self._su = result

      result = self.__input_su_pri("단가를")
      if result == "exit":
          return "menu"
      self._pri = result

      self._price = self._su * self._pri
      return self._price

  def output_product_info(self):
    print(f"{self._code}, {self._name}, {self._su}, {self._pri}, {self._price}")