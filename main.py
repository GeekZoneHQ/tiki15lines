import os

directory = r'files_here'
for entry in os.scandir(directory):
    print(entry.path)
    with open(entry.path, 'r') as f_in:
        data = f_in.read().splitlines(True)
    with open(entry.path, 'w') as f_out:
        f_out.writelines(data[15:])

