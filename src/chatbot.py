
print("🤖 Chatbot démarré ! Tape 'exit' pour quitter.")

while True:
    user_input = input("Toi: ")

    # Nettoyage : minuscules + supprimer les espaces
    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        print("Bot: Au revoir !")
        break

    print(f"Bot: Tu as écrit → '{clean_input}'")