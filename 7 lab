import random

# 1. Чтение содержимого из текстового файла "text1.txt" построчно и отображение на экране:
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# 2. Чтение случайной строки из файла:
def read_random_line(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
            print(random_line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# 3. Подсчет прописных букв в текстовом файле:
def count_uppercase_chars(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = sum(1 for char in content if char.isupper())
            print(f"Uppercase characters count: {count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# 4. Подсчет количества строк из файла, не начинающихся с буквы 'D':
def count_non_d_starting_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            count = sum(1 for line in lines if not line.startswith('D'))
            print(f"Number of lines not starting with 'D': {count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# 5. Подсчет слов, оканчивающихся на символ 'F':
def count_words_ending_with_f(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            count = sum(1 for word in words if word.endswith(('F', 'f')))
            print(f"Words ending with 'F' count: {count}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Вызов всех функций для обработки файла 'text1.txt':
read_text_file('text1.txt')
read_random_line('text1.txt')
count_uppercase_chars('text1.txt')
count_non_d_starting_lines('text1.txt')
count_words_ending_with_f('text1.txt')
