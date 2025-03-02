# https://inf-ege.sdamgia.ru/problem?id=33182
"""
Определите, сколько раз в тексте произведения А.С. Пушкина «Капитанская дочка» встречается имя Емельян в любом падеже.

Открыв файл нас встретят обложка и аннотация, которые не относятся к тексту произведения - их надо удалить.
(Но если задание поставлено "в файле, содержащем произведение", то учитывать нужно и аннотацию)
* Интересно то, что в аннотации встречается слово Емельян, но опять же, искать нужно в произведении.

Склоняем имя Емельян, для каждого падежа ищем как отдельное слово. Сумма результатов каждого падежа и будет ответом.
Емельян = 1
Емельяна = 1
Емельяну = 0
Емельяна = 0
Емельяном = 0
Емельяне = 0

Ответ: 2
"""