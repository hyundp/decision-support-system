# case 1. 42서울 소프트웨어 라피신 등록취소 할 때 사용한 방법.
# 1. 지금 하지 않더라도 다음에 할 수 있는가?
# 2. 할 수 있다면 그 과정은 다시 시작하기 쉬운가?
# 3. 비슷한 효과를 얻을 수 있는 대체제가 있는가??
# 4. 지금 하면 온전히 그 활동에 집중할 수 있는가?
# 5. 포기해야할 것이 시간, 노력 이외에 있는가?
# 6. 포기해야 하는 것들은 선택전략을 처음부터 해봤을 때 어떤 가치를 가지는가?
# 7. 죽기전에 후회할까?
# 8. 둘다 할 수 있는가?

questionList = ["1. 지금 하지 않더라도 다음에 할 수 있는가?", "2. 다음에 할 수 있다면 그 과정은 다시 시작하기 쉬운가?",
                "3. 비슷한 효과를 얻을 수 있는 대체제가 있는가?", "4. 지금 하면 온전히 그 활동에 집중할 수 있는가?",
                "5. 포기해야할 것이 시간, 노력 이외에 있다면, 그것의 가치는 어느정도인가?",
                "6. 죽기전에 후회할까?"]

answerList = []

questionValue = [6, 4, 5, 6, 0, 10]


for x in range(0, len(questionList)):
    print(questionList[x])
    print('당신이 생각한 정도를 적어주세요 0~1')
    answerList[x] = input()
    
