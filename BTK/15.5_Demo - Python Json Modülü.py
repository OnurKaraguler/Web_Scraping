import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False         # varsayımsal olarak kullanıcı log in olmamış
        self.currentUser = {}           # login olmuş ise isLoggedIn True olacak ve bilgileri buraya yazılacak

        # load users from .json file
        self.loadUser()

    def loadUser(self):
        if os.path.exists('users.json'):        # dosya daha önce oluşturuldu mu?
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            # print(self.users)

    def register(self, user: User):         # Dışarıdan User bilgisi gelecek ve tipi User olacak
        self.users.append(user)
        self.saveToFile()
        print('kullanıcı oluşturuldu.')
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapıldı')
                break
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('giriş yapılmadı.')

    def saveToFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))      # json olarak kaydetmek için user bilgileri __dict__ ile dict e çevrilir.
        # print(list)
        # print(type(list))

        with open ('users.json', 'w') as file:
            json.dump(list, file)         # dump-> kullanıcı kaydetmek için, dumps-> var olan objeyi json a dönüştürür

repository = UserRepository()

while True:
    print('Menu'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5 -Exit\nseçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            print(user)
            repository.register(user)

            # print(repository.users)
        elif secim == '2':
            if repository.isLoggedIn:
                print('zaten login oldunuz')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username,password)

        elif secim == '3':
            repository.logout()
        elif secim == '4':
            repository.identity()
        else:
            print('Yanlış seçim')