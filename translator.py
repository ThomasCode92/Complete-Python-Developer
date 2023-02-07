from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('text.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)

        # Write the translation to a new file
        with open('./test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:
    print('check your file path')
    raise err
