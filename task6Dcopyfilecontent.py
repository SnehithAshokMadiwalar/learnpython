# copy file content snehith
with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    dest.write(src.read())

