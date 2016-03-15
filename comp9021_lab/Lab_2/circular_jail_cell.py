# 1 = closed
# 0 = open
doors = [1] * 100
#print(doors)

for run_time in range(0, 100):
	#doors = [ 0 if door == 1 else 1 for door in doors ]
	door_index = 0
	for door in doors:
		if (door_index+1) % (run_time+1) == 0:
			if door == 0:
				doors[door_index] = 1
			else:
				doors[door_index] = 0
		door_index = door_index + 1

	#print("{} : {}".format(run_time + 1, doors))

open_doors = 100 - sum(doors)

print("{} prisoners find their doors open after 100 rounds.".format(open_doors))