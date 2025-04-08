from greets import greetings
from translate import Translator

translator = Translator(to_lang='pt')

if __name__ == "__main__":
    for g in greetings:
        print(translator.translate(g).title())


