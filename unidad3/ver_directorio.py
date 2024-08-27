import os

with os.scandir('files/') as directorio:
    for item in directorio:
        print(item.name)