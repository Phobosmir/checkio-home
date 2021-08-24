

def count(file):
    return sum(1 for line in file.open() for char in line if char.isupper() )
