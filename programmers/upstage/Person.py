class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def introduce(self, name):
        return f"Hello, my name is {name} and I am {self.age} years old."

def main():
    # Person 클래스의 인스턴스 생성
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    # 인스턴스의 introduce 메서드 호출
    print(person1.introduce("Kim"))
    print(person2.introduce("Jae"))


if __name__ == "__main__":
    main()
