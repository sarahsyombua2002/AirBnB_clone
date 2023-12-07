import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        to_save = {}
        for key, value in self.__objects.items():
            to_save[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(to_save, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    # Check if the class exists in the global namespace
                    if class_name in globals():
                        obj = globals()[class_name](**value)
                        self.__objects[key] = obj
                    else:
                        print(f"Class {class_name} not found in globals(). Skipping.")
        except FileNotFoundError:
            pass

