from collections import deque
 
def reverse_first_k(q, k):
    solve(q, k)
    s = len(q) - k
    for _ in range(s):
        x = q.popleft()
        q.append(x)
    return q
 
def solve(q, k):
    if k == 0:
        return
    e = q.popleft()
    solve(q, k - 1)
    q.append(e)

queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
k = 5
queue = reverse_first_k(queue, k)
 

while queue:
    print(queue.popleft(), end=' ')