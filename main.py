pick = input("type d for dice and c for coin\n")

pickl = pick.lower()
import random;

rnumc = random.randint(0,1)
rnumd = random.randint(0,5)

cdata = ["heads" ,"tails"]
ddata = [1 , 2 ,3, 4, 5, 6]

coin = cdata[rnumc]
dice = ddata[rnumd]


if pick == "d":
  print(dice);

elif pick == "c" :
  print(coin);
else :
  print("you typed wrong")

