''' Implementation of transcription text parser that transforms text based on certain phrases '''

import re 

text = "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit. Number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn't improved for last 4 weeks."

# match = re.search("Number", text)

# print(match.start(), match.end())

# numberN = r"\['Number']"
# bullets = re.split(numberN, text)

x = text.split("Number ", 1)
bulletpoint = x[1]
number = bulletpoint.split(' ')[0].lower()

if number == 'one':
  index = 1
elif number == 'two':
  index = 2
elif number == 'three':
  index = 3;
elif number == 'four':
 index = 4;
elif number == 'five':
   index = 5;
elif number == 'six':
 index = 6;
elif number == 'seven':
  index = 7;
elif number == 'eight':
 index = 8;
elif number == 'nine':
  index = 9;

y = bulletpoint.split("Number next ")

print(x[0])
for count, points in enumerate(y):
  print(str(index+count) +'. '+ points)
