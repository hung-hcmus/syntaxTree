import pickle
import re
import nltk
import os
from nltk.draw import TreeView
from PIL import Image

def extract_features(sentence, index):
  return {
      'word':sentence[index],
      'is_first':index==0,
      'is_last':index ==len(sentence)-1,
      'is_capitalized':sentence[index][0].upper() == sentence[index][0],
      'is_all_caps': sentence[index].upper() == sentence[index],
      'is_all_lower': sentence[index].lower() == sentence[index],
      'is_alphanumeric': int(bool((re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])',sentence[index])))),
      'prefix-1':sentence[index][0],
      'prefix-2':sentence[index][:2],
      'prefix-3':sentence[index][:3],
      'prefix-3':sentence[index][:4],
      'suffix-1':sentence[index][-1],
      'suffix-2':sentence[index][-2:],
      'suffix-3':sentence[index][-3:],
      'suffix-3':sentence[index][-4:],
      'prev_word':'' if index == 0 else sentence[index-1],
      'next_word':'' if index < len(sentence) else sentence[index+1],
      'has_hyphen': '-' in sentence[index],
      'is_numeric': sentence[index].isdigit(),
      'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
  }

def renderTreee(message):
  currentPath = os.path.dirname(__file__)
  filename = os.path.join(currentPath, "model.sav")
  penn_crf = pickle.load(open(filename, 'rb'))
  currentPath = os.path.join(currentPath, "static/images")

  for (dirpath, dirnames, filenames) in os.walk(currentPath):
    for filename in filenames:
      itemPath = os.path.join(dirpath, filename)
      os.remove(itemPath)  
      print(itemPath)
      
  sentence = message
  for i in range(len(sentence.split("."))):
    if sentence.split(".")[i] != "":
      sent = sentence.split(".")[i]
      features = [extract_features(sent.split(), idx) for idx in range(len(sent.split()))]

      penn_results = penn_crf.predict_single(features)

      penn_tups = [(sent.split()[idx], penn_results[idx]) for idx in range(len(sent.split()))]

      pattern = """NP: {<DT>?<JJ>*<NN>}
      VBD: {<VBD>}
      IN: {<IN>}
      """
      NPChunker = nltk.RegexpParser(pattern)
      result = NPChunker.parse(penn_tups)
      #path to file ps and png
      psPath  = os.path.join(currentPath, "tree" + str(i) + ".ps")
      pngPath = os.path.join(currentPath, "tree" + str(i) + ".png")
      #save file ps and convert to png
      TreeView(result)._cframe.print_to_file(psPath)
      with Image.open(psPath) as psimage:
        psimage.save(pngPath)
      os.remove(psPath)
  
  return penn_tups

