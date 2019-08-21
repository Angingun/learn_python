# 奥特曼打小怪兽

from abc import ABCMeta, abstractclassmethod
from random import randrange


class Fight(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

        @property
        def name(self):
            return self._name

        @property
        def hp(self):
            return self._hp

        @hp.setter
        def hp(self, hp):
            self._hp = hp if hp >= 0 else hp = 0

        @property
        def alive(self):
            return self._hp > 0

        @abstractclassmethod
        def attack(self, other):
            pass


class UtralMan(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randrange(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attck(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randrange(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randrange(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~{}奥特曼~~~\n'.format(self._name) + \
            '生命值: {}\n'.format(self._hp) + \
            '魔法值：{}\n'.format(self._mp)

# uncompleted

