import random
import time
time.sleep(1)
print(' ******* king queen soldier thief game ******* ' )
time.sleep(1)

print('king:100 , queen :50, soldier :20 , thief :0')
time.sleep(1)

a = str(input("enter player 1 name \n"))
b = str(input("enter player 2 name \n"))
c = str(input("enter player 3 name \n"))
d = str(input("enter player 4 name \n"))

length_of_game  = int(input("how much rounds \n"))

king = 100
queen = 50
soldier = 20
thief = 0

a_score = []
b_score = []
c_score = []
d_score = []



for i in range(1,length_of_game+1):
    list_for_random =[100,0,20,50]
    print('round', i)
    time.sleep(1)
    print('shacking chits ... ')
    time.sleep(1)
    print('picking chits...')
    time.sleep(1.5)
    pick_1 = random.choice(list_for_random)
    a_score.append(pick_1)
    list_for_random.remove(pick_1)
    print(a , 'get ', a_score[i-1] , 'points')
    time.sleep(1.5)

    pick_2 = random.choice(list_for_random)
    b_score.append(pick_2)
    list_for_random.remove(pick_2)
    print(b , 'get ', b_score[i-1] , 'points')
    time.sleep(1.5)

    pick_3 = random.choice(list_for_random)
    c_score.append(pick_3)
    list_for_random.remove(pick_3)
    print(c , 'get ', c_score[i-1] , 'points')
    time.sleep(1.5)

    pick_4 = random.choice(list_for_random)
    d_score.append(pick_4)
    list_for_random.remove(pick_4)
    print(d , 'get ', d_score[i-1] , 'points')
    time.sleep(1.5)

print("result is... -")

time.sleep(2)
    
print('total points of ', a , 'is' , sum(a_score))
time.sleep(1)
print('total points of ', b , 'is' , sum(b_score))
time.sleep(1)
print('total points of ', c , 'is' , sum(c_score))
time.sleep(1)
print('total points of ', d , 'is' , sum(d_score))

result_list =[sum(a_score),sum(b_score),sum(c_score),sum(d_score)]
max_num = max(result_list)
result_list.remove(max_num)

second_max = max(result_list)

    

if sum(a_score) > sum(b_score) and  sum(a_score) > sum(c_score) and sum(a_score) > sum(d_score):
    print(a , 'won')

elif sum(b_score) > sum(a_score) and  sum(b_score) > sum(c_score) and sum(b_score) > sum(d_score):
    print(b , 'won')

elif sum(c_score) > sum(a_score) and  sum(c_score) > sum(b_score) and sum(c_score) > sum(d_score):
    print(c , 'won')

else:
    print(d , 'won')

if a_score ==second_max:
    print(a ,' is first runner up' )

if b_score ==second_max:
    print(b ,' is first runner up' )

if c_score ==second_max:
    print(c ,' is first runner up' )

if d_score ==second_max:
    print(d ,' is first runner up' )

