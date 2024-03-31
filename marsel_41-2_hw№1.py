class superhero:
    def __init__(self,name,nickname,superpower,health_point,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase

    def printt(self):
        print (f'имя: {self.name}')

    def __len__(self):
        return len(self.catchphrase)


    def __str__(self):
        return (f'прозвише: {self.nickname}\n'
                f'супер способность: {self.superpower}\n'
                f'здоровье: {self.health_point * 2}')



hero = superhero('Грут',
                 'Деревянный',
                 'быстрая регенерация, '
                 'очень большая физическая сила, '
                 'умеет управлять деревьями',
                  200,
                 'я есть грут')
hero.printt()
print(hero)
print(len(hero))

