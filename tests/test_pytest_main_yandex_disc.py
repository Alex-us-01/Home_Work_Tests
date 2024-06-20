import pytest
from main_yandex_disc import YandexDisc


class TestYandexDisc(YandexDisc):
    def test_create_folder(self):
        result = self.create_folder()
        expected = 201
        assert expected == result

    def test_create_folder_wrong(self):
        with pytest.raises(ValueError):
            return self.create_folder_wrong()

    def test_check_folder(self):
        result = self.check_folder()
        expected = 200
        assert expected == result

    def test_check_folder_wrong(self):
        with pytest.raises(ConnectionError):
            return self.check_folder_wrong()

    def test_delete_folder(self):
        result = self.delete_folder()
        expected = 204
        assert expected == result

    def test_delete_folder_wrong(self):
        with pytest.raises(TypeError):
            return self.delete_folder_wrong()
