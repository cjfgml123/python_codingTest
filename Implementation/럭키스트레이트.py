N = list(input())
N = list(map(int,N))

index = len(N) // 2
_list1 = N[0:index]
_list2 = N[index:]

if sum(_list1) == sum(_list2):
    print("LUCKY")
else:
    print("READY")

