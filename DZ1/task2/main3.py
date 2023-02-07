with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines.sort(key=lambda x: int(x.split("-")[1].split(".")[0]))
    
with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line)