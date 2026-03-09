
from 박세현_0309_02 import Sangpum, RangeError

lst = []

def menu_title():
  print("*** 상품관리 ***")
  print("1. 상품정보 입력")
  print("2. 상품정보 출력")
  print("3. 상품정보 조회")
  print("4. 상품정보 수정")
  print("5. 상품정보 삭제")
  print("6. 프로그램 종료")
  print()

def input_sungjuk():
  print()
  while True:
      obj = Sangpum()
      result = obj.input_Sangpum_info(lst)
      if result == "menu":
          break
      result = obj.update_price()
      if result == "menu":
          break
      lst.append(obj)
      print("\n상품 정보 입력 성공!!!\n")
      break

def print_sungjuk():
  if len(lst) == 0:
    print("\n출력할 데이터가 없음!!\n")
    return

  print("\n\t\t\t *** 상품관리 ***")
  print("=================================")
  print("상품코드   상품명   수량   단가  금액")
  print("=================================")
  tot_price = 0
  for obj in lst:
    obj.output_product_info()
    tot_price += obj.price
  print("=================================")
  print(f"\t\t\t 총금액: {tot_price}\n")

def search_sungjuk():
  if len(lst) == 0:
    print("\n조회할 데이터가 없음!!\n")
    return

  while True:
      code = input("\n조회할 상품코드 입력(돌아가기 => 'exit' 입력) => ").strip()

      if code == "exit":
          break

      for obj in lst:
        if obj.code == code:
          print("\n상품코드   상품명   수량   단가  금액")
          print("=================================")
          obj.output_product_info()
          print("=================================")
          break
      else:
        print("\n조회할 상품 정보가 없음!!!\n")

def update_sungjuk():
  if len(lst) == 0:
    print("\n수정할 데이터가 없음1!!\n")
    return

  while True:
      code = input("\n수정할 상품코드 입력(돌아가기 => 'exit' 입력) => ").strip()

      if code == "exit":
          return

      for obj in lst:
        if obj.code == code:
          print()
          result = obj.update_price()
          if result == "menu":
              return
          print(f"\n상품 코드 {code} 정보 수정 성공!!\n")
          break
      else:
        print("\n수정할 상품 정보가 없음!!!\n")

def delete_sungjuk():
  if len(lst) == 0:
    print("\n삭제할 데이터가 없음!!\n")
    return

  while True:
      code = input("\n삭제할 상품코드 입력(돌아가기 => 'exit' 입력) => ").strip()
      if code == "exit":
          break

      for obj in lst:
        if obj.code == code:
          lst.remove(obj)
          print(f"\n상품 코드 {code} 정보 삭제 성공!!\n")
          break
      else:
        print("\n삭제할 상품 정보가 없음!!!\n")

if __name__ == "__main__":
  while True:
    menu_title()
    try:
        menu = int(input("메뉴를 선택하세요(1~6) => ").strip())

        if 0 < menu <= 6:
          if menu == 1:
            input_sungjuk()
          elif menu == 2:
            print_sungjuk()
          elif menu == 3:
            search_sungjuk()
          elif menu == 4:
            update_sungjuk()
          elif menu == 5:
            delete_sungjuk()
          elif menu == 6:
            print("\n프로그램 종료!!")
            break
        else:
          raise RangeError
    except ValueError as e:
        print(f"\n1 ~ 6사이의 숫자(정수)를 입력해주세요.\n")
    except Exception as e:
      print(f"\n{e}\n")