from sys import stdin, stdout
n = int(stdin.readline()) #6

#문자열로 입력받기
arr = ""
for _ in range(n):
    arr += input()


delete = [list(map(int, stdin.readline().split())) for _ in range(2)]   # 삭제할 인덱스 2개

#파이썬의 문자열 슬라이싱 활용
for s, e in delete:
    arr = arr[:s-1] + arr[e:]

#개수 출력
print(len(arr))
#남은 젠가 출력
for i in range(len(arr)):
    print(arr[i])