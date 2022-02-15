class Bank:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, popolnenie):
        self.popolnenie = popolnenie
        self.balance += self.popolnenie
        print(f'Вы успешно пополнили ваш счет на сумму {self.popolnenie}\nВаш текущий счет: {self.balance}')
    
    def withdraw(self, snyatie):
        self.snyatie = snyatie
        if self.balance >= self.snyatie:
            self.balance -= self.snyatie
            print(f'Вы успешно сняли {self.snyatie}\nВаш текущий баланс: {self.balance}')
        else: 
            print(f'Недостаточно средств\nВаш текущий баланс: {self.balance}')

A1 = Bank(input(), int(input()))
A1.deposit(int(input('Вставьте купюру в купюроприемник\n')))
A1.withdraw(int(input('Введите нужную вам сумму\n')))