file = open("arquivo_txt/dados.txt", 'w+')
file.write("Fulano\n")
file.write("cicrano\n")
file.write("beltrano\n")

file.seek(0)
print(file.read())

file.seek(0)
print(file.readline())

file.seek(0)
print(file.readlines())

file.seek(0)
for name in file.readlines():
    print(name[:-1])

file.seek(0)
for name in file.readlines():
    print(name)

