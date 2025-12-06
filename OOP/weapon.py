class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = Weapon(name="Iron Sword",
                    weapon_type="sword",
                    value=10,
                    damage=5)
short_bow = Weapon(name="Short Bow",
                   weapon_type="ranged",
                   value=8,
                   damage=4)
fists = Weapon(name="Fists",
               weapon_type="blunt",
               value=0,
               damage=2)
