''' Implementation of transcription text parser that transforms text based on certain phrases '''

def transcribe(text):
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
for count, point in enumerate(y):
  print(str(index+count) +'. '+ point.capitalize())

  