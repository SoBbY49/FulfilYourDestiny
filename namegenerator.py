from string import ascii_letters

consonants = []
vowels = []
adjectives = []

# NOTE: files must end in a new line or we lose the last letter
for line in open('Data/bagofconsonants.txt', 'r'):
    holding = ""

    for letter in line:
        if letter in ascii_letters:
            holding = holding + letter
        elif letter in [',', '\n']:
            consonants.append(holding)
            holding = ""

for line in open('Data/bagofvowels.txt', 'r'):
    holding = ""

    for letter in line:
        if letter in ascii_letters:
            holding = holding + letter
        elif letter in [',', '\n']:
            vowels.append(holding)
            holding = ""

for line in open('Data/adjectives.txt', 'r'):
    holding = ""

    for letter in line:
        if letter in ascii_letters:
            holding = holding + letter
        elif letter in [',', ';', '\n']:
            adjectives.append(holding)
            holding = ""

print("All my adjectives: %s" % (adjectives) )
print("All my consonants: %s" % (consonants) )
print("All my vowels: %s" % (vowels) )

#Bubble sort
length = len(adjectives)

for i in range(length):
    for j in range(length-1):
        if adjectives[j] > adjectives[j + 1]:
            adjectives[j], adjectives[j + 1] = adjectives[j + 1], adjectives[j]


print(adjectives)
