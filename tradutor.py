from googletrans import Translator

translator = Translator()

language = {"bn": "Bangla",
            "en": "English",
            "ko": "Koren",
            "fr": "French",
            "de": "German",
            "he": "Hebrew",
            "hi": "Hindi",
            "it": "Italian",
            "ja": "Japanese",
            'la': "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "ru": "Russian",
            "ar": "Arabic",
            "zh": "Chinese",
            "es": "Spanish"
            "pt": "Portuguese"
            }

allow = True

while allow:

    user_code = input(
        f"Escolha a linguagem que você deseja traduzir. Caso contrário digite opções. \n")

    if user_code == "opções":
        print("Code : Language")
        for i in language.items():
            print(f"{i[0]} => {i[1]}")
        print()

    else:
        for lan_code in language.keys():
            if lan_code == user_code:
                print(f"Você selecionou {language[lan_code]}")
                allow = False
        if allow:
            print("Essa linguagem não é valida!")

while True:
    string = input(
        "\nDigite o texto que você deseja traduzir: \nPara sair digite 'fechar'\n")

    if string == "fechar":
        print(f"\nTenha um bom dia!")
        break

    translated = translator.translate(string, dest=user_code)

    print(f"\n{language[user_code]} tradução: {translated.text}")
    
    print(f"Pronúncia: {translated.pronunciation}")

    for i in language.items():
        if translated.src == i[0]:
            print(f"Traduzido do: {i[1]}")
