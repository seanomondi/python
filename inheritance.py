class Animal:
    def animals(self):
        print('can breath')

    def monkey(self):
        print('can walk')

    def baboon(self):
        print('can run')


class Human(Animal):
    def mtu(self):
        print('lives on land')


being = Human()

print(being.mtu())
