



dict_second_line = {
    "spider" : "It wriggled and jiggled and tickled inside her.",
    "bird" : "How absurd to swallow a bird.",
    "cat" : "Imagine that, to swallow a cat!",
    "dog" : "What a hog, to swallow a dog!",
    "goat" : "Just opened her throat and swallowed a goat!",
    "cow" : "I dont know how she swallowed a cow!"
}

dict_verse = {
    "fly" : "I dont know why she swallowed the fly. Perhaps she'll die.",
    "spider" : "She swallowed the spider to catch the fly.",
    "bird" : "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
    "cat" : "She swallowed the cat to catch the bird.", 
    "dog" : "She swallowed the dog to catch the cat.",
    "goat" : "She swallowed the goat to catch the dog.",
    "cow" : "She swallowed the cow to catch the goat.",
    "horse" : "I know an old lady who swallowed a horse. She's dead of course!"
}

verse = []

##############################################################################


def first_line(animal):
    print("I know an old lady who swallowed a " + animal + ".")

def second_line(animal):
    print(dict_second_line[animal])

def format(listed_verses):
    for animal in listed_verses:
        print(dict_verse[animal])
    print("")

#################################

def setup():
    print("")
    print("")
    print("")

def intro(animal):
    verse.insert(0,animal)
    format(verse)

def stanza(animal):
    first_line(animal)
    second_line(animal)
    verse.insert(0,animal)
    format(verse)

def finish(animal):
    print(dict_verse[animal])

#################################

def recite_poem():
    setup()
    intro("fly")
    stanza("spider")
    stanza("bird")
    stanza("cat")
    stanza("dog")
    stanza("goat")
    stanza("cow")
    finish("horse")

################################################################################

recite_poem()