import json

def load_quotes(path='quotes.json'):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)
        
def filter_by_lang(quotes, lang):
    return [q for q in quotes if q['lang'] == lang]
