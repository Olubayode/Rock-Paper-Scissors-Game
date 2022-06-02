import random

options =  ['R','P','S']
options_lower = []
for i in options:
    options_lower.append(i.lower())
print(options_lower)

def comp_play():
    return random.choice(options_lower)

def main():
    num_games = int(input('Enter the number of games you would like to play with the CPU: '))
    print('You are going to play ' + str(num_games) + ' games with the CPU!')
    num_wins = 0
   
    for i in range(num_games):
        player_move = input(' Pick an option between R, P or S ')
        # player_move = player_move.lower()
        CPU_move = comp_play()
        while player_move.lower() not in options_lower:
            # player_move = input(' Pick an option between R, P or S ')
            # CPU_move = comp_play()
            print('Error occured! Kindly input the right options available between R,P and S')
            player_move = input(' Pick an option between R, P or S ')
            # if player_move in options:
            #     break

        while player_move.lower() == CPU_move :
            print('Wow! You both tied! Play Again')
            player_move = input('Pick an option between R, P or S ')
       

            if player_move.lower() in options_lower:
                CPU_move = comp_play()
                print('The computer went with: ' + CPU_move)
                print("Both player's moves in Player  ({}): CPU ({})".format(player_move, CPU_move))
                if player_move.lower() == 'R' and CPU_move == 'S':
                    print("Both player's moves in Player  ({}): CPU ({})".format('Rock', 'Scissors'))
                    print('You won!')
                    num_wins +=1
                elif player_move.lower() == 'P' and CPU_move == 'R':
                    print("Both player's moves in Player  ({}): CPU ({})".format('Paper', 'Rock'))
                    print('You won!')
                    num_wins +=1
                elif player_move.lower() == 'S' and CPU_move == 'P':
                    print("Both player's moves in Player  ({}): CPU ({})".format('Scissors', 'Paper'))
                    print('You won!')
                    num_wins +=1
                else:
                    print('Ooopps! You lost')
                    # break

        if player_move.lower() in options_lower:
            CPU_move = comp_play()
            print('The computer went with: ' + CPU_move)
            print("Both player's moves in Player  ({}): CPU ({})".format(player_move, CPU_move))
            if player_move.lower() == 'R' and CPU_move == 'S':
                print("Both player's moves in Player  ({}): CPU ({})".format('Rock', 'Scissors'))
                print('You won!')
                num_wins +=1
            elif player_move.lower() == 'P' and CPU_move == 'R':
                print("Both player's moves in Player  ({}): CPU ({})".format('Paper', 'Rock'))
                print('You won!')
                num_wins +=1
            elif player_move.lower() == 'S' and CPU_move == 'P':
                print("Both player's moves in Player  ({}): CPU ({})".format('Scissors', 'Paper'))
                print('You won!')
                num_wins +=1
            else:
                print('Ooopps! You lost')
                
    print('You won ' + str(num_wins) + ' out of ' + str(num_games))
    return(num_wins)
print(main())
            


