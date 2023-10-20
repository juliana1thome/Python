from collections import deque

deque1=deque([1,2,3,4,5])
print(deque1)
# deque([1, 2, 3, 4, 5])

deque2=deque('abcde')
print(deque2)
# deque(['a', 'b', 'c', 'd', 'e'])

deque3=deque([i for i in range(10) if i%2==0])
print(deque3)
# deque([0, 2, 4, 6, 8])