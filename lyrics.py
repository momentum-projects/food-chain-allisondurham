








fly = "I dont know why she swallowed the fly. Perhaps she'll die."
spider = "She swallowed the spider to catch the fly."
bird = "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
cat = "She swallowed the cat to catch the bird." 
dog = "She swallowed the dog to catch the bird."
goat = "She swallowed the goat to catch the dog."
cow = "She swallowed the cow to catch the goat."
horse = "I know an old lady who swallowed a horse. She's dead of course!"

def intro(animal):
    print("I know an old lady who swallowed a " + animal + ".")
    
def format(verse):
    print("")
    for line in verse:
        print(line)


intro('spider')
# => I know an uld lady who swallowed a spider.


##########
# verse = []
# verse.insert(0,fly)
# format(verse)
# verse.insert(0,spider)
# format(verse)
# verse.insert(0,cat)
# format(verse)
# verse.insert(0,dog)
# format(verse)
# verse.insert(0,goat)
# format(verse)
# verse.insert(0,cow)





#verse(fly, spider, bird, cat, dog, goat, cow, horse)

#print (fly)
# lyric = (
#     f"{fly}"
#     f"{spider}"
#     f"{bird}"
# )
# print(lyric)

# f"{fly} {spider} {bird}"

#repeated = {"fly" : "I dont know why she swallowed the fly.  Perhaps she'll die.", "spider" : "She swallowed the spider to catch the fly.", "bird" : "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.", "cat" : "She swallowed the cat to catch the bird.", "dog" : "She swallowed the dog to catch the cat.", "goat" : "She swallowed the goat to catch the dog.", "cow" : "She swallowed the cow to catch the goat."}
# "hello, {fly} {spider} {bird}".format(**repeated)

# i know an old lady who swallowed a (variable).
# another line or two of rhyming text


#   ***  add one each time, but add to the front of list*** 

#She's dead, of course!"

# (new line for horse?)