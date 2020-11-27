import nltk

print(nltk.corpus.gutenberg.fileids())

output = [
    "austen-emma.txt",
    "austen-persuasion.txt",
    "austen-sense.txt",
    "bible-kjv.txt",
    "blake-poems.txt",
    "bryant-stories.txt",
    "burgess-busterbrown.txt",
    "carroll-alice.txt",
    "chesterton-ball.txt",
    "chesterton-brown.txt",
    "chesterton-thursday.txt",
    "edgeworth-parents.txt",
    "melville-moby_dick.txt",
    "milton-paradise.txt",
    "shakespeare-caesar.txt",
    "shakespeare-hamlet.txt",
    "shakespeare-macbeth.txt",
    "whitman-leaves.txt",
]
emma = nltk.corpus.gutenberg.words("austen-emma.txt")
print(emma)

emma_output = ["[", "Emma", "by", "Jane", "Austen", "1816", "]", ...]

print(len(emma))  # output 192427

emma = nltk.Text(nltk.corpus.gutenberg.words("austen-emma.txt"))
print(emma)  # output <Text: Emma by Jane Austen 1816>

print(emma.concordance("surprize"))

output_surprize = """Displaying 25 of 37 matches:
er father , was sometimes taken by surprize at his being still able to pity ` 
hem do the other any good ." " You surprize me ! Emma must do Harriet good : a
Knightley actually looked red with surprize and displeasure , as he stood up ,
r . Elton , and found to his great surprize , that Mr . Elton was actually on 
d aid ." Emma saw Mrs . Weston ' s surprize , and felt that it must be great ,
father was quite taken up with the surprize of so sudden a journey , and his f
y , in all the favouring warmth of surprize and conjecture . She was , moreove
he appeared , to have her share of surprize , introduction , and pleasure . Th
ir plans ; and it was an agreeable surprize to her , therefore , to perceive t
talking aunt had taken me quite by surprize , it must have been the death of m
f all the dialogue which ensued of surprize , and inquiry , and congratulation
 the present . They might chuse to surprize her ." Mrs . Cole had many to agre
the mode of it , the mystery , the surprize , is more like a young woman ' s s
 to her song took her agreeably by surprize -- a second , slightly but correct
" " Oh ! no -- there is nothing to surprize one at all .-- A pretty fortune ; 
t to be considered . Emma ' s only surprize was that Jane Fairfax should accep
of your admiration may take you by surprize some day or other ." Mr . Knightle
ation for her will ever take me by surprize .-- I never had a thought of her i
 expected by the best judges , for surprize -- but there was great joy . Mr . 
 sound of at first , without great surprize . " So unreasonably early !" she w
d Frank Churchill , with a look of surprize and displeasure .-- " That is easy
; and Emma could imagine with what surprize and mortification she must be retu
tled that Jane should go . Quite a surprize to me ! I had not the least idea !
 . It is impossible to express our surprize . He came to speak to his father o
g engaged !" Emma even jumped with surprize ;-- and , horror - struck , exclai
None"""

from nltk.corpus import gutenberg

file_ids = gutenberg.fileids()
print(file_ids)
emma = gutenberg.words("austen-emma.txt")

# short program to display other information about each text

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(
        round(num_chars / num_words),  # average word length
        round(num_words / num_sents),  # average sentence length
        round(
            num_words / num_vocab
        ),  # number of times each vocabulary item appears in the text on average -- our lexical diversity score
        fileid,
    )
"""
result of the for loop
5 25 26 austen-emma.txt
5 26 17 austen-persuasion.txt
5 28 22 austen-sense.txt
4 34 79 bible-kjv.txt
5 19 5 blake-poems.txt
4 19 14 bryant-stories.txt
4 18 12 burgess-busterbrown.txt
4 20 13 carroll-alice.txt
5 20 12 chesterton-ball.txt
5 23 11 chesterton-brown.txt
5 18 11 chesterton-thursday.txt
4 21 25 edgeworth-parents.txt
5 26 15 melville-moby_dick.txt
5 52 11 milton-paradise.txt
4 12 9 shakespeare-caesar.txt
4 12 8 shakespeare-hamlet.txt
4 12 7 shakespeare-macbeth.txt
5 36 12 whitman-leaves.txt
"""

