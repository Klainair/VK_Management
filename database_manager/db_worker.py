from pymongo import MongoClient


class DBWorker:
    __client = None
    # Атавизм. Перенес коннект к базе в __init__, использование вне данного метода не планируется.
    # db = None
    __picture_collection = None
    __gif_collection = None
    __video_collection = None

    def __init__(self, username, password, aut_source):
        self.__client = MongoClient('localhost',
                                    username=username,
                                    password=password,
                                    autSource=aut_source,
                                    authMechanism='SCRAM-SHA-256')
        # Пока писал self.__db = self.__client[...] понял что что-то делаю не так ->
        # -> Перенес __db в __init__
        db = self.__client['picture']
        # TODO: поменять название базы в монго с picture на *придумать навзание*
        # Название коллекций не трогать, пока что все устраивает (18.04.19)
        self.__picture_collection = db['picture']
        self.__gif_collection = db['gif']
        self.__video_collection = db['video']

    def write_data(self, data):
        # TODO: ушел на работу. Доделать
        pass
