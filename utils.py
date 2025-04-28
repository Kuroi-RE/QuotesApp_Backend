import json

def filter_by_lang(quotes, lang):
    return [q for q in quotes if q['lang'] == lang]
