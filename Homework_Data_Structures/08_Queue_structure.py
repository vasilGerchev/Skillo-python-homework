queue = []


def enqueue(element):
    queue.append(element)


def dequeue():
    return queue.pop(0)


enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
print(dequeue())