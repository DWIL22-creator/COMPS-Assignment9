class Person:
    def __init__(self, name):
        self.name = name
        self.friends = [] #Initialized as an empty list.

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

deriya = Person("Deriya")
print(deriya.name)
jose = Person("Jose")
print(jose.name)
lynda = Person("Lynda")
print(lynda.name)
angel = Person("Angel")
print(angel.name)

deriya.add_friend(jose)
deriya.add_friend(lynda)
deriya.add_friend(angel)

print(f"{deriya.name} connects to: {[friend.name for friend in deriya.friends]}")
'''
        A class representing a person in a social network.
        Attributes:
            name (str): The name of the person.
            friends (list): A list of friends (Person objects).
        Methods:
            add_friend(friend): Adds a friend to the person's friend list.
'''


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name): #Should add a new name/person to the network.
        if name not in self.people:
            self.people[name] = Person(name) #Creates a new person object 

    def add_friendship(self, person1_name, person2_name):
        #Modeling a bidirectional connection between two people. Like a friendship.
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]

            #Create the friendship connection
            #You can't add the other person to their own friend list.
            person1.add_friend(person2)
            person2.add_friend(person1)

        else:
            print(f"Both people must be in the network before adding a friendship!")

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} connects to: {friend_names}")

network = SocialNetwork()
network.add_person("Deriya")
network.add_person("Deriya") #Testing adding duplicate people.
network.add_person("Jose")
network.add_person("Lynda")
network.add_person("Angel")
network.add_person("Latavia")
network.add_person("Vaya")

print("")
print("Current Network:")
network.print_network() #Printing network to see what names were added.

network.add_friendship("Deriya", "Jose") #1
network.add_friendship("Lynda", "Deriya") #2
network.add_friendship("Jose", "Angel") #3
network.add_friendship("Latavia", "Vaya")#4
network.add_friendship("Latavia", "Deriya") #5
network.add_friendship("Deriya", "Vaya") #6
network.add_friendship("Latavia", "Lynda") #7
network.add_friendship("Vaya", "Jose") #8


network.add_friendship("Latavia", "Amani") #Adding a friendship where one person doesn't exist.

print("")
print("New Network!")
network.print_network()

'''
1) A graph is the right structure to represent a social network because graphs represent how relationships are bidirectional, that more than one connection can exist, that there is no hierarchy with friends, and complex pathways matter to discover community. 
In this scenario people are nodes (vertices) and friendships are edges. You can have multiple friends, in the same way that people could have one friend.
Not everyone in the network will be friends, which is ideal for adjacency lists because they store only actual connections which is more memory efficient. 
This can be modeled with the add_friendship section, that highlights which connections are forged. 
Despite the complexity of friends, multiple connections exist, and new communities are forged from the friendships created.

2) A list or tree wouldn't work well for this because it has no built in way to represent relationships between people in the list. 
To track connections, I would need to build a separate data structure, which would be highly counterintuitive. 
Additionally, a tree structure enforces a strict parent child hierarchy with no cycles. 
In a social network, friendships are peer-to-peer and can form cycles. 
For instance, A is friends with B, B with C, and C with A. 
Trees cannot represent cycles, so they would either lose information or not accurately capture the relationships in a non-hierarchical manner.

3) With an adjacency list, adding a friend is O(1) on average - you just append to a list. 
Printing the network requires iterating through all people and their friends, so it's O(V+E). 
For a small network this is fine, but it would slow down significantly with a larger network. 
Lastly, with adjacency lists it's memory efficient for sparse networks, but for a larger friendship list, switching to a set would trade memory for speed.
'''