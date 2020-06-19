#문자열 자료형
print("ㅋ"*9)
# boolean 자료형 참 /거짓
print(not True)
print(not False)
print(not(5>10))
#변수-어떠한 값을 저장하는 공간
animal="강아지"
name="연탄이"
age=4
hobby="산책"
is_adult= age>=3
print("우리집"+animal+"의 이름은"+name+"에요")
print(name+"는"+str(age)+"살이며"+hobby+"을 아주 좋아해요")
print(name,"는", (age), "살이며", hobby, "을 아주 좋아해요")
print(name+"는 어른일까요"+str(is_adult))
#리스트
subway=[10,20,30]
print(subway)
print(subway.index(10))#10이 몇번째 칸에 있는가?
subway.append(40)#리스트에 40을 추가
subway.insert(1,15)#15를 10/20사이에 추가
print(subway.pop())#위에 있는 값부터 하나씩 꺼낸다
print(subway)
print(subway.count)#같은 값이 몇번 있는지 카운트
#리스트 정렬
num_list=[5,3,2,1,4]
num_list.sort()#오름차순으로 정렬
print(num_list)
num_list.reverse#내림차순으로 정렬
print(num_list)
#리스트 지우기
num_list.clear()
print(num_list)
#다양한 자료형 함께 사용
mix_list=["최담록",20,True]
print(mix_list)
#리스트 확장
num_list.extend(mix_list)
print(num_list)