import os
import markovify

def main():

  learned_data = "learned_data.json"

  if os.path.exists(learned_data):
    with open(learned_data) as f:
      text_model = markovify.Text.from_json(f.read())
  else:
    print("no learned data.")
    exit()

#  sentence = text_model.make_short_sentence(140, tries=10, max_overlap_ratio=0.1, max_overlap_total = 3)
#  print(str(len(sentence)) + ":" + ''.join(sentence.split()))

  sentence = text_model.make_short_sentence(
      130, max_overlap_ratio=0.5, tries=30)
  print(''.join(sentence.split()))


  if len(sentence) > 20:
    # save sentences which are *not* shorter than 20  words. 
    with open('malkov_sentences.txt', 'a', encoding = 'UTF-8') as f:
        f.write(''.join(sentence.split()) + "\n")
  else:
    print("canceled due to very short sentence.")


if __name__ == '__main__':
  for var in range(0,100):
    main()
