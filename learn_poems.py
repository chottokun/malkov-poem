# -*- coding:utf-8 -*-

import MeCab
import re
from glob import iglob
import re
import markovify
import os

def wakati(filename_wakati):

  Tagger = MeCab.Tagger("-Owakati")

  with open(filename_wakati) as infile, open("./data/poem-wakati.txt", "w") as outfile:
    for line in infile:
      line = Tagger.parse(line)
      outfile.write(line)
      print(line)


def main():

  learned_data = "learned_data.json"

  if os.path.exists(learned_data):
    with open(learned_data) as f:
      combined_model = markovify.Text.from_json(f.read())
  else:
    print("no learned data.")
    combined_model = None

  for (dirpath, _, filenames) in os.walk('./data'):
    for filename in filenames:
      if filename.lower().endswith('.txt'):
        with open(os.path.join(dirpath, filename)) as f:
          text_model = markovify.Text(f, retain_original=True, state_size=3)

          if combined_model:
            combined_model = markovify.combine(models=[combined_model, text_model], weights=[1.0,1.0])
          else:
            combined_model = text_model

        sentence = combined_model.make_sentence()
        print(''.join(sentence))

        with open(learned_data, 'w') as f:
          f.write(combined_model.to_json())
          print("saved: " + learned_data)

      #remove learned file.
#      os.remove(os.path.join(dirpath, filename))


if __name__ == '__main__':
  wakati('poem.txt')
  main()

