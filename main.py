
from node import Node

node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")

print("=== INITIAL DATA ===")
node1.show_data()
node2.show_data()
node3.show_data()



node1.update_data("Age", 25)
node2.update_data("Age", 30)

print("\n=== CONSISTENCY VIOLATION ===")
node1.show_data()
node2.show_data()
node3.show_data()


node2.replicate_to([node1, node3])

print("\n=== AFTER CONFLICT RESOLUTION ===")
node1.show_data()
node2.show_data()
node3.show_data()
