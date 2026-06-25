# DecodeLabs - Project 1
# Etape 5 : La base de données

# Le dictionnaire = la "mémoire" du chatbot
RESPONSES = {
    "bonjour":      "Salut ! Comment puis-je t'aider ?",
    "salut":        "Hey ! Bienvenue chez DecodeLabs !",
    "comment tu vas": "Je fonctionne à 100% ! Merci de demander 😄",
    "c'est quoi l'ia": "L'IA, c'est enseigner à une machine à prendre des décisions !",
    "qui t'a créé":  "Un stagiaire DecodeLabs avec du Python pur !",
    "aide":         "Je connais : bonjour | salut | comment tu vas | aide | bye",
    "bye":          "À bientôt ! Continue à coder 🚀",
}

print("🤖 Chatbot démarré ! Tape 'exit' pour quitter.")
print(f"📚 Base de données chargée : {len(RESPONSES)} réponses\n")

while True:
    user_input = input("Toi: ")
    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        print("Bot: Au revoir !")
        break

    print(f"Bot: clé recherchée → '{clean_input}'")