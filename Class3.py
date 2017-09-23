from pymystem3 import Mystem

mystem = Mystem()
text = 'Как насчёт небольшого стемминга'
lemmas = mystem.lemmatize(text) #вывод лемм слов (начальных форм)
lemmas2 = mystem.analyze(text) #вывод грамм характеристик слов в виде словаря
print(''.join(lemmas))

for key in lemmas2:
    for el in key:
        print(key[el]) # вот вроде что-то осмысленное выдал



