arr = input().split()
arr = list(map(int,arr))
arr.sort()
print(arr)

d = 2
n = len(arr)
x = 5
for i in range(len(arr)):
	n //= d
	if arr[i] > x:i -= n
	elif arr[i] < x:i += n
	elif arr[i] == x:
		print("found at %s" % i)
		break
	d *= 2
