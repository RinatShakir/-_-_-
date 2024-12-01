import time #                                                   # Имрортируем функцию времени в наш код.

class User:                                                     # Создаем класс пользователей, которые инициирует ввод пользователя: его ник, пароль и возраст.
    def __init__(self, nickname, password, age):               # Создаем функцию инициирования ввода пользователя и его данных.
        self.nickname = nickname                                # Инициируется запись ника пользователя.
        self.password = hash(password)                          # Инициируется операция хэширования пароля пользователя для безопасности.
        self.age = age                                          # Инициируется запись возраста пользователя.

    def __str__(self):                                          # Создаем функцию для получения строкового представления ника пользователя,
                                                                # где будет происходить преобразование ника в строку.
        return self.nickname                                    # Записываем метод возврата ника пользователя в строковом значении.

    def __eq__(self, other):                                    # Создаем функцию, где будет происходить сравнение пользователя
                                                                # по нику с другими никами других пользователей.
        return other.nickname == self.nickname                  # Записываем метод возврата ника, который и будет записан.

    def get_info(self):                                         # Создаем функцию получения информации по пользователю,
        return self.nickname, self.password                     # где возвращаем ник и пароль пользователя.

class Video:                                                    # Создаем 2-й класс видео материалов,
    def __init__(self, title, duration, adult_mode = False):    # в котором создаем функцию инициализации данных ведоматериала,
                                                                # где есть заголовок видеоматериала, длина заголовка в секундах и есть возрастное ограничение.
        self.title = title                                      # Инициируется заголовок видеоматериала.
        self.duration = duration                                # Инициируется длина (продолжительность) видеоматериала.
        self.time_now = 0                                       # Инициируется текущий момент времени, изначально установленный на 0.
        self.adult_mode = adult_mode                            # Инициируется флаг проверки возрастной категоризации,
                                                                # где получаем логический 0 или 1.

    def __str__(self):                                          # Создаем функцию для получения строкового представления видеоматериала,
                                                                # где будет происходить преобразование название видеоматериала в строку.
        return self.title                                       # Записываем метод возврата названия видеоматериала в строковом значении.

    def __repr__(self):                                         # Создаем функцию для возврата заголовка видеоматериала для его просмотра.
        return self.title                                       # # Записываем метод возврата заголовка.

class UrTube:                                                   # Создаем 3-й класс под название "UrTube" для входа,
    def __init__(self):                                         # в котором создаем функцию инициализации данных.
        self.users = []                                         # Инициируется регистрация пользователей.
        self.videos = []                                        # Инициируется регистрация загруженных видеоматериалов.
        self.current_user = None                                # Инициируется запись текущего пользователя, который изначально получает значение None.

    def log_in(self, login, password):                          # Создаем внутри функцию для входа пользователя по логину и паролю.
        for user in self.users:                                 # Внутри функции записываем цикл для входа пользователя,
            if (login, hash(password) == user.get_info()):        # где при выполнении условия проверки, что логин и хэшированный пароль равен текущему пользователю,
                self.current_user = user                        # инициируется ввод текущего пользователя и
                return user                                     # возвращается значение пользователя, который в данный момент находится на платформе.

    def register(self, nickname, password, age):                # Создаем функцию регистрации пользователя с ником, паролем и возрастом,
        new_user = User(nickname, password, age)                # где новый пользователь - это текущий пользователь.
        if new_user not in self.users:                          # Внутри создается условие, что если новый пользователь не из числа имеющихся пользователей,
            self.users.append(new_user)                         # то в случае несовпадения новый пользователь добавляется в конец списка с помощью операции append.
            self.current_user = new_user                        # И в конце текущий пользователь регистрируется, как новый.
        else:                                                   # В иных случаях, когда есть совпадение текущего пользователя со списком других,
            print(f'Пользователь {nickname} уже существует')    # выводится на экран соответствующая запись.

    def log_out(self):                                          # Создаем функцию выхода пользователя,
        self.current_user = None                                # где происходит обнуление значения пользователя.

    def add(self, *videos: Video):                              # Создаем функцию добавления видеоматериала на платформу, где видео могут иметь разные количества значений
                                                                # (используем *).
        for video in videos:                                    # Внутри функции создаем цикл проверки текущего видеоматериала из числа всех видеоматериалов,
            if video.title not in self.videos:                  # где выполняется условие проверки, что наименования текущего видеоматериала НЕ совпадает с другими.
                self.videos.append(video)                       # При выполнении условия новый видеоматериал добавляется в конец списка с помощью операции append.

    def get_videos(self, search):                               # Создаем функцию для поиска видеоматериала по заголовку.
        titles = []                                             # Внутри создаем список наименований видеоматериалов.
        for video in self.videos:                               # Также внутри функции создаем цикл для проверки вводимого наименования видео по всему списку видеоматериалов.
            if search.lower() in str(video).lower():            # Используем условие с методом преобразования к нижнему регистру строкого значения наименования видео.
                titles.append(video)                            # При выполнении условия поисковый видеоматериал добавляется в конец списка с помощью операции append
        return titles                                           # и возвращается список видеоматериалов.

    def watch_videos(self, title):                              # Создается функция просмотра видеоматериала,
        if self.current_user is None:                           # где создается условие проверки текущего пользователя, что он новый.
            print('Войдите в аккаунт, чтобы смотреть видео')    # При выполнении условия на экран выводится соответствующее приглашение зайти в свой аккаунт
            return                                              # и осуществляется возврат страницы.
        for video in self.videos:                               # Внутри функции записывается цикл для проверки текущего видеоматеариала из списка видеоматериалов,
            if title == video.title:                            # где создается условие, что наименование видео соответствует названию по списку.
                if video.adult_mode and self.current_user.age >= 18:
                                                                # Также внутри этого условия создается другое условие доя проверки возвраста пользователя,
                                                                # где условие выполнения обозначено, как равно или больше 18 лет.
                    while video.time_now < video.duration:      # Внутри данного условия создается цикл для просмотра видео по времени,
                        video.time_now += 1                     # где текущее время равно текущему значению индекса + 1.
                        print(video.time_now, end =' ')         # Выводится на экран текущее значение времени, а при завершении пустое строковое значение.
                        time.sleep(1)                           # Записываем операцию для принятия в качестве аргумента число, указывающее продолжительность паузы в секундах.
                    video.time_now = 0                          # Определяем текущее значение времени с 0.
                    print('Конец видео')                        # По итогам завершения цикла выводим на экран соответствующую надпись.
                else:                                           # В иных случаях, когда пользователю меньще 18 лет,
                    print('Вам нет 18 лет, пожалуйства покиньте страницу')
                                                                # предлагаем пользователю покинуть страницу просмотра видео с выводом соотв.надписи на экран.
                    break                                       # прерываем цикл.

                                                                # Записываем входные параметры для проверки кода:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

                                                                # добавление видео:
ur.add(v1, v2)

                                                                # проверка поиска:
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

                                                                # проверка на вход пользователя и возрастное органичение:
ur.watch_videos('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_videos('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_videos('Для чего девушкам парень программист?')

                                                                # проверка входа в другой аккаунт:
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

                                                                # попытка возпроизвести несуществующее видео:
ur.watch_videos('Лучший язык программирования 2024 года!')