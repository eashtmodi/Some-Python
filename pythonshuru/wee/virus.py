import os

files = os.listdir()

for i in files:
    if i.endswith('.py'):
        pass
    else:
        try:
            os.rmdir(str(i))
        except:
            os.remove(str(i))
print('done')