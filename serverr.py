from flask import Flask, request, jsonify
import nltk
import spacy
from textblob import TextBlob
from nltk.corpus import stopwords, wordnet
import random

# Télécharger les ressources NLP nécessaires
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Charger le modèle linguistique français de spaCy
nlp = spacy.load("fr_core_news_sm")

app = Flask(__name__)

def get_synonym(word):
    """ Trouve un synonyme en français. """
    synonyms = wordnet.synsets(word, lang='fra')
    if synonyms:
        return random.choice(synonyms).lemmas()[0].name()
    return word

def reformulate_text(text, style):
    """ Applique des variations stylistiques au texte. """
    if style == "formel":
        return text.replace("très", "particulièrement").replace("c'est", "cela constitue")

    elif style == "poetique":
        return text.replace("important", "essentiel comme l'air que l'on respire").replace("idée", "pensée qui danse au gré du vent")

    elif style == "journalistique":
        return "Selon nos sources, " + text + ". Cette déclaration soulève des questions sur son impact futur."

    elif style == "juridique":
        return "Conformément aux dispositions en vigueur, " + text + ", sous réserve d'interprétation jurisprudentielle."

    elif style == "informel":
        return text.replace("c'est", "c'est genre").replace("important", "super important")

    return text

def improve_text(text, style):
    """ Génère plusieurs versions du texte en fonction du style. """
    drafts = []
    drafts.append(f"🔹 **Brouillon initial :** {text}")

    words = nltk.word_tokenize(text, language="french")
    filtered_words = [word for word in words if word.lower() not in stopwords.words('french')]
    draft1 = " ".join(filtered_words)
    drafts.append(f"🔹 **Première révision (plus concise) :** {draft1}")

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    draft2 = " ".join(sentences[::-1]) 
    drafts.append(f"🔹 **Deuxième révision (réorganisation) :** {draft2}")

    draft3 = " ".join([get_synonym(word) if len(word) > 4 else word for word in words])
    drafts.append(f"🔹 **Troisième révision (vocabulaire enrichi) :** {draft3}")

    draft4 = reformulate_text(text, style)
    drafts.append(f"🔹 **Quatrième révision ({style}) :** {draft4}")

    return drafts

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get("text", "").strip()
    style = data.get("style", "formel")

    if not text:
        return jsonify({"error": "Le texte ne peut pas être vide."}), 400

    drafts = improve_text(text, style)
    return jsonify({"drafts": drafts})

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/generate', methods=['POST'])
def generate():
    print("✅ Requête reçue dans Flask")  # LOG
    data = request.json
    print("🔹 Données reçues :", data)  # LOG
    
    text = data.get("text", "").strip()
    style = data.get("style", "formel")
    
    if not text:
        print("❌ Erreur : Le texte est vide")
        return jsonify({"error": "Le texte ne peut pas être vide."}), 400
    
    drafts = improve_text(text, style)
    
    print("✅ Réponse générée, envoi au client")  # LOG
    return jsonify({"drafts": drafts})
