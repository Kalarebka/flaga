import json
import wikipedia as wiki

wiki.set_lang("pl")

def character_lookup(name):
    description = wiki.summary(name, sentences=6)
    return description

name_list = ['Arystoteles', 'Freddie Mercury', 'Tolkien', 'Lady Gaga', 'Wittgenstein', 'Władysław Łokietek', 'Maria Konopnicka', 'Alan Turing', 'Grzegorz Świetlicki', 'Jan Kochanowski', 'Martin Luther King']

character_list = []
for character in name_list:
    description = character_lookup(character)
    character_list.append([character, description, len(description), len(description.split(' '))])

with open('../dane/characters.json', 'w') as f:
    json.dump(character_list, f)
