def read_file_to_index(filename, index):
    with open(filename, 'r') as file:
        file.seek(index)
        content = file.read()
        return content

filename = 'your_file.txt'
index = 100  # Read up to the 100th byte

content = read_file_to_index(filename, index)
print(content)