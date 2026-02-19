import os
import ast


class CodeIndexer:
    def __init__(self, root_directory):
        self.root = root_directory
        self.index = {}

    def build_index(self):
        for subdir, _, files in os.walk(self.root):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(subdir, file)
                    self.index[path] = self.extract_symbols(path)
        return self.index

    def extract_symbols(self, filepath):
        symbols = {
            "functions": [],
            "classes": []
        }

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    symbols["functions"].append(node.name)
                elif isinstance(node, ast.ClassDef):
                    symbols["classes"].append(node.name)

        except Exception:
            pass

        return symbols

    def search(self, query):
        results = []
        for file, content in self.index.items():
            for symbol_type in content:
                for name in content[symbol_type]:
                    if query.lower() in name.lower():
                        results.append({
                            "file": file,
                            "type": symbol_type,
                            "name": name
                        })
        return results
