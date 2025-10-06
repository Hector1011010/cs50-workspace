name = input('Give me a filename: ').lower()

if name.endswith(('.gif', '.png', '.jpeg', '.jpg')):
    print(f'image/{name.split(".")[-1]}')
elif name.endswith(('.pdf', '.zip')):
    print(f'application/{name.split(".")[-1]}')
elif name.endswith('.txt'):
    print("text/plain")
else:
    print("application/octet-stream")
