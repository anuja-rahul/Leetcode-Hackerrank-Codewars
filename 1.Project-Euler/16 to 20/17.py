import inflect

engine = inflect.engine()


def number_to_words(n):
    words = engine.number_to_words(n)
    formatted_words = words.replace('-', '').replace(' ', '')
    return formatted_words


def get_letter_count(number):
    letters = ""
    for i in range(1, number+1):
        letters += number_to_words(i)
    print(len(letters))


get_letter_count(1000)
