from unittest import result

pi = 3.14

def circle_area(r):
    #circle_area(r)의 local 영역
    global pi
    pi = pi + 0.0015
    result = pi * (r ** 2)
    return result

if __name__ == "__main__":
    print(f"PI : {pi}")
    print(f"반지름 : {3} 면적 : {circle_area(3)}")
    print(f"PI : {pi}")