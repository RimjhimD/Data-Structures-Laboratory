# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:37:57 2023

@author: msi
"""

from collections import defaultdict, deque

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_connection(self, user1, user2):
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)
    
    def degree_centrality(self, user):
        return len(self.graph[user])
    
    def bfs_connected_users(self, start_user):
        visited = set()
        queue = deque([start_user])
        while queue:
            user = queue.popleft()
            visited.add(user)
            for neighbor in self.graph[user]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return len(visited) - 1  # Exclude the start_user itself
    
    def most_influential_users(self):
        return sorted(self.graph.keys(), key=lambda user: self.degree_centrality(user), reverse=True)
    
    def visualize_social_network(self):
        for user, connections in self.graph.items():
            print(user, " -> ", connections)

# Create the social network
network = SocialNetwork()
network.add_connection('User1', 'User2')
network.add_connection('User1', 'User3')
network.add_connection('User2', 'User4')
network.add_connection('User3', 'User4')
network.add_connection('User3', 'User5')

# Identify the most influential users
most_influential = network.most_influential_users()
print("Most Influential Users:", most_influential)

# Calculate connected users to User1
connected_count = network.bfs_connected_users('User1')
print("Connected Users to User1:", connected_count)

# Visualize the social network (for illustrative purposes)
print("Social Network Visualization:")
network.visualize_social_network()
