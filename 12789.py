from collections import deque

N = int(input())

student_stack = list()
student_queue = deque()

input_student_list = list(map(int, input().split()))

for i in input_student_list:
    student_queue.append(i)

seq_count = 1

try:
    while seq_count < N:
        stack_pop = 0
        queue_pop = 0

        if len(student_queue) > 0:
            queue_pop = student_queue[0]
        
        if len(student_stack) > 0:
            stack_pop = student_stack[-1]
        
        if stack_pop == seq_count:
            seq_count += 1
            student_stack.pop()
            continue
        elif queue_pop == seq_count:
            seq_count += 1
            student_queue.popleft()
            continue
        elif queue_pop != seq_count:
            student_queue.popleft()
            student_stack.append(queue_pop)
            continue
        elif stack_pop != seq_count:
            print("Sad")
            break
except:
    print("Sad")

if seq_count == N:
    print("Nice")
    