macbeth_sentences = gutenberg.sents("shakespeare-macbeth.txt")
print(macbeth_sentences)

macbeth_output = [
    [
        "[",
        "The",
        "Tragedie",
        "of",
        "Macbeth",
        "by",
        "William",
        "Shakespeare",
        "1603",
        "]",
    ],
    ["Actus", "Primus", "."],
    ...,
]

print(macbeth_sentences[1116])
macbeth1116 = [
    "Double",
    ",",
    "double",
    ",",
    "toile",
    "and",
    "trouble",
    ";",
    "Fire",
    "burne",
    ",",
    "and",
    "Cauldron",
    "bubble",
]

longest_len = max(len(s) for s in macbeth_sentences)
print(longest_len)  # 158

longest_sentence = [s for s in macbeth_sentences if len(s) == longest_len]
print(longest_sentence)
sentence_list = [
    [
        "Doubtfull",
        "it",
        "stood",
        ",",
        "As",
        "two",
        "spent",
        "Swimmers",
        ",",
        "that",
        "doe",
        "cling",
        "together",
        ",",
        "And",
        "choake",
        "their",
        "Art",
        ":",
        "The",
        "mercilesse",
        "Macdonwald",
        "(",
        "Worthie",
        "to",
        "be",
        "a",
        "Rebell",
        ",",
        "for",
        "to",
        "that",
        "The",
        "multiplying",
        "Villanies",
        "of",
        "Nature",
        "Doe",
        "swarme",
        "vpon",
        "him",
        ")",
        "from",
        "the",
        "Westerne",
        "Isles",
        "Of",
        "Kernes",
        "and",
        "Gallowgrosses",
        "is",
        "supply",
        "'",
        "d",
        ",",
        "And",
        "Fortune",
        "on",
        "his",
        "damned",
        "Quarry",
        "smiling",
        ",",
        "Shew",
        "'",
        "d",
        "like",
        "a",
        "Rebells",
        "Whore",
        ":",
        "but",
        "all",
        "'",
        "s",
        "too",
        "weake",
        ":",
        "For",
        "braue",
        "Macbeth",
        "(",
        "well",
        "hee",
        "deserues",
        "that",
        "Name",
        ")",
        "Disdayning",
        "Fortune",
        ",",
        "with",
        "his",
        "brandisht",
        "Steele",
        ",",
        "Which",
        "smoak",
        "'",
        "d",
        "with",
        "bloody",
        "execution",
        "(",
        "Like",
        "Valours",
        "Minion",
        ")",
        "caru",
        "'",
        "d",
        "out",
        "his",
        "passage",
        ",",
        "Till",
        "hee",
        "fac",
        "'",
        "d",
        "the",
        "Slaue",
        ":",
        "Which",
        "neu",
        "'",
        "r",
        "shooke",
        "hands",
        ",",
        "nor",
        "bad",
        "farwell",
        "to",
        "him",
        ",",
        "Till",
        "he",
        "vnseam",
        "'",
        "d",
        "him",
        "from",
        "the",
        "Naue",
        "toth",
        "'",
        "Chops",
        ",",
        "And",
        "fix",
        "'",
        "d",
        "his",
        "Head",
        "vpon",
        "our",
        "Battlements",
    ]
]

longest_sentence = " ".join(longest_sentence[0])
print(longest_sentence)

# Doubtfull it stood , As two spent Swimmers , that doe cling together , And choake their Art : The mercilesse Macdonwald ( Worthie to be a Rebell , for to that The multiplying Villanies of Nature Doe swarme vpon him ) from the Westerne Isles Of Kernes and Gallowgrosses is supply ' d , And Fortune on his damned Quarry smiling , Shew ' d like a Rebells Whore : but all ' s too weake : For braue Macbeth ( well hee deserues that Name ) Disdayning Fortune , with his brandisht Steele , Which smoak ' d with bloody execution ( Like Valours Minion ) caru ' d out his passage , Till hee fac ' d the Slaue : Which neu ' r shooke hands , nor bad farwell to him , Till he vnseam ' d him from the Naue toth ' Chops , And fix ' d his Head vpon our Battlements

