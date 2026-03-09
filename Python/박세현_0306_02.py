class BlankError(Exception):
  def __init__(self):
    super().__init__("내용을 입력하세요.")

class HakbunError(Exception):
  def __init__(self):
    super().__init__("숫자(정수)만 사용 가능합니다.")

class SameError(Exception):
  def __init__(self):
    super().__init__("중복된 학번입니다.")

class IrumError(Exception):
  def __init__(self):
    super().__init__("문자만 입력 가능합니다.")

class RangeError(Exception):
  def __init__(self):
    super().__init__("0 ~ 100 사이의 숫자를 입력하세요.")

class Sungjuk:
  def __init__(self):
    self._hakbun = ""
    self._irum = ""
    self._kor = 0
    self._eng = 0
    self._math = 0
    self._tot = 0
    self._avg = 0.0
    self._grade = ""

  def get_hakbun(self):
    return self._hakbun
  def set_hakbun(self, hakbun):
    self._hakbun = hakbun
  hakbun = property(get_hakbun, set_hakbun)

  def get_irum(self):
    return self._irum
  def set_irum(self, irum):
    self._irum = irum
  irum = property(get_irum, set_irum)

  def get_kor(self):
    return self._kor
  def set_kor(self, kor):
    self._kor = kor
  kor = property(get_kor, set_kor)

  def get_eng(self):
    return self._eng
  def set_eng(self, eng):
    self._eng = eng
  eng = property(get_eng, set_eng)

  def get_math(self):
    return self._math
  def set_math(self, math):
    self._math = math
  math = property(get_math, set_math)

  def get_tot(self):
    return self._tot
  def set_tot(self, tot):
    self._tot = tot
  tot = property(get_tot, set_tot)

  def get_avg(self):
    return self._avg
  def set_avg(self, avg):
    self._avg = avg
  avg = property(get_avg, set_avg)

  def get_grade(self):
    return self._grade
  def set_grade(self, grade):
    self._grade = grade
  grade = property(get_grade, set_grade)

  def input_student_info(self, lst):
    while True:
      try:
        self._hakbun = input("학번 입력 => ").strip()

        if self._hakbun == "":
          raise BlankError()

        elif not self._hakbun.isdigit():
          raise HakbunError()

        for item in lst:
          if item._hakbun == self._hakbun:
            raise SameError()

      except Exception as e:
        print(f"\nError : {e}\n")
        continue

      else:
        break

    while True:
      try:
        self._irum = input("이름 입력 => ").strip()

        if self._irum == "":
          raise BlankError()

        elif not self._irum.isalpha():
          raise IrumError()

      except Exception as e:
        print(f"\nError : {e}\n")

      else:
        break

    self.update_student_score()
    return True

  # 추가 수정
  def input_student_score(self, subject):
    while True:
      try:
        score = int(input(f"{subject} 점수 입력 => ").strip())

        if not 0 <= score <= 100:
          raise RangeError()

        return score

      except ValueError:
        print("숫자(정수)를 입력하세요.")

      except RangeError as e:
        print(e)

  def update_student_score(self):
    self._kor = self.input_student_score("국어")
    self._eng = self.input_student_score("영어")
    self._math = self.input_student_score("수학")

  def process_student_sungjuk(self):
    self._tot = self._kor + self._eng + self._math
    self._avg = self._tot / 3
    if self._avg >= 90:
      self._grade = "수"
    elif self._avg >= 80:
      self._grade = "우"
    elif self._avg >= 70:
      self._grade = "미"
    elif self._avg >= 60:
      self._grade = "양"
    else:
      self._grade = "가"

  def output_student_info(self):
    print("%4s %3s %4d  %4d  %4d  %4d  %5.2f  %2s" %
          (self._hakbun, self._irum, self._kor, self._eng, self._math,
           self._tot, self._avg, self._grade))