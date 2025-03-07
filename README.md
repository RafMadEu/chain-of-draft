Chain of Draft (Multistyle) 📝✨

🚀 **Un outil de reformulation automatique de texte en plusieurs styles**  
📍 **100% local et gratuit** – Pas besoin d'API payante, fonctionne en **Python (Flask, NLTK, spaCy, TextBlob)** avec une interface web.  

 🔹 Fonctionnalités :
✅ Reformulation automatique en **plusieurs styles** :  
   - 📌 Formel → Style professionnel et structuré  
   - 🎭 Poétique → Style créatif et imagé  
   - 📰 Journalistique → Style informatif et impactant  
   - ⚖ Juridique → Style légal et argumenté  
   - 💬 Informel → Style naturel et détendu  
✅ Interface web simple en HTML + JavaScript 
✅ Traitement du texte avec NLP (spaCy, NLTK, TextBlob)
✅ Stockage possible en `.txt`, `.csv` ou base SQLite  
✅ 100% Open Source & Offline

---

## 🔹 Comment l'utiliser ?
### **1️⃣ Installation des dépendances**
Avant de lancer le projet, installe les bibliothèques nécessaires :

bash

pip install flask nltk spacy textblob
python -m spacy download fr_core_news_sm
python -m textblob.download_corpora

2️⃣ Lancer le serveur

python server.py

✅ Flask démarre sur http://127.0.0.1:5000/

3️⃣ Ouvrir l'interface web
📂 Ouvre index.html dans un navigateur
✍ Écris un texte et choisis un style
🚀 Clique sur "Prompt" et admire la reformulation !

📌 Exemple d'utilisation
Avant (texte original) :

Mon chat est très intelligent et il comprend beaucoup de choses.

Après reformulation selon les styles :

Formel → "Mon félin démontre des capacités cognitives avancées et une compréhension étendue."
Poétique → "Mon chat, tel un sage, perçoit les mystères du monde dans un doux murmure."
Journalistique → "Selon plusieurs sources, les chats posséderaient une intelligence insoupçonnée."
Juridique → "Conformément aux études en éthologie, il est établi que certains félins présentent une acuité intellectuelle remarquable."
Informel → "Franchement, mon chat capte tout, c'est un vrai génie poilu !"

⚡ Améliorations possibles
💡 Ajout d’un mode GPT-like en local
💡 Option pour enregistrer l’historique des prompts
💡 Interface plus avancée avec Bootstrap ou Tailwind CSS

🔥 Contribuer
Tu peux proposer des améliorations via des Issues ou des Pull Requests sur GitHub !
Toutes les contributions sont les bienvenues.

📜 Licence
🔓 Ce projet est Open Source et libre d'utilisation.


