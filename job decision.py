# 직업선택 알고리즘

# 1. 그 일에서 얼마나 최고가 되고 싶은가? --> 1*a
# 2. 그 일에 얼마나 재능이 있는가? --> 0.8*b
# 3. 그 일에 얼마나 흥미가 있는가? --> 0.6*c
# 4. 이 일을 하며 평생을 살아도 얼만큼 괜찮은가? --> 0.7*d

# 평균이 0.49가 넘는 일을 하자. ( 산출근거 0.7*0.7 = 0.49 )
a = 0.8
b = 0.5
c = 0.7
d = 0.8


m = ((a*1) + (b*0.8) + (c*0.6) + (d*0.7))/4

print(m)

if m >= 0.49:
    print('하자')
else:
    print('하지말자')