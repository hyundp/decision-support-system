# 직업선택 알고리즘
# 평균이 0.49가 넘는 일을 하자. ( 산출근거 0.7*0.7 = 0.49 )


a = float(input("1. 그 일에서 얼마나 최고가 되고 싶은가? (0 ~ 1)\n"))*1
b = float(input("2. 그 일에 얼마나 재능이 있는가? (0 ~ 1)\n"))*0.8
c = float(input("3. 그 일에 얼마나 흥미가 있는가? (0 ~ 1)\n"))*0.6
d = float(input("4. 이 일을 하며 평생을 살아도 얼만큼 괜찮은가? (0 ~ 1)\n"))*0.7
e = float(input("5. 평생 그 일에서 활용되는 능력을 발전시키며 살 수 있는가? (0 ~ 1)\n"))*0.8
f = float(input("6. 돈을 얼만큼 벌 수 있는가? (0 ~ 1)\n"))*0.7
g = float(input("7. 사회적으로 얼만큼 인정받을 수 있는가? (0 ~ 1)\n"))*0.6
h = float(input("8. 그 일을 시작하는 것이 얼만큼 쉬운가? (0 ~ 1)\n"))*0.4
i = float(input("9. 그 일을 지속하는 것이 얼만큼 쉬운가? (0 ~ 1)\n"))*0.5
j = float(input("10. 그 일을 하는 것이 사랑하는 사람들을 얼만큼 위한 일인가? (0 ~ 1)\n"))*0.7

question_list = [a, b, c, d, e, f, g, h, i, j]
m = sum(question_list) / len(question_list)

print("합계 : ", m)

if m >= 0.49:
    print('하자')
else:
    print('하지말자')