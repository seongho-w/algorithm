class person:
    def __init__(self, param_name):
        print("i am created!",self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name,"입니다")

    pass

person_1 =person("유재석")
print(person_1.name)
print(person_1)
person_1.talk()
person_2 =person("박명수")
print(person_2)
print(person_2.name)
person_2.talk()