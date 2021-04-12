print("1.더하기 2.빼기 3.곱하기 4.나누기")
while True:
     item=int(input("원하는 기능을 선택하고 번호를 입력하세요"))
     A=int(input("첫번째 숫자 : "))
     B=int(input("두번째 숫자 : "))
     if item==1:
          print("더하기 결과 : ",A+B)
     elif item==2:
          print("빼기 결과 : ",A-B)
     elif item==3:
          print("곱하기 결과 : ",A*B)
     elif item==4:
          print("나누기 결과 : ",A/B)
     else:
          print("잘못입력하였습니다.")
          break
