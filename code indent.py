ENCODING = "utf-8"

path = r"C:\我是D槽\LaTeX\競程模板\競程模板.tex"

with open(path, "r", encoding=ENCODING) as file:
    text = file.readlines()

w = 2

output = []
in_code = False
for line in text:
    if line.startswith(r"\begin{minted}"):
        in_code = True
    elif line.startswith(r"\end{minted}"):
        in_code = False
    elif in_code:
        count = 0
        for c in line:
            if c != " ": break
            count += 1
        line = " " * (count // 4 * 2) + line[count:]
    output.append(line)

with open(path, "w", encoding=ENCODING) as file:
    file.write("".join(output))
