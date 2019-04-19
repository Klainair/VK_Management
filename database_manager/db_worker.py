from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from util.logSystem.log_manager import Log_manager

# TODO: Обернуть код в try: except:
class DBWorker:
    __client = None
    # Атавизм. Перенес коннект к базе в __init__, использование вне данного метода не планируется.
    # db = None
    __picture_collection = None
    __gif_collection = None
    __video_collection = None

    def __init__(self, username, password, aut_source):
        self.__client = MongoClient('127.0.0.1',
                                    username=username,
                                    password=password,
                                    authSource=aut_source,
                                    authMechanism='SCRAM-SHA-1')
        try:
            self.__client['admin'].command('ismaster')
            print('Соединение установлено')
        except ConnectionFailure:
            Log_manager.errors(message='Не удалось установить соединение с MongoDB')
        # Пока писал self.__db = self.__client[...] понял что что-то делаю не так ->
        # -> Перенес __db в __init__
        db = self.__client['picture']
        # TODO: поменять название базы в монго с picture на *придумать навзание*
        # Название коллекций не трогать, пока что все устраивает (18.04.19)
        self.__picture_collection = db['picture']
        self.__gif_collection = db['gif']
        self.__video_collection = db['video']

    # data - картинка в base64 формате
    def write_picture(self, data=None, source_vk=None, used=False):
        try:
            post = {"picture": data,
                    "source_vk": source_vk,
                    "used": used}
            data_id = self.__picture_collection.insert_one(post).inserted_id
            print("Записана картинка: " + data_id)
            return True
        except:
            return False
