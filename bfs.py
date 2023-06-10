import collections

# visited
# |key|: 訪れたノード
# |value|: startからkeyが指す頂点までの距離
def calculate_distance(start, goal, links):
    queue = Queue()
    visited = {}
    visited[start] = True
    path = {}   # 経路を記憶/各ノードの親ノードを記憶しておく
    queue.enqueue(start)
    while not queue.empty():
        node = queue.dequeue()
        if node == goal:
            ans = calculate_path(path, start, goal)
            return ans
        for child in links[node]:
            if not child in visited:
                visited[child] = True
                path[child] = node
                queue.enqueue(child)
    return "Not Found"

def calculate_path(path, start, goal):
    ans = []
    child_node = goal
    while child_node != start:
        ans.append(child_node)
        child_node = path[child_node]
    ans.append(start)
    ans_reverse = []
    for i in range(len(ans)):
        n = len(ans)
        ans_reverse.append(ans[(n-1)-i]) 
    return ans_reverse   
        

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
        

    
    
