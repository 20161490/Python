print("1.더하기 2.빼기 3.곱하기 4.나누기")
while True:
    item=int(input("원하는 기능을 선택하고 번호를 입력하세요"))
    a=int(input("1번째 숫자"))
    b=int(input("2번째 숫자"))
    c=[a+b]
    d=[a-b]
    e=[a*b]
    f=[a/b]
    for c1 in c:
        if item==1:
            print("더하기 결과 : ",c1)
    for d1 in d:
        if item==2:
            print("빼기 결과 : ",d1)
    for e1 in e:
        if item==3:
            print("곱하기 결과 : ",e1)
    for f1 in f:
        if item==4:
            print("나누기 결과 : ",f1)
    if item>4:
        print("잘못입력하셧습니다.")
        break
    elif item<1:
        print("잘못입력하셧습니다.")
        break
    

