#!/usr/bin/env python3

# add your code in this file
import os, sys, json, pickle
# ntz 
# ntz has four commands.
# [r]emember: calls a category you want to see DONE 
# [-c] creates or appends to a category (add a note to the category)  done?
# [f]orget a note DONE  
# [e]dit a note DONE
# clear

# the sys module provides access to 

# main function

def remember():
  pass
  

def add_category(note_dict, category_to_add):
  note_dict[category_to_add] = {}

def add_note(note_dict, category, note_name, note_to_add):
  print('note_dict: ',note_dict)
  if category in note_dict.keys():
    print('yes I am in your keys')
    note_dict[category][note_name] = note_to_add
  else:
    print('Your category is not available')
    return


def edit_note(note_dict, category, note_name, updated_note):
  if category not in note_dict.keys():
    print('The note you want to edit\'s category does not exist')
  elif category in note_dict.keys() and note_name not in note_dict[category].keys():
    print('The note you want to edit\'s category does exist, but the note name does not')
  elif category in note_dict.keys() and note_name in note_dict[category].keys():
    del note_dict[category][note_name]
    note_dict[category][note_name] = updated_note
  return
  

def forget_note(note_dict, category, note_name):
  if category not in note_dict.keys():
    print('Your category does not exist')
  elif category in note_dict and note_name not in note_dict[category].keys():
    print('Your category exists but your note name does not')
  elif category in note_dict and note_name in note_dict[category].keys():
    del note_dict[category][note_name]
  return


def forget_category(note_dict, category):
  if category not in note_dict.keys():
    print('Your category to delete does not exist')
  else:
    del note_dict[category]


def remember(note_dict, category):
  info = ''
  info +=  'Category Recalled - ' + category + '\n' + 'Note(s) Recalled - \n'
  for line in note_dict[category]:
    info += line + ': ' + note_dict[category][line] + '\n'
  print(info)

def load_json():
  with open ('/Users/sean/labs/ntzsave.json', 'r') as f:

    dict_convert = json.load(f)
    #print(dict_convert)
    return dict_convert


def dump_json(dict_to_dump):
   with open('/Users/sean/labs/ntzsave.json', 'w') as f:
     dumped = json.dump(dict_to_dump, f)
     return dumped

def read_file(file):
  final_output = ''
  for key in file:
    final_output += 'Category - ' + str(key) + ': ' + '\n\n'
    for index in file[key]:
      final_output += str(index) + ': ' + str(file[key][index]) + '\n\n'
  print(final_output)


#dump_json()
#read_file()

def cli():
  # check command line for what decision you want, then you ahve funcs for each one and then call the function
  latest_notes = load_json()
  if len(sys.argv) == 1:
    read_file(latest_notes)
  elif sys.argv[1] == 'r' and len(sys.argv) == 3:
    remember(latest_notes, sys.argv[2])

  elif sys.argv[1] == '-c':
    if len(sys.argv) == 3: 
      add_category(latest_notes, sys.argv[2])
    elif len(sys.argv) == 5:
      'this is called'
      add_note(latest_notes, sys.argv[2], sys.argv[3], sys.argv[4])

  elif sys.argv[1] == 'f':
    if len(sys.argv) == 3:
      forget_category(latest_notes, sys.argv[2])
    elif len(sys.argv) == 4:
      forget_note(latest_notes, sys.argv[2], sys.argv[3])
  
  elif sys.argv[1] == 'e':
    if len(sys.argv) == 5:
      edit_note(latest_notes, sys.argv[2], sys.argv[3], sys.argv[4])
    

  
  
  #print(latest_notes)
  dump_json(latest_notes)
  read_file(latest_notes)
  '''
  if arg
  if input == 'r':
    pass
  '''







if __name__ == '__main__':
  cli()