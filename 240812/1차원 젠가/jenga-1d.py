from sys import stdin, stdout
n = int(stdin.readline()) #6

def oneToTow(x):
    if len(x) == 1:
        return "00"+x
    elif len(x) == 2:
        return "0"+x
    else:
        return x

#문자열로 입력받기
arr = ""
for _ in range(n):
    arr += oneToTow(input())


delete = [list(map(int, stdin.readline().split())) for _ in range(2)]   # 삭제할 인덱스 2개

#파이썬의 문자열 슬라이싱 활용
for s, e in delete:
    arr = arr[:s*3-3] + arr[e*3:]

#개수 출력
print(int(len(arr)/3))
#남은 젠가 출력
for i in range(0, len(arr), 3):
    print(int(arr[i]+arr[i+1]+arr[i+2]))