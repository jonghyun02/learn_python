n,m = map(int, input().split())
book = {}
for i in range(n): #도감 추가
    pokemon = input()
    num = str(i+1)
    book[pokemon] = num
    book[num] = pokemon

for i in range(m): #문제
    quiz = input()
    print(book[quiz])

#CHAT GPT 코드: 좀 더 보기 편하게 리스트, 딕셔너리로 자료형을 나눴음
# 포켓몬의 개수 N과 문제의 개수 M을 입력받습니다.
N, M = map(int, input().split())

# 포켓몬 이름을 저장할 리스트와 딕셔너리를 초기화합니다.
pokemon_list = [None] * (N + 1) #번호->이름, [None] * (N+1)은 None으로 N+1만큼 리스트를 초기화 한다는 뜻
pokemon_dict = {} #이름->번호

# 포켓몬 이름을 입력받아 리스트와 딕셔너리에 저장합니다.
for i in range(1, N + 1):
    name = input().strip()
    pokemon_list[i] = name
    pokemon_dict[name] = i

# 쿼리를 처리하고 출력합니다.
for _ in range(M):
    query = input().strip()
    
    if query.isdigit():  # 숫자인 경우
        index = int(query)
        print(pokemon_list[index])
    else:  # 문자(포켓몬 이름)인 경우
        print(pokemon_dict[query])
