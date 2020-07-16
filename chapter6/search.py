from collections import deque

graph = {}
graph["you"] = ["adit", "alice", "bob"]
graph["adit"] = ["cooper"]
graph["alice"] = ["john"]
graph["bob"] = ["dan"]
graph["cooper"] = []
graph["john"] = []
graph["dan"] = []

def search():
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == "john":
                print("Mango seller found!")
                return True
            else:
                search_queue += graph
                searched.append(person)
    return False

print(search())

