import requests


class YandexDisc:


    base_url = 'https://cloud-api.yandex.net'
    url_ = f'{base_url}/v1/disk/resources'

    params = {
        'path': 'TEST_FOLDER'
    }
    headers_dict = {
        'Authorization': 'TOKEN YANDEX DISC'
    }

    def create_folder(self):
        response = requests.put(self.url_,
                                params=self.params,
                                headers=self.headers_dict)
        return response.status_code

    def create_folder_wrong(self):
        raise ValueError

    def check_folder(self):
        response = requests.get(self.url_,
                                params=self.params,
                                headers=self.headers_dict)
        return response.status_code

    def check_folder_wrong(self):
        raise ConnectionError

    def delete_folder(self):
        response = requests.delete(self.url_,
                                   params=self.params,
                                   headers=self.headers_dict)
        print(response.status_code)
        return response.status_code

    def delete_folder_wrong(self):
        raise TypeError
