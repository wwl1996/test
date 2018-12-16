import random


# 定义英雄类
class Hero(object):

    def __init__(self, name):
        self.name = name
        self.hp = 100  # 血量
        self.attack = random.randint(45, 100)  # 随机产生攻击值
        self.defense = 30

    # 显示英雄信息
    def __str__(self):
        return "名字:%s 血量:%s 攻击:%d 防御:%d" % (self.name, self.hp, self.attack, self.defense)

    # 攻击函数
    def fight(self, monster):
        # 计算怪物掉血多少
        mhp = self.attack - monster.defense
        # 减少怪物血量
        monster.hp = monster.hp - mhp
        # 提示信息
        print("英雄[%s]对怪物[%s]造成了%d伤害!" % (self.name, monster.name, mhp))


#  定义怪物类
class Monster(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100  # 血量
        self.attack = random.randint(31, 100)  # 随机产生攻击值
        self.defense = 30

    # 显示怪物信息
    def __str__(self):
        return "名字:%s 血量:%s 攻击:%d 防御:%d" % (self.name, self.hp, self.attack, self.defense)

    # 攻击函数
    def fight(self, hero):
        # 计算怪物掉血多少
        mhp = self.attack - hero.defense
        # 减少怪物血量
        hero.hp = hero.hp - mhp
        # 提示信息
        print("怪物[%s]对英雄[%s]造成了%d伤害!" % (self.name, hero.name, mhp))


# 创建对象
hero = Hero("一刀死")
# 创建怪物
monster = Monster("打死我爆好装备")
# 回合数
my_round = 1
# 开始回合战斗
input('ready go')

while True:
    input()
    print(hero)
    print(monster)
    print("-" * 50)
    print("当前第%d回合:" % my_round)
    hero.fight(monster)
    if monster.hp <= 0:
        print("英雄[%s]击败了怪物[%s],顺利通关!" % (hero.name, monster.name))
        break
    monster.fight(hero)
    if hero.hp <= 0:
        print("怪物[%s]仰天大笑，哈哈哈,弱鸡!" % monster.name)
        break

    my_round += 1

print("Game Over!")