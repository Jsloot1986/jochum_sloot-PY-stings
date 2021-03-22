# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#deel 1
player_first_goal = 'Ruud Gullit'
player_second_goal = 'Marco van Basten'

goal_1 = 32
goal_2 = 54

scores = player_first_goal + ' ' + str(goal_1) + "," + player_second_goal + ' ' + str(goal_2)

print(scores)

report = f'{player_first_goal} scores at {goal_1}nd minute \n{player_second_goal} scores at {goal_2}th minute'

print(report)

#deel 2
player = 'Ronald Koeman'
firstname = player.find(' ', 1, 13)
first_name = player[:6]
first_letter = player[:1]
last_name_len = len(player)
lastname = player.find(' ', 6, 13)
last_name = player[6:]

name_short = first_letter + last_name


#print(first_name)
#print(lastname)
#print(last_name)
#print(last_name_len)
#print(name_short)

chant = f'{first_name}! ' * firstname

print(chant)

good_chant = chant != ' '

print(good_chant)

