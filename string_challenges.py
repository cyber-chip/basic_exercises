# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))
print(word.count('а'))

# Вывести количество гласных букв в слове
glasnie = "аоиеёэыуюя"
word = 'Архангельск'
l = [c for c in word if c in glasnie]
print("Список гласных букв:", l)
print("Длина списка:", len(l))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
result = len(sentence.split())

print("Количество слов в предложении: " + str(result))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

print("\n".join([e[0] for e in sentence.split()]))


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
resul = sum(map(len, words))/len(words)
print(resul)
