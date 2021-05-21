import csv
import random
import operator

player_scores = []

def read_file(file):
	"""Reads a file and returns file contacts """
	file_contents = []
	with open(file) as csvfile:
		reader = csv.reader(csvfile)
		file_contents = list(reader)
	return file_contents


def main():
	players = read_file('Players.csv')
	players.pop(0)
	for player in players:
		pass

	random.shuffle(players)
	game(players)

def game(players):

	start = 0
	end = 12
	step = 3


	# with respect to ranking
	players = players[4:]

	def match(player1, player2):
		


		player1_match = 0
		player2_match = 0

		player1_set = 0
		player2_set = 0

		player1_game = 0
		player2_game = 0
		
		print('---Tournement---')
		print(f'{player1[1]}, v {player2[1]}')


		while True:
			
			#  GAME SET
			player1_set = 0
			player2_set = 0

			print('--Set--')
			while True:			
					# GAME
					player1_game = 0
					player2_game = 0

					print('-Game-')
					while True:


						if ( random.random() ** 1/player1[3] > random.random() ):
							player1_game = player1_game + 1

						if ( random.random() ** 1/player2[3] > random.random() ):
							player2_game = player2_game + 1

						if player1_game >= 4 and player1_game - player2_game >= 2:
							print(f'{player1[1]} wins the game agianst {player2[1]}, {player1_game}-{player2_game}')
							break

						if player2_game >= 4 and player2_game - player1_game >= 2:
							print(f'{player2[1]} wins the game agianst {player1[1]}, {player2_game}-{player1_game}')
							break
					
					if (player1_game > player2_game):
						player1_set = player1_set + 1
					
					if (player2_game > player1_game):
						player2_set = player2_set + 1
					
					if (player1_set > 5 and player1_set - player2_set >= 2):
						print(f'{player1[1]} wins the set agianst {player2[1]}, {player1_set}-{player2_set}')
						break
					if (player2_set > 5 and player2_set - player1_set >= 2):
						print(f'{player2[1]} wins the set agianst {player1[1]}, {player2_set}-{player1_set}')
						break

			if player1_set > player2_set:
				player1_match = player1_match + 1
			if player2_set > player1_set: 
				player2_match = player2_match + 1

			if (player1_match == 1 and player2_match == 1):
				print(f'{player1[1]} wins decude match agianst {player2[1]}, {player1_match}-{player2_match}')
				break
			if player1_match == 2:
				print(f'{player1[1]} wins the match agianst {player2[1]}, {player1_match}-{player2_match}')
				break
			if player2_match == 2:
				print(f'{player2[1]} wins the match agianst {player1[1]}, {player2_match}-{player1_match}')
				break

		player1[4] = player1_match		
		player2[4] = player2_match		

		addPoint({player1[1]: player1_match, player2[1]: player2_match })

		player1_match = 0
		player2_match = 0

	for i in range(0, 12):
		players[i].append(random.randint(1,10))
		players[i].append('0')


	for i in range(start, end, step):
		for j in range(i, i + step ,):
			for k in range(i + step - 1, i, -1):
				if j == k or k == j:
					break
				match(players[j], players[k])	

	winners = []
	for i in range(start, end, step):
		item = filter(players[i: i + step], 4)
		if len(item) == 2:
			item = filter(players[i: i + step], 2)
		if len(item) == 3:
			item = filter(players[i: i + step], 2)
		else:
			winners.append(item)
	
	players = winners

	start = 0
	end = 3
	step = 2
	for i in range(start, end, step):
		for j in range(i, i + step ,):
			for k in range(i + step - 1, i, -1):
				if j == k or k == j:
					break
				match(players[j], players[k])	

	winners = []
	for i in range(start, end, step):
		item = filter(players[i: i + step], 4)
		if len(item) == 2:
			item = filter(players[i: i + step], 2)
		if len(item) == 3:
			item = filter(players[i: i + step], 2)
		else:
			winners.append(item)

	players = winners

	match(players[0], players[1])


	item = filter(players, 4)
	if len(item) == 2:
		pass
	if len(item) == 2:
		pass


def filter(lst, key):
    flag = False
    l = []
    maximum = lst[0]
    for sublst in lst:
        if sublst[key] > maximum[key]:
            flag = True
            maximum = sublst
        if sublst[key] == maximum[key]:
            l.append(sublst)
    if len(l) == 1:
        l = list(l[0])
    return maximum if flag else l

def addPoint(dic):
	player_scores.append(dic)



if __name__ == "__main__":
	main()



