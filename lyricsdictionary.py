



key_first_line = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

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



def first_line(animal):
    print("I know an old lady who swallowed a " + animal + ".")
    
def second_line(animal):
    print(dict_second_line[animal])

def format(listed_verses):
    for animal in listed_verses:
        print(dict_verse[animal])
    print("")


# def stanza(key_first_line):
#     first_line(animal)
#     second_line(animal)
#     verse.insert(0,animal)
#     format(verse)



##########
print("")
print("")
print("")
verse = []
verse.insert(0,"fly")
format(verse)

# stanza("spider")

first_line("spider")
second_line("spider")
verse.insert(0,"spider")
format(verse)

first_line("bird")
second_line("bird")
verse.insert(0,"bird")
format(verse)

first_line("cat")
second_line("cat")
verse.insert(0,"cat")
format(verse)

first_line("dog")
second_line("dog")
verse.insert(0,"dog")
format(verse)

first_line("goat")
second_line("goat")
verse.insert(0,"goat")
format(verse)

first_line("cow")
second_line("cow")
verse.insert(0,"cow")
format(verse)

print(dict_verse["horse"])