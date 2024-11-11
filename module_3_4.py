# Создаем функцию, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.

def single_root_words(root_word, *other_words):
    same_words = [] # внутри функции создаем пустой список
    for word in other_words: # задаем переменную word в цикле for, которое будет корнем слова для прохождения цикла после написания неоднокоренного слова other_words из списка
        if root_word.lower() in word.lower() or word.lower() in root_word.lower(): # задаем внутри цикла условие, что если однокоренное слово root_word содержить корень (word),
             # внутри условия вызываем функцию нижнего регистра для определяемых переменных для того, чтобы исключить отбраковку слов написанных с заглавных букв.
            same_words.append(word) # используем функцию append для возврата по циклу в списке same_word.

    return same_words # при выполнении условия и окончанию цикла возвращаем слово из списка same_word.

# вписываем заданные входые параметры из задачи для последующей обработки в функции и вывода на экран результата.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)