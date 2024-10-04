import timeit

# 실행할 코드 정의
code_to_test = """
    # 여기에 실행할 코드를 넣으세요.
"""

# 실행 시간 측정
elapsed_time = timeit.timeit(code_to_test, number=10)  # 10번 실행

print(f"평균 실행 시간: {elapsed_time / 10}초")