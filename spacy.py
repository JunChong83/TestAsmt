import spacy

#from spacy.lang.en import English

nlp = spacy.load('en_core_web_sm')
#nlp = English()

doc = nlp("In 1990, more than 60% of people in East Asia were in extreme poverty. Now less than 4% are.")

# Iterate over the tokens in the doc
# for token in doc:
#     print(token.text, token.pos_, token.dep_, token.head.text)
#     # Check if the token resembles a number
#     if token.like_num:
#         # Get the next token in the document
#         next_token = doc[token.i + 1]
#         # Check if the next token's text equals '%'
#         if next_token.text == '%':
#             print('Percentage found:', token.text)

for ent in doc.ents:
  print(ent.text, ent.label_)