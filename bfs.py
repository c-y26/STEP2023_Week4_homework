import collections

# visited
# |key|: 訪れたノード
# |value|: startからkeyが指す頂点までの距離
def calculate_distance(start, goal, links):
    queue = Queue()
    visited = {}
    visited[start] = 0
    queue.enqueue(start)
    while not queue.empty():
        node = queue.dequeue()
        if node == goal:
            return visited[node]
        for child in links[node]:
            if not child in visited:
                visited[child] = visited[node] + 1
                queue.enqueue(child)
    return -1
        

class Queue:
    
    def __init__(self):
        self.queue = collections.deque()
         
    def enqueue(self, node):
        self.queue.append(node)

    def dequeue(self):
        node = self.queue.popleft()
        return node

    def empty(self):
        if len(self.queue) != 0:
            return False
        else:
            return True
