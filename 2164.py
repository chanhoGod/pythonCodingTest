from collections import deque

N = int(input())

card_deck = deque()

for i in range(1, N + 1):
    card_deck.append(i)

change_time = True

while len(card_deck) > 1:
    if change_time == True:
        card_deck.popleft()
        change_time = False
    else:
        card_pop = card_deck.popleft()
        card_deck.append(card_pop)
        change_time = True

print(card_deck[0])