from collections import deque

class MainQueue:
    def queueExample(self):
        queue = deque()
        queue.append("Java")
        queue.append("DotNet")
        queue.append("PHP")
        queue.append("HTML")
        print("remove:", queue.popleft())
        print("element:", queue[0])
        print("poll:", queue.popleft())
        print("peek:", queue[0])

if __name__ == "__main__":
    main_queue = MainQueue()
    main_queue.queueExample()
