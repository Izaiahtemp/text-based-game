#adventure game
 import time 
choice_1 = input(" you have been locked up in this prison for 2 years \n i think it's time to escape do you agree type start when you are ready ") 
if choice_1 == "start" or "Start":
  print('you start gathering information to help you escape ')
  time.sleep(1)

choice_2 = input(" while sitting at lunch you see a door left slightly open \n if you want to try and escape now press N if you want to wait and see if a better  opportunity comes about press W ") 
time.sleep(1)
if choice_2 == "N" or choice_2 == "n": 
  print('you make a run for the door when the guard stops looking')
  time.sleep(1)
  ( 'you make it to the door as you run in you see two guards running at you from the left you turn to the right there is a door \n you check to see if it is unlocked but that only wated time the gards catch you and add another 10 yeas onto your sentance \n GAME OVER! ') 
  exit()

if choice_2 == "w" or choice_2 == "W":
  choice_3 = input('you are doing your daily job in the tool shed you notice there are no guards around they are all distracted by a fight in the yard \n do you want to steal a hammer press S if you dont want to risk it press D ')

if choice_3 == "d" or choice_3 == "D":
  print (' You leave the hammer behind as you are leaving you notice you are alone in the yard you look around confused but you wont let this opportunity go to waste ')
  time.sleep(1)
  print (' you go to the laundry room and steel a pile of sheets and make a rope to climb over the gate \n as you are climbing over the gate the guards must have spotted you because you hear an alarm go off \n  you make it out of the prison you keep running until you hear dogs barking you turn back there are about ten police dogs chacing you you keep running as fast as you can but they catch you and that was the last anybody heard about you \n  GAME OVER  ')
  exit() 

else: 
    print ('you steal the hammer and leave trying not to look suspicious')
    time.sleep(1)
    print('it has been 2 days since you stole the hammer and you finnaly think you know the perfect time to start hammering at your wall \n every lunch there is always yelling and fighting \n so you decide to stay back at lunch and as soon as the yelling starts you start smashing the wall ')
  
time.sleep(1)

choice_4 = input(" you realise how long this is going to take you have an idea on how you can get this done faster \n press P if you want to pay someone to have another fight and steal another hammer and recruit someone to help you escape or press B to keep digging by yourself ")

if choice_4 == "b" or "B":
  print("you keep digging on your own it is taking ages but you are almost thrugh \n you have a poster that covers the hole when your not in the cell \n when you get back to your cell you continue digging and the gaurds come around for a random cell inspecton \n your poster doesn't fool the gaurds \n GAME OVER ")
  exit()

if choice_4 == "p" or "P": 
  print('you listen around for anyone trying to escape ')
  choice_5 = input('do you want to risk the plan and ask someone to join and help or carry on the plan \n press A to ask someone and press c to keep going on your own ')

  if choice_5 == "c" or "C": 
    print("you keep digging on your own it is taking ages but you are almost thrugh \n you have a poster that covers the hole when your not in the cell \n when you get back to your cell you continue digging and the gaurds come around for a random cell inspecton \n your poster doesn't fool the gaurds \n GAME OVER ")
  exit() 

  if choice_5 == "A" or "a": 
    choice_6 = input('you ask John to help you \n dig together for two days and finally get through the wall \n do you choose press N to try now or press W to wait a few days and get more tools ')
    if choice_6 == "W" or "w": 
      print('you wait three days \n the gaurds do a cell inspection and find your hole and you go to a maximum security prison \n GAME OVER ')
      exit() 


if choice_6 == "N" "n"

 print (' you and John sneak through the hole \n into the vents you crawl through till you reach the end you climb onto the roof \n you have to take a small fall out of the gate and you get out and run away you have escaped \n YOU WIN! ')


    



  
  





















  
  