from collections import deque

def DuckDuckGoose(players, k):
    queue = deque(players)

    count = 1
    while len(queue) > 1:
        currentPlayer = queue.popleft()
        if count == k:
            # Player is removed from the game
            pass
        else:
            queue.append(currentPlayer)

        count += 1
        if count > k:
            count = 1

    return queue.pop()
