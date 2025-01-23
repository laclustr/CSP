import os

end_range = 13

for i in range(1, end_range):
    os.mkdir(f"{i:04d}")
"""
for i in range(1, end_range):
    with open(os.path.join(f"{i:04d}", f"{i:04d}.py"), "w") as file:
        file.write("")
"""