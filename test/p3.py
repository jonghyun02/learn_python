#if문
#Q1
a = "Life is to short, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
else:
    print("none")
#출력 : shirt

#while문
#Q1
i = 0
while True:
    i += 1
    if(i>5):
        break
    print(i*'*')

#for문
#Q1
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)