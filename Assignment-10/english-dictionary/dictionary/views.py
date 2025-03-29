from django.shortcuts import render
from PyDictionary import PyDictionary
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def word(request):
#     search = request.GET.get('search')
#     dictionary = PyDictionary()
#     meaning = dictionary.meaning(search)
#     synonyms = dictionary.synonym(search)
#     antonyms = dictionary.antonym(search)
#     context = {
#         'meaning': meaning['Noun'][0],
#         'synonyms': synonyms,
#         'antonyms': antonyms
#     }
#     return render(request, 'word.html',  context)

# def word(request):
#     search = request.GET.get('search', '')

#     if not search:
#         return render(request, 'word.html', {'word': '', 'meaning': "No word entered"})

#     url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{search}"
#     response = requests.get(url)

#     print(f"API URL: {url}")  # Debugging step
#     print(f"Response Status Code: {response.status_code}")
    
#     if response.status_code == 200:
#         data = response.json()
#         print("API Response:", data)  # Debugging step

#         if isinstance(data, list) and data:
#             meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
#         else:
#             meaning = "Meaning not available"
#     else:
#         meaning = "Word not found"

#     context = {
#         'word': search,
#         'meaning': meaning,
#         'synonyms': ["Synonyms not available"],
#         'antonyms': ["Antonyms not available"]
#     }
#     return render(request, 'word.html', context)
from django.shortcuts import render
import requests

def word(request):
    search = request.GET.get('search', '').strip()

    if not search:
        return render(request, 'word.html', {'word': '', 'meaning': "No word entered"})

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{search}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if not data or not isinstance(data, list):
            context = {'word': search, 'meaning': "Word not found", 'synonyms': [], 'antonyms': []}
            return render(request, 'word.html', context)

        meanings = data[0].get("meanings", [])
        
        if meanings:
            meaning = meanings[0]["definitions"][0].get("definition", "Meaning not available")
        else:
            meaning = "Meaning not available"

        synonyms = set()
        antonyms = set()

        for meaning_data in meanings:
            # Extract synonyms/antonyms from meanings
            synonyms.update(meaning_data.get("synonyms", []))
            antonyms.update(meaning_data.get("antonyms", []))

            # Extract from each definition
            for definition in meaning_data.get("definitions", []):
                synonyms.update(definition.get("synonyms", []))
                antonyms.update(definition.get("antonyms", []))

        # Convert to list & handle missing values
        synonyms = list(synonyms) if synonyms else ["Synonyms not available"]
        antonyms = list(antonyms) if antonyms else ["Antonyms not available"]

        context = {
            'word': search,
            'meaning': meaning,
            'synonyms': synonyms,
            'antonyms': antonyms
        }
    else:
        context = {
            'word': search,
            'meaning': "Word not found",
            'synonyms': ["Synonyms not available"],
            'antonyms': ["Antonyms not available"]
        }

    return render(request, 'word.html', context)
