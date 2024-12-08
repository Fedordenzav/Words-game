import speech_recognition as sr
from random import choice 
from time import sleep

def voice_to_text():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        text = recog.recognize_google(audio, language="en-EN")
        return text



levels = {
    "easy": ["apple", "what", "dog", "cat"],
    "medium": ["body", "bored", "mirror", "comfortable", "tired"],
    "hard": ["machine learning", "after go police", "brand", "after party"]
}

def game():
    level = input("Какой уровень игры вы хотите выбрать?(easy, medium, hard):")
    while level not in levels:
        print("Такого уровня игры нету!")
        level = input("Какой уровень игры вы хотите выбрать?(easy, medium, hard):")    
    
    words = levels.get(level)
    words = words.copy()

    score = 0 
    attempts = 3

    while True:
        if attempts <= 0:
            print("У вас закончились попытки! Вы проиграли!")
        word = choice(words)
        break
        if attempts > 0 and len(words) == 0:
            print("Вы выиграли! Поздравляем!")
        break 
    word = choice(words)
    print(f'Проговорите слово "{word}"')
    player_word = voice_to_text().lower()

    if player_word == word:
        print("Вы ответили правильно!")
        score += 1
        words.remove(word)
    else:
        attempts -= 1
        print("Вы ответили неправильно!")

game()
