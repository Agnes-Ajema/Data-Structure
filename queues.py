#implementation using queue.Queue

from queue import Queue
y=Queue(maxsize=4)
print(y.qsize())
y.put("Agnes")
y.put("Ajema")
y.put("Phines")
y.put("precious")
print(y)
print(y.full())

print(y.get())
print(y.get())
print(y.get())
print(y.get())

print(y.empty())
print(y.full())

from collections import deque
a=deque()
a.append(15)
a.append(16)
a.append(17)
a.append(18)
print(a)
