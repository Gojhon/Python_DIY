try:
    no1=6
    no2=0
    no1/no2
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자가 아닙니다.")