# Lancia i Dadi
In questo gioco il programma genera due numeri casuali tra 1 e 6. Il programma poi chiede all'utente se vuole lanciare di nuovo i dadi. Se risponde y o yes allora la
coppia di dadi viene lanciata di nuovo.

```py
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice.  The values are:")
    print(random.randint(min, max))
    print(random.randint(min, max))
    roll_again = input("Roll the dices again?")
```

```sh
Rolling the dice.  The values are:
4
4
Roll the dices again?
```