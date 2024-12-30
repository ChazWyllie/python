# r+ read and write
with open('file-io/data/null.txt', 'r+') as f: 
    print(f.read())
    f.write("This will overwrite the original content")
    f.write("\nThis will append to the original content")
    print(f.read())
