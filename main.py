import bankaccount
from Character import Hero, Enemy
from bankaccount import BankAccount
from weapon import short_bow, iron_sword
from Bank import Bank

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon = short_bow)

while False:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    if hero.__getattribute__("health") < 90:
        print("AWWWW MY GAWDDDD")

    input()
client_accounts = []
bank = Bank("ING BANK SLASKI", account_id=1)
first_customer = bank.create_account( "2222555533334444", "Jan Kowalski", "1232")
client_accounts.append(first_customer)
for clients in client_accounts:

    print(f"{clients.accountName}")
first_customer.check_balance()
print(f"The bank name is: ", bank.name)
first_customer.deposit(200)
bank.show_accounts()

cels_temp = [23, 34, 12, 24]
fahr_temp = []
cels_temp.append(2)
for temperature in cels_temp:
    fahrenheit = (temperature * 9/5) + 32
    fahr_temp.append(fahrenheit)

print(fahr_temp)


