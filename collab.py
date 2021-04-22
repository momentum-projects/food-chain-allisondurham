dictionary = {
    "fly": "I dont know why she swallowed the fly.",
    "spider": "She swallowed the spider to catch the fly.",
    "bird": "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
    "cat": "She swallowed the cat to catch the bird.", 
    "dog": "She swallowed the dog to catch the cat.",
    "goat": "She swallowed the goat to catch the dog.",
    "cow": "She swallowed the cow to catch the goat.",
    "horse": "I know an old lady who swallowed a horse."
}

poems = {
    "fly": "Perhaps she'll die.",
    "spider": "It wriggled and jiggled and tickled inside her.",
    "bird": "How absurd to swallow a bird.",
    "cat": "Imagine that, to swallow a cat!",
    "dog": "What a hog, to swallow a dog!",
    "goat": "Just opened her throat and swallowed a goat!",
    "cow": "I dont know how she swallowed a cow!",
    "horse": "She's dead of course!"
}

list_of_keys = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

def print_verse(animal):
    first_line(animal)
    poem_line(animal)

def poem_line(animal):
    print(poems[animal])

def first_line(animal):
    print("I know an old lady who swallowed a " + animal + ".")
    
def second_line(u_animal):
    print(u_animal)

def format(verse):
    for line in verse:
        print(line)
    print("")

for animal in list_of_keys:
    print_verse(animal)