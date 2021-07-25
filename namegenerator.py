from string import ascii_letters

consonants = []
vowels = []

# NOTE: files must end in a new line or we loses the last letter
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


print("All my consonants: %s" % (consonants) )
print("All my vowels: %s" % (vowels) )

