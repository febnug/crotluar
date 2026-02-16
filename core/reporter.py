import json

class Reporter:
    def __init__(self):
        self.data = {}

    def add(self, module, results):
        self.data[module] = results
        print(f"[+] {module} results recorded")

    def export_json(self, filename="report.json"):
        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)
