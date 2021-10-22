import os, glob, json, shutil

try:
    os.mkdir('./processed')
except OSError:
    print ('The folder is there already man')

input = glob.glob("./process/index-[0-9]*.json")

subtotal = 0.0

for path in input:
    with open(path) as x:
        content = json.load(x)
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    dest = f"./processed/{name}"
    shutil.move(path, dest)
    print(f"moved '{path}' to '{dest}'")

print('TOTAL: $%.2f' % subtotal)