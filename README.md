## 100DaysOfCode with Machine Learning

#### Start: November 23, 2020

##### My Goals:

- don't be hard on myself
- code/learn everyday a bit
- focus mostly on Natural Language Processing

### Day 6: November 30, 2020

**Plans for Today:**

- one video from Coursera
- or some reading of chapter 2 NLP with Python

**Today's Progress:**

- Almost finished week 1 of Coursera Python Text Mining. Started doing a programming assignment even though I won't be able to submit it, because I need to purchase a subscription first. (but I won't)

**Thoughts:**

- The assignment is a bit problematic. I think I need to spend more time learning Regex. The exercise is about extracting dates from a lot of data and then sorting the dates. I started using one regex pattern, now need to think about a clean way of using more date patterns.

* I think I need to start the Coursera specialization from the beginning. I need to learn pandas first, I suppose to do some of the exercises.

**Link to work:**

**Plans for tomorrow:**

- Learn more about Regex and try to finish the assignment from Coursera.
- Start Introduction to Data Science in Python

**Resources:**

- https://www.coursera.org/learn/python-data-analysis/home/welcome

* https://docs.python.org/3/library/re.html#

### Day 5: November 28, 2020

**Plans for Today:**

- continue reading chapter 2 of NLP with Python

**Today's Progress:**

- read 1.3 and 1.4 of chapter 2 - The Brown Corpus and The Reuters Corpus.
- watched a video about Regex from Coursera and read and rewrite code from a part about Regex

**Thoughts:**
Regex is a bit problematic ;-)

**Link to work:**

**Plans for tomorrow:**

- one video from Coursera
- or some reading of chapter 2 NLP with Python

**Resources:**

### Day 4: November , 2020

**Plans for Today:**

- start chapter 2

**Today's Progress:**

- started part 1 of ch2 - Accessing Text Corpora (Gutenberg Corpus)

**Thoughts:**
Pretty interesting but started working on it quite late at night

**Link to work:**
https://github.com/maknetaRo/100days-ml/blob/main/exercises/chapter2.py

**Plans for tomorrow:**

- continue Text Corpora part

**Resources:**
https://www.nltk.org/book/ch02.html

### Day 3: November 26 , 2020

**Plans for Today:**

- finish chapter 1

**Today's Progress:**

- finished chapter 1 with exercises

Notes:

- A **collocation** is a sequence of words that occur together unusually often.

```
list(bigrams(["more", "is", "said", "than", "done"])) // checks pairs of words
.collocations() // frequent bigrams

fdist.max()
fdist.freq('monstrous') // frequency of a given sample
fdist.N() // total number of samples
fdist1 |= fdist2 // update fdist1 with counts from fdist2
```

**Thoughts:**
Coding is the easier part of the NLP. That's true, that thinking about the problem should go first.

**Link to work:**

**Plans for tomorrow:**

- at least one video on Coursera

**Resources:**

### Day 2: November 24, 2020

**Plans for Today:**

- continue the first chapter of NLP book
  or/and
- at least one video on Coursera

**Today's Progress:**

- read to part 3.3 NLP with Python Chapter 1 - started learning about Frequency Distributions

```
// FreqDist - built-in support
fdist1 = FreqDist(text1)
fdist1.most_common(50) // finds 50 the most common worlds
fdist1["whale"] // finds how many times the word is in the text

fdist1.plot(50, cumulative=True) // chart to show the frequency of the most common words

fdist1.hapaxes() // finds the rare words

// how to find words that are more than 15 characters long
[w for w in V if len(w) > 15]

// find words that are more than 7 characters long and they are repeated in text more than 7 times
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)
```

**Thoughts:**

- Today I've been a bit tired. I skimmed through the Python lists, slicing and strings.

**Link to work:**

**Plans for tomorrow:**

- continue chapter 1

**Resources:**
https://www.nltk.org/book/ch01.html#:~:text=Once%20you've%20installed%20NLTK,collection%20as%20shown%20in%201.1.&text=Figure%201.1%3A%20Downloading%20the%20NLTK,the%20available%20packages%20using%20nltk

### Day 1: November 23, 2020

**Plans for Today:**

- check a few links & choose the most interesting

**Today's Progress:**

- started Applied Text Mining in Python course on Coursera & watched about half or the first week
- refreshed String Operations and Handling Larger Text in Python.

```
[ ] .istitle()
[ ] .endswith(char)  .startswidth(char)
[ ] .isupper()  .islower()  .istitle()
[ ] .isalpha()  .isdigit()  .isalnum()
[ ] .lower() .upper(); .titlecase()
[ ] .split(ch)
[ ] .join(ch)
[ ] .strip() .rstrip()
[ ] .find(ch) .rfind(ch)
[ ] .replace(u, v)
[ ] list(word) // to split characters in a word

// work with files
[ ] f = open('title.txt', 'r')
[ ] f.readline() // 1st line
[ ] f.seek(0) // reset the reading to start from the beginning
[ ] text = f.read()  // all text
[ ] text.splitlines()
[ ] f.write(message)
[ ] f.close()

// regular expressions
'@[A-Za-z0-9_]+' // will return all words that:
// - start with '@' and are followed for at least one:
// capital letter
// lowercase letter
// uppercase letter
// number
// or underscore

import re
[w for w in text if re.search('@[A-Za-z0-9_]+', w)]
```

- Started reading Natural Language Processing with Python (online) (example mostly from the book)

```
import nltk
nltk.download()
from nltk.book import *

text1.concordance("monstrous") // shows every occurance of a give word, together with some context

text1.similar("monstrous") // shows words that are used similarly in the text

tex1.common_contexts(["monstrous", "very]) // examines the contexts that are shared by two or more words

// first install matplotlib (for charts)
from matplotlib import pyplot as plt
text4.dispersion_plot(['citizens', 'democracy', 'freedom', 'duties', 'America'])
```

![nltk-dispersion-plot](images/nltk-dispersion-plot.png)

**Thoughts:**
So far so good. Old good Python. I'm always excited when I start something. I hope to go to day 100 with a few good projects.

**Link to work:**

**Plans for tomorrow:**

- continue the first chapter of NLP book
  or/and
- at least one video on Coursera

**Resources:**

- Coursera: https://www.coursera.org/learn/python-text-mining/home/week/1
- NLP with Python book: https://www.nltk.org/book/ch01.html#:~:text=Once%20you've%20installed%20NLTK,collection%20as%20shown%20in%201.1.&text=Figure%201.1%3A%20Downloading%20the%20NLTK,the%20available%20packages%20using%20nltk.

===========================================

### Reading List:

Book: Natural Language Processing with Python https://www.nltk.org/book/

1. https://www.upgrad.com/blog/natural-language-processing-nlp-projects-ideas-topics-for-beginners/
2. https://towardsdatascience.com/a-list-of-beginner-friendly-nlp-projects-using-pre-trained-models-dc4768b4bec0
3. https://medium.com/towards-artificial-intelligence/natural-language-processing-nlp-with-python-tutorial-for-beginners-1f54e610a1a0
4. https://medium.com/towards-artificial-intelligence/oh-hello-nlp-project-ideas-for-beginners-eec5c0061d5a
5. https://towardsdatascience.com/text-classification-in-python-dd95d264c802
6. https://www.reddit.com/r/Python/comments/4vaihz/beginner_nlp_project/
7. https://www.quora.com/What-are-some-really-interesting-NLP-projects-that-I-can-take-up

<!-- Template
### Day 0: August , 2019

**Plans for Today:**

**Today's Progress:**

**Thoughts:**

**Link to work:**

**Plans for tomorrow:**

**Resources:** -->
