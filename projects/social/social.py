from random import shuffle

import time
start_time = time.time()

class Queue():
    def __init__(self):
        self.storage = []
    
    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

class Stack():
    def __init__(self):
        self.storage = []
    
    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # iterate over 0 to num users 
        for i in range(num_users):
            # add user f"{user}+1}"
            self.add_user(f"user_{self.last_id}")

        # Create friendships
        # generate all possible friendships
        list_friends = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                list_friends.append((user_id, friend_id))
        # shuffle the friendships
        shuffle(list_friends)

        # take n number of friends from the front of the list
        # by using the equation num_users * avg_friendships // 2 (a for loop)
        for i in range((num_users * avg_friendships) // 2):
            friends = list_friends[i]
            # destructure the tuple
            user_id = friends[0]
            friend_id = friends[1]
            self.add_friendship(user_id, friend_id) 



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # dft with path
        # create empty Stack
        s = Stack()

        # push first user/friend path
        s.push([user_id])

        # while the stack is not empty
        while s.size() > 0:
            # pop the last element on stack
            path = s.pop()
            # get last item in path
            curr_user_id = path[-1]
            # check if visited:
            if curr_user_id not in visited:    
                # set visited[curr_user_id]=path
                visited[curr_user_id] = path
                # for each friend_id in friendships[curr_user_id]:
                for friend_id in self.friendships[curr_user_id]:  
                    # copy the path as new path
                    new_path = path.copy()
                    # append friend_id to new path
                    new_path.append(friend_id)
                    # push new path
                    s.push(new_path)
        # return visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    print("--- %s seconds ---" % (time.time()- start_time))
