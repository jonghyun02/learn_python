s = input()
sub_str = set()
for i in range(len(s),0,-1):
    for j in range(len(s)-i+1):
        sub_str.add(s[j:j+i]) #O(n**3) n은 s의 길이
print(len(sub_str))

#CHAT GPT 코드: 접미사 배열과 LCP 배열 사용 -> 시간복잡도 O(nlogn) 나중에 찾아볼 것