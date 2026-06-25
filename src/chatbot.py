# DecodeLabs - Project 1
# Etape 6 : Version FINALE complète

# ============================
# LA BASE DE DONNÉES
# ============================
RESPONSES = {
    "bonjour":          "Salut ! Comment puis-je t'aider ?",
    "salut":            "Hey ! Bienvenue chez DecodeLabs !",
    "comment tu vas":   "Je fonctionne à 100% ! Merci de demander 😄",
    "c'est quoi l'ia":  "L'IA c'est enseigner à une machine à décider !",
    "qui t'a créé":     "Un stagiaire DecodeLabs avec du Python pur !",
    "aide":             "Je connais : bonjour | salut | comment tu vas | aide | bye",
    "bye":              "À bientôt ! Continue à coder 🚀",
}

# ============================
# FONCTION : NETTOYER L'INPUT
# ============================
def sanitize(text):
    return text.lower().strip()

# ============================
# FONCTION : TROUVER LA RÉPONSE
# ============================
def get_response(user_input):
    return RESPONSES.get(user_input, "❓ Je ne comprends pas. Tape 'aide' !")

# ============================
# LA BOUCLE PRINCIPALE
# ============================
print("🤖 Chatbot DecodeLabs démarré !")
print("📚 Réponses disponibles :", len(RESPONSES))
print("💡 Tape 'aide' pour voir les commandes\n")

while True:
    user_input = input("Toi: ")
    clean_input = sanitize(user_input)

    if clean_input == "exit":
        print("Bot: Arrêt du système. Au revoir ! 👋")
        break

    response = get_response(clean_input)
    print(f"Bot: {response}\n")