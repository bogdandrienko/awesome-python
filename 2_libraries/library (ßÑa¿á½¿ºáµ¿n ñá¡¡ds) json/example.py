
class JsonClass:
    @staticmethod
    def write_json_to_file(dictionary: dict, file_name="json"):
        with open(f'{file_name}.json', 'w') as file:
            json.dump(dictionary, file)

    @staticmethod
    def read_json_from_file(file_name="json"):
        with open(f'{file_name}.json', 'r') as file:
            return json.load(file)

    class Example:
        @staticmethod
        def example_write_json_to_file():
            data = {
                'key_1': 'value_1',
                'key_2': 3,
                'key_3': {
                    'key_3_1': True,
                    'key_3_2': 'value_3_2',
                }
            }
            JsonClass.write_json_to_file(dictionary=data, file_name='json')

        @staticmethod
        def example_read_json_to_file():
            dictionary = JsonClass.read_json_from_file(file_name='json')
            print(dictionary)
            print(dictionary['key_1'])