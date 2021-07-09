# List Comprehensions facilitates the processes of creating a list, it already creates the loop for you
# List Comprehensions vs Lists:
# List: [1, 2, "a", 33.1]
# List Comprehensions: [expr for val in collection]
# List Comprehensions: In this type the list will be created only with items that passes the tests
# List Comprehensions: [expr for val in collection if <test>]
# List Comprehensions: [expr for val in collection if <test1> and if <test2>]
# List Comprehensions: You can also loop over more than one collection
# List Comprehensions: [expr for val1 in collection1 and val2 in collection2]

# Example1:
# No list Comprehension
squares = []

for i in range(1, 101):
    squares.append(i**2) # ** Means ^

print(squares)
print("*********************************************************")

# With List Comprehension
squares2 = [i**2 for i in range(1, 101)]
print(squares2)
print("*********************************************************")

# Example2:
remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)
print("*********************************************************")

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)
print("*********************************************************")

#Example3(with if clause):
# Get the movies that only start with letter G
movies = ["Star Wars", "Gandhi", "Cassablanca", "Citizen Kane", "Thor", "Ghostbusters", "Good Will Hunting", "Close Encounters of the Third Kind", "Sharknado ", "Thor2", "Gattaca", "Pippi Longstocking", "Mary Poppins"]

# Without List Comprehension
gmovies1 = []

for title in movies:
    if title.startswith("G"):
        gmovies1.append(title) # Add to the list called gmovies

print(gmovies1)
print("*********************************************************")

# With List Comprehension
gmovies2 = [title for title in movies if title.startswith("G")]

print(gmovies2)
print("*********************************************************")

# Example4 ( with if clause):
# Get the movies that were released before 200 and ends with letter a
movies = [("Star Wars: The Phantom Menace", 1999), ("Gandhi", 1982), ("Cassablanca", 1942), ("Citizen Kane", 1941), ("Thor", 2011), ("Ghostbusters", 1984), ("Good Will Hunting", 1997), ("Close Encounters of the Third Kind", 1977), ("Sharknado", 2013), ("Thor2", 2013), ("Gattaca", 1997), ("Pippi Longstocking", 1969), ("Mary Poppins", 1964)]
pre2000 = [(title, year) for (title, year) in movies if year <= 2000 if title.endswith('a')]
print(pre2000)
print("*********************************************************")

