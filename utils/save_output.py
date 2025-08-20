import os

def save_output(agent_name: str, content: str):
    folder = f"./generated/{agent_name.lower()}"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, "output.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Output saved to {file_path}")
