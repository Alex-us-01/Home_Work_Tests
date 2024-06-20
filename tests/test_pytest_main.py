import pytest

from main import discriminant, vote, solve


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
            [1, 2, 3, -8],
            [2, 4, 6, -32],
            [5, 2, 8, -156],
            [3, 2, -4, 52],
            # [2, 2, 2, 10]
    )

)
def test_discriminant(a, b, c, expected):
    result = discriminant(a, b, c)
    assert expected == result


def test_discriminant_wrong():
    numbers = [2, 2, 2]
    expected = -32
    result = discriminant(*numbers)
    assert expected != result


@pytest.mark.parametrize(
    'args, expected',
    (
            [[1, 1, 1, 1, 2], 1],
            [[1, 5, 5, 5, 7, 3, 1, 1, 2, 5, 5], 5],
            [[1, 3, 2, 2, 3, 3, 1, 1, 2, 5, 2], 2],
            [[1, 3, 1, 1, 4], 1],
            [[2, 4, 4, 3, 4, 3], 4],
    )
)
def test_vote(args, expected):
    result = vote(args)
    assert expected == result


def test_vote_wrong():
    numbers = []
    with pytest.raises(ValueError):
        vote(numbers)


@pytest.mark.parametrize(
    'phrases, expected',
    (
            [[
                "нажал кабан на баклажан",
                "дом как комод",
                "рвал дед лавр",
                "азот калий и лактоза",
                "а собака боса",
                "тонет енот",
                "карман мрак",
                "пуст суп"
            ], ['нажал кабан на баклажан', 'рвал дед лавр', 'азот калий и лактоза', 'а собака боса', 'тонет енот',
                'пуст суп']
            ],
    )
)
def test_solve(phrases, expected):
    result = solve(phrases)
    assert expected == result


def test_solve_wrong():
    phrases = []
    result = solve(phrases)
    expected = []
    assert expected == result


# class TestYandexDisc(YandexDisc):
#     def test_create_folder(self):
#         result = self.create_folder()
#         expected = 201
#         assert expected == result
#
#     def test_check_folder(self):
#         result = self.check_folder()
#         expected = 200
#         assert expected == result
#
#     def test_delete_folder(self):
#         result = self.delete_folder()
#         expected = 204
#         assert expected == result
#
#     def test_delete_folder_wrong(self):
#         with pytest.raises(TypeError):
#             self.delete_folder()
