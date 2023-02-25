#!/usr/bin/env python3

platforms = {}
with open("pip.log", "r") as log:
    for line in log:
        line = line.strip()
        if line != "py3-none-any" and line.startswith("py3-none-"):
            line = line[9:]
            if "linux" in line:
                if line.startswith("linux_"):
                    platforms[-2] = line
                elif line.startswith("manylinux_"):
                    _, a, b, *_ = line.split("_", maxsplit=3)
                    platforms[(int(a) * 1000) + int(b)] = line
                else:
                    platforms[-1] = line
            elif line.startswith("macosx_") and "universal" not in line:
                _, a, b, *_ = line.split("_", maxsplit=3)
                platforms[(int(a) * 1000) + int(b)] = line
            else:
                print(line)
if platforms:
    for _, it in sorted(platforms.items()):
        print(it)
