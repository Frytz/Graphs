from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return (len(self.queue))

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = {}

print(player.current_room.id)
print(player.current_room.get_exits())

directions = ('n', 's', 'e', 'w')

inverseDirections = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
def traverseMap(player, direction = ''):
    
    # Check if all rooms have been explored and stop if they have.
    if len(graph.keys()) == 500:
        return
    # While the map is not completely explored
    # If the room doesn't exist

    currentRoom = player.current_room.id

    if player.current_room.id not in graph:
            # Initialize in your room graph with '?' exits
            graph[player.current_room.id] = {}
            for exit in player.current_room.get_exits():
                graph[player.current_room.id][exit] = '?'

    # If coming from another room
    if direction is not '':
        # find opposite direction of current travel
        opposite = inverseDirections[direction]
        # set prevRoom using Room method 'getRoomInDirection'
        prevRoom = player.current_room.get_room_in_direction(opposite)
        # Update the graph the entry for previous room
        graph[currentRoom][opposite] = prevRoom.id

    new_direction = '?'

    # If there is an unexplored exit in the current room (i.e. a '?' exit), travel in that direction
    for exit in player.current_room.get_exits():
        if graph[currentRoom][exit] == '?':
            # if the current room has an unexplored exit set the new_direction to that exit
            new_direction = exit
            # travel there and append the current exit to the traversal path
            player.travel(exit)
            traversal_path.append(exit)
            # set new_room to the player's current room and set the previous room's exit to the new room
            new_room = player.current_room.id
            graph[currentRoom][exit] = new_room
            # Walk there
            traverseMap(player, exit)
            break

    # Else, find the nearest room using BFS with an unexplored exit and travel there
    # Set a travel_path
    travel_path = []

    if new_direction is '?':
        # Setup a new Queue with the currentRoom
        q = Queue()
        visited = set()
        q.enqueue([currentRoom])

        while q.size() > 0:
            # While there is something in the Queue take out the last item and set current room to the last item in path
            path = q.dequeue()
            currentRoom = path[-1]

            if currentRoom not in visited:
                visited.add(currentRoom)

                # If currentRoom has an unexplored exit
                if '?' in graph[currentRoom].values():
                    # Return path to that room and reset the queue
                    travel_path = path
                    q = Queue()
                    break

                for neighbor in graph[currentRoom].values():
                    # for every direction in the current room add it to the path to search through and add it to the queue
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    for r in travel_path:
        # for every room in the travel path
        room = player.current_room.id
        g_keys = graph[room].keys()
        for d in g_keys:
            # For every room we walked along add the values that match to that room to our traversal path
            if graph[room][d] == r:
                player.travel(d)
                traversal_path.append(d)

    # Explore the map again now that we are at a room with an unexplored exit
    traverseMap(player)

traverseMap(player)


# print(graph)
# print(traversal_path)
# print("\n*****")


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
