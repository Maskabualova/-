import random

def choose_word():
    words = {
        'python': 'Это язык программирования.',
        'программа': 'Система, выполняющая определенные задачи.',
        'игра': 'Развлечение или занятие, которое приносит удовольствие.',
        'компьютер': 'Электронное устройство для обработки данных.',
        'разработка': 'Процесс создания программного обеспечения.'
    }
    word = random.choice(list(words.keys()))
    return word, words[word]

def display_word(word, guessed_letters):
    displayed = ''
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + ' '
        else:
            displayed += '_ '
    return displayed.strip()

def choose_difficulty():
    print("Выберите уровень сложности:")
    print("1. Легкий (10 попыток)")
    print("2. Средний (6 попыток)")
    print("3. Сложный (3 попытки)")
    print("4. Мегасложный (2 попвтки)")

    while True:
        choice = input("Введите номер уровня сложности (1/2/3/4): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 6
        elif choice == '3':
            return 3
        elif choice == '4':
            return 2
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 3 или 4.")

def main():
    word_to_guess, hint = choose_word()
    guessed_letters = set()
    attempts = choose_difficulty()

    print("\nДобро пожаловать в игру 'Угадай слово'!")
    print(f"Подсказка: {hint}")

    while attempts > 0:
        print(f"\nСлово: {display_word(word_to_guess, guessed_letters)}")
        print(f"Оставшиеся попытки: {attempts}")
        print("Введите 'hint' для подсказки или 'guess' для угадывания слова.")
        guess = input("Введите букву или слово: ").lower()

        if guess == 'hint':
            if attempts > 1:
                print(f"Подсказка: {hint}")
                attempts -= 1
            else:
                print("У вас недостаточно попыток для получения подсказки.")
            continue

        if len(guess) == 1:
            if not guess.isalpha():
                print("Пожалуйста, вводите только буквы.")
                continue

            if guess in guessed_letters:
                print("Вы уже угадывали эту букву.")
                continue

            guessed_letters.add(guess)

            if guess in word_to_guess:
                print("Вы угадали букву!")
            else:
                attempts -= 1
                print("К сожалению, такой буквы нет.")

        elif len(guess) == len(word_to_guess):
            if guess == word_to_guess:
                print(f"Поздравляем! Вы угадали слово: {word_to_guess}")
                break
            else:
                attempts -= 1
                print("Вы ошиблись в угадывании слова.")
        else:
            print("Пожалуйста, угадывайте одну букву или целое слово.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Поздравляем! Вы угадали слово: {word_to_guess}")
            break
    else:
        print(f"Вы проиграли! Загаданное слово было: {word_to_guess}")

if __name__ == "__main__":
    main()

