



# list not actually being used anywhere
# might try to use to create loop for stanza function 
# but would likely have to rework dictionary entries and exceptional phrases at intro and finish
things_she_ate = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

# dictionary for second line of each phrase
dict_second_line = {
    "spider" : "It wriggled and jiggled and tickled inside her.",
    "bird" : "How absurd to swallow a bird.",
    "cat" : "Imagine that, to swallow a cat!",
    "dog" : "What a hog, to swallow a dog!",
    "goat" : "Just opened her throat and swallowed a goat!",
    "cow" : "I dont know how she swallowed a cow!"
}

# dictionary for repeated verses
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
# define empty list that repeating verses will be added to the front of
verse = []

##############################################################################

# print first line of each phrase     ("string")
def first_line(animal):
    print("I know an old lady who swallowed a " + animal + ".")

#print second line of each phrase     (use "key" to call entry from dict_second_line)
def second_line(animal):
    print(dict_second_line[animal])

# print  list of accumulated verses and a blank line
def format(listed_verses):
    for animal in listed_verses:
        print(dict_verse[animal])
    print("")

#################################

# prints three blank lines so poem isnt squished up against other stuff in terminal
def setup():
    print("")
    print("")
    print("")

# adds first animal to front of empty new list and prints it     
# this phrase gets special treatment because first is different
def intro(animal):
    verse.insert(0,animal)
    format(verse)

# prints phrases that follow a repeatable pattern    call with  "string" that is same as corresponding dictionary keys
# first line, print second line, adds relevant line to repeating verse list, print repeating verses list
def stanza(animal):
    first_line(animal)
    second_line(animal)
    verse.insert(0,animal)
    format(verse)

# prints last phrase     because its different      call with key from dict_verse
def finish(animal):
    print(dict_verse[animal])

##########################
# arranges poem elements together in order
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

############################################################################

# calling this function makes everything
recite_poem()

