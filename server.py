from flask import Flask, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import spacy
from textblob import TextBlob

app = Flask(__name__)

# Télécharger les ressources nécessaires de NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Charger le modèle de langue française de spaCy
nlp = spacy.load('fr_core_news_sm')

def improve_text(text, style):
    """
    Améliore le texte en fonction du style spécifié.
    """
    drafts = []

    # Version concise
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stopwords.words('french')]
    concise_text = ' '.join(filtered_words)
    drafts.append(f"🔹 **Version concise :** {concise_text}")

    # Réorganisation
    doc = nlp(text)
    sentences = list(doc.sents)
    if len(sentences) > 1:
        sentences.reverse()
        reorganized_text = ' '.join([sent.text for sent in sentences])
        drafts.append(f"🔹 **Réorganisation :** {reorganized_text}")
    else:
        drafts.append(f"🔹 **Réorganisation :** {text}")

    # Synonymes enrichis
    synonyms_text = []
    for word in words:
        synsets = wordnet.synsets(word, lang='fra')
        if synsets:
            lemmas = synsets[0].lemma_names('fra')
            if lemmas:
                synonyms_text.append(lemmas[0])
            else:
                synonyms_text.append(word)
        else:
            synonyms_text.append(word)
    enriched_text = ' '.join(synonyms_text)
    drafts.append(f"🔹 **Synonymes enrichis :** {enriched_text}")

    # Style spécifique
    if style == 'formel':
        formal_text = f"Selon nos observations, {text.lower()}."
        drafts.append(f"🔹 **Style formel :** {formal_text}")
    elif style == 'poétique':
        poetic_text = f"Dans le doux murmure du vent, {text.lower()}."
        drafts.append(f"🔹 **Style poétique :** {poetic_text}")
    elif style == 'journalistique':
        journalistic_text = f"D'après nos sources, {text.lower()}."
        drafts.append(f"🔹 **Style journalistique :** {journalistic_text}")
    elif style == 'juridique':
        legal_text = f"Conformément aux dispositions en vigueur, {text.lower()}."
        drafts.append(f"🔹 **Style juridique :** {legal_text}")
    elif style == 'informel':
        informal_text = f"Franchement, {text.lower()}."
        drafts.append(f"🔹 **Style informel :** {informal_text}")
    else:
        drafts.append(f"🔹 **Style inconnu :** {text}")

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
