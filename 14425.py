# N, M = map(int, input().split())

# N_list = [input().strip() for i in range(N)]
# N_dict = {key:1 for key in N_list}

# M_list = [input().strip() for i in range(M)]

# answer_num = 0

# for i in M_list:
#     if i in N_dict:
#         answer_num += 1
        

# print(answer_num)



# 트라이 - 문자열 검색을 빠르게 실행할 수 있도록 설계한 트리 형태의 자료구조
import sys

read = sys.stdin.readline

N, M = map(int, read().strip().split())

# 노드 클래스 생성, isEnd는 문자열의 끝인지 아닌지를 나타내는 변수, childNode는 자식 노드를 저장하는 딕셔너리
class Node:
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.childNode = {}
        
# 트라이 클래스 생성, 문자열 삽입 메서드와 문자열 탐색 메서드 생성
class Trie:
    def __init__(self):
        self.parent = Node(False)
    
    def insert(self, string):
        nowNode = self.parent
        tmp_length = 0
        
        for char in string:
            # 자식 노드들에서 미생성된 문자열이면 새로 생성
            if char not in nowNode.childNode:
                nowNode.childNode[char] = Node(False)
            
            nowNode = nowNode.childNode[char]
            tmp_length += 1
            if tmp_length == len(string):
                nowNode.isEnd = True
        
    def search(self, string):
        nowNode = self.parent
        tmp_length = 0
        for char in string:
            if char in nowNode.childNode:
                nowNode = nowNode.childNode[char]
                tmp_length += 1
                if tmp_length == len(string) and nowNode.isEnd == True:
                    return True
            else:
                return False
        
        return False

myTrie = Trie()
result = 0

for _ in range(N):
    myTrie.insert(read().strip())

for _ in range(M):
    if myTrie.search(read().strip()) == True:
        result += 1

print(result)