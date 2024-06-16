
def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    dscr = b ** 2 - 4 * a * c
    print(dscr)
    return dscr


def solution(a, b, c):
    discr = discriminant(a, b, c)
    if discr == 0:
        x = -(b / (2 * a))
        print(x)
    elif discr > 0:
        x1 = (-b + discr ** 0.5) / 2 * a
        x2 = (-b - discr ** 0.5) / 2 * a
        print(f'{x1} {x2}')
    elif discr < 0 :
        print('корней нет')



def vote(votes):
    list_idx = []
    for idx, i in enumerate(votes):
        list_idx.append([votes.count(i), idx])
    return (votes[max(list_idx)[1]])


def solve(phrases: list):
    result = [] # список палиндромов
    for phrase in phrases: # пройдите циклом по всем фразам
        phrase_1 = phrase.replace(' ','') # сохраните фразу без пробелов
        if phrase_1 == phrase_1[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    print(result)
    return result


phrases = [
           "нажал кабан на баклажан",
           "дом как комод",
           "рвал дед лавр",
           "азот калий и лактоза",
           "а собака боса",
           "тонет енот",
           "карман мрак",
           "пуст суп"
]
phrases = []
# solve(phrases=phrases)

if __name__ == '__main__':
    # solution(1, 8, 15)
    # solution(1, -13, 12)
    # solution(-4, 28, -49)
    # solution(1, 1, 1)
    # discriminant(3,2,-4)
    # print(vote([]))
    # print(vote([1,2,3,2,2]))
    solve(phrases=phrases)
