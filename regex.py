text = "Natural language processing has its roots in the 1950s. \
Already in 1950, Alan Turing published an article titled \"Computing Machinery \
and Intelligence\" which proposed what is now called the Turing test as a criterion \
of intelligence, a task that involves the automated interpretation and generation of \
 natural language, but at the time not articulated as a problem separate from artificial intelligence."

import re

sentence_endings = r"[.?!]"

print(re.split(sentence_endings, text))

capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, text))

spaces = r"\s+"
print(re.split(spaces, text))

digits = r"\d+"
print(re.findall(digits, text))

import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

sentences = sent_tokenize(text)
print(len(sentences), 'sentences:', sentences)

from nltk.tokenize import word_tokenize

tokenized_sent = word_tokenize(sentences[1])
unique_tokens = set(word_tokenize(text))
print(unique_tokens)

match = re.search("from", text)
print(match.start(), match.end())

pattern1 = r"\[.*\]"
print(re.search(pattern1, text))

pattern2 = r"[\w\s]+:"
print(re.search(pattern1, text))

from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

pattern3 = r"#\w+"

hashtags = regexp_tokenize(text, pattern3)
print(hashtags)