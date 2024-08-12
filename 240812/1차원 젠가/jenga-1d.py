from sys import stdin, stdout
n = int(stdin.readline()) #6

arr = [int(stdin.readline()) for _ in range(n)]

delete = [list(map(int, stdin.readline().split())) for _ in range(2)]   # 삭제할 인덱스 2개

#파이썬의 문자열 슬라이싱 활용
for s, e in delete:
    arr = arr[:s-1] + arr[e:]

#개수 출력
stdout.write(str(len(arr))+"\n")

#남은 젠가 출력
for i in arr:
    stdout.write(str(i)+"\n")