class Node:
    def __init__(self, name):
        self.name = name
        self.data = {
            "Student": "Zamanbek",
            "Age": 20
        }
    def update_data(self, key, value):
        self.data[key] = value

    def replicate_to(self, nodes):
        for node in nodes:
            node.data = self.data.copy()

    def show_data(self):
        print(f"{self.name}: {self.data}")