from spellchecker import SpellChecker
class SpellCheckerApp:
    def __init__(self):
        self.spell=Spellchecker()

    def correct_txt(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'correcting "{word}"to"{corrected_word}"')
                corrected_words.append(corrected_word)
                

        #return correct text
        return''.join(corrected_words)
    
#run app 
    def run(self):
        print("\n-------spell checker-------")
        while True:
            text = input('Enter text to check (or type "exit" to quit): ')

            if text.lower() == 'exit':
                print('closing the program...!!!!')
                break
            corrected_text = self.correct_txt(text)
            print(f'corrected text :{corrected_text}')

#run main program
if __name__ == "__main__":
    SpellCheckerApp().run()
