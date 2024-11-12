#My exceeding of requirements was met by adding a get_adverb function in lines 52 - 56


import random
def main():
   print(make_sentence(1, 'past'))
   print(make_sentence(1, 'present'))
   print(make_sentence(1, 'future'))
   print(make_sentence(2, 'past'))
   print(make_sentence(2, 'present'))
   print(make_sentence(2, 'future'))


def get_determiner(quantity):

  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]

  word = random.choice(words)
  return word


def get_noun(quantity):
  
  if quantity == 1:
     words = [ "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
  else:
     words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

  word = random.choice(words)
  return word


def get_verb(quantity, tense):
  
  if tense == 'past':
     words = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
  elif tense == 'present':
     if quantity == 1:
        words = [ "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
     else:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  elif tense == 'future':
     words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

  word = random.choice(words)
  return word


def get_adverb():
   words = ['amazingly', 'beautifully', 'carefully', 'darkly', 'eagerly',
   'quickly', 'hesitantly',]
   word = random.choice(words)
   return word

def get_preposition():
   words = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
   word = random.choice(words)
   
   
   return word

def get_prepositional_phrase(quantity):
   if quantity == 1:
      prep_phrase = [get_preposition(), get_determiner(1), get_noun(1)]
      new_prep_phrase = " ".join(map(str, prep_phrase))
   else:
      prep_phrase = [get_preposition(), get_determiner(2), get_noun(2)]
      new_prep_phrase = " ".join(map(str, prep_phrase))
    

   return new_prep_phrase






def make_sentence(quantity, tense):
   if quantity == 1:
      sentence = [get_determiner(1), get_noun(1), get_verb(1, tense), get_adverb(), get_prepositional_phrase(1)]
      new_sentence = " ".join(map(str, sentence)).capitalize() + '.'
   else:
      sentence = [get_determiner(2), get_noun(2), get_verb(2, tense), get_adverb(), get_prepositional_phrase(2)]
      new_sentence = " ".join(map(str, sentence)).capitalize() + '.'
   
   return new_sentence



main()



     
