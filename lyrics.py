








fly = "I dont know why she swallowed the fly. Perhaps she'll die."
spider = "She swallowed the spider to catch the fly."
bird = "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
cat = "She swallowed the cat to catch the bird." 
dog = "She swallowed the dog to catch the bird."
goat = "She swallowed the goat to catch the dog."
cow = "She swallowed the cow to catch the goat."
horse = "I know an old lady who swallowed a horse. She's dead of course!"

u_spider = "It wriggled and jiggled and tickled inside her."
u_bird = "How absurd to swallow a bird."
u_cat = "Imagine that, to swallow a cat!"
u_dog = "What a hog, to swallow a dog!"
u_goat = "Just opened her throat and swallowed a goat!"
u_cow = "I dont know how she swallowed a cow!"


def first_line(animal):
    print("I know an old lady who swallowed a " + animal + ".")
    
def second_line(u_animal):
    print(u_animal)

def format(verse):
    for line in verse:
        print(line)
    print("")


#first_line('spider')
# => I know an uld lady who swallowed a spider.


##########
print("")
print("")
print("")
verse = []
verse.insert(0,fly)
format(verse)

first_line("spider")
second_line(u_spider)
verse.insert(0,spider)
format(verse)

first_line("cat")
second_line(u_cat)
verse.insert(0,cat)
format(verse)

first_line("dog")
second_line(u_dog)
verse.insert(0,dog)
format(verse)

first_line("goat")
second_line(u_goat)
verse.insert(0,goat)
format(verse)

first_line("cow")
second_line(u_cow)
verse.insert(0,cow)
format(verse)

print(horse)





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