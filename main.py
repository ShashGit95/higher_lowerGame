from game_data import data
from art import logo,vs
from replit import clear
import random
print(logo)
def play_game():
  
    def check_data(followers1,followers2):
      
        if followers1 > followers2:
            highest_followers = followers1
        else:
            highest_followers = followers2
        
        user_choose = input("Who has more followers? Type 'A' or 'B': ")
        
        if user_choose.upper() == "A" and highest_followers == followers1:
          return True 
        elif user_choose.upper() == "B" and highest_followers == followers2:
          return True
        else:
          return False

    score = 0
    random_item2 = random.sample(data, 1)
    while True:
      random_item1 = random_item2
      item1 = random_item1[0]
      name1 = item1['name']
      value1 = item1['follower_count']
      descr1 = item1['description']
      countr1 =item1['country']
    
      random_item2 = random.sample(data, 1)   
      while random_item2 == random_item1:
        random_item2 = random.sample(data, 1)   
      item2 = random_item2[0]
      name2 = item2['name']
      value2 = item2['follower_count']
      descr2 = item2['description']
      countr2 =item2['country']
      
      print(f"compare_A : {name1} , {descr1} , from {countr1} ")
      print(vs)
      print(f"compare_B : {name2} , {descr2} , from {countr2} ")
      
      checked_data = check_data(value1,value2)
      clear()
      print(logo)
      if checked_data:
          score += 1
          print(f"You're right! Current score: {score}")
          
      else:
          print(f"Sorry, that's wrong. Final score: {score}")
          break
    
    

while True:
    play_game()
    play_again = input("Do you want to play again? Type 'yes' or 'no': ")
    if play_again.lower() == "no":
        print("Good Bye!")
        break
    elif play_again.lower() != "yes":
        print("Invalid input")
        break
    clear()
    print(logo)
