# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#deel 1
player_first_goal = 'Ruud Gullit'
player_second_goal = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_first_goal + ' ' + str(goal_0) + ',' + player_second_goal + ' ' + str(goal_1)

print(scorers)

report = f'{player_first_goal} scores at {goal_0}nd minute\n{player_second_goal} scores at {goal_1}th minute'

print(report)

#deel 2
player = 'Ronald Koeman'

first_name = player[:player.find(' ')]

first_letter = player[:1]

last_name_len = len(player[player.find(' '):-1])

name_short = f'{player[:1]}{player[player.find(" "):]}'


print(first_name)
print(last_name_len)
print(name_short)

chant = f'{first_name}! ' * len(first_name)

print(chant)

good_chant = chant != chant[-1:chant.find(' ')]

print(good_chant)

