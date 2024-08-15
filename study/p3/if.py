coding_lan = ['Java','Python','C']
if 'html' in coding_lan:
    print("프로그래밍 언어")
else:
    pass #아무것도 안함

if 'html' not in coding_lan:
    print("프로그래밍 언어가 아님")
else:
    pass #아무것도 안함

a = 1
if a or False: # ||, &&, ! 사용 불가능. or, and, not으로 해야함.
    print("oh")