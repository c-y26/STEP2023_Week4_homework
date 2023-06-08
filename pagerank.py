from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

class Graph:
    
    def __init__(self, links):
        self.node_num = len(links)
        self.node_info = {}
        self.links = links
        
            
    # step1: 全ノードに初期値1.0を与える    
    def initialize_all_node(self):
        for node in self.links:
            new_node = Node(node, self.links[node])
            self.node_info[node] = new_node
    
    # step2: 各ノードのページランクを振り分ける        
    def calculate_pagerank(self):
        all_node_attribute = 0
        for node in self.node_info:
            node_info = self.node_info[node]
            current_page_rank = node_info.page_rank
            if node_info.child_num == 0:
                # 隣接ノードがない場合
                all_node_attribute += current_page_rank / self.node_num
            else:
                # 隣接ノードがある場合
                child_node_attribute = current_page_rank * 0.85
                all_node_attribute += (current_page_rank * 0.15) / self.node_num
                child_node_attribute = child_node_attribute / node_info.child_num
                # ページランクの85%分を子ノードに分配する
                for child_node in node_info.child:
                    child_node_info = self.node_info[child_node]
                    child_node_info.new_page_rank += child_node_attribute
        
        # 各ノードのページランクのうち15%を全ノードに振り分ける
        # 隣接ノードがない場合は100%を全ノードに振り分ける
        for node in self.node_info:
            node_info = self.node_info[node]
            node_info.new_page_rank += all_node_attribute
    
    
    # step3: 各ノードのページランクを更新する
    # sum: 全nodeのpage_rankの合計値    
    def update_pagerank(self):
        #sum = 0
        for node in self.node_info:
            node_info = self.node_info[node]
            node_info.page_rank = node_info.new_page_rank
            node_info.new_page_rank = 0
            #sum += node_info.page_rank
        #print(sum)
        #print()
    
    def is_convergence(self):
        for node in self.node_info:
            node_info = self.node_info[node]
            current_page_rank = node_info.page_rank
            new_page_rank = node_info.new_page_rank
            if abs(current_page_rank - new_page_rank) > 10 ** (-1):
                return False
        return True
    
    def find_top_ten(self):
        list = []
        for node in self.node_info:
            node_info = self.node_info[node]
            node_value = node_info.node_value
            current_page_rank = node_info.page_rank
            list.append((current_page_rank, node_value))
            
        sorted_list = sorted(list, reverse=True)
        top10 = []
        if self.node_num < 10:
            num = self.node_num
        else:
            num = 10
        for i in range(num):
            top10.append(sorted_list[i])
        return(top10)
            

class Node:
    
    def __init__(self, node, child_list):
        self.node_value = node
        self.page_rank = 1.0
        self.new_page_rank = 0 
        self.child = child_list
        self.child_num = len(child_list)
    
