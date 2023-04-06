import threading
import random
import time

# number of nodes in the network
num_nodes = 5

# number of gossip rounds
num_rounds = 10

# number of voting values
num_voting_values = 3

# list of nodes in the network
nodes = []

# initialize the nodes with random voting values
for i in range(num_nodes):
    nodes.append({'id': i, 'voting': random.randint(1, num_voting_values)})

# function to perform gossiping


def gossip(node):
    # select a random node to send the message to
    target_node = random.choice(nodes)

    # check if the target node has the same voting value as the source node
    if node['voting'] == target_node['voting']:
        return

    # update the voting value of the target node
    target_node['voting'] += node['voting']

    # print the gossip message
    print(f"Node {node['id']} sent a message to Node {target_node['id']}")

# function to simulate the gossip protocol


def simulate_gossip():
    for i in range(num_rounds):
        # select a random node to start gossiping from
        source_node = random.choice(nodes)

        # perform gossiping
        gossip(source_node)

# create a thread for each node in the network
threads = []
for node in nodes:
    t = threading.Thread(target=simulate_gossip, args=())
    threads.append(t)

# start the threads
for t in threads:
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

# print the final voting values of all nodes
for node in nodes:
    print(f"Node {node['id']} has voting value {node['voting']}")
