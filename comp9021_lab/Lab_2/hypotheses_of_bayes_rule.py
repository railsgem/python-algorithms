# 6 Estimating the probabilities of hypotheses in the light of more
# and more evidence
# Write a program that simulates the cast of an unknown die, chosen from a set of 5 dice with 4, 6,
# 8, 12, and 20 faces. To start with, every die has a probability of 0.2 to be the chosen die. At every
# cast, the probability of each die being the chosen die is updated using Bayes’ rule (find out about
# it if you do not know it). The probabilities are displayed for at most 5 casts. If more than 5 casts
# have been requested, the final probabilities obtained for the chosen number of casts are eventually
# displayed.
from random import choice

dice = [ 4, 6, 8, 12, 20]
possibility_of_outcomes = [0] * max(dice)
hypotheses = [None] * (max(dice)+1)

# the first time possibility of dice chosen 
# [None, None, None, None, 0.2, None, 0.2, None, 0.2, None, None,
#  None, 0.2, None, None, None, None, None, None, None, 0.2]
for i in dice:
	hypotheses[i] = 0.2

chosen_die = choice(dice)
#print(hypotheses)
casts = int(input("Enter the desired number of times a randomly chosen die will be cast:"))
#print(casts)

print("This is a secret, but the chosen die is the one with {} faces".format(chosen_die))

for cast in range(casts):
	for i in range(max(dice)):
		# for example, 
		# possibility_of_outcomes[0] means: the possibility of the outcome = 1
		# possibility_of_outcomes[0] = h(d4)/ 4 + h(d6)/6...+ h(d20)/20
		# h(d4) means the hypothese of the 4 faces cast's outcome = 1
		# As d4 hase 4 faces, each face to be cast is equal = 1/4, 
		# the initial h(d4)=0.2, so do other dice.	
		sum_of_die_hypotheses = 0		
		for die in dice:
			if i < die:
				sum_of_die_hypotheses = sum_of_die_hypotheses + hypotheses[die]/die
		possibility_of_outcomes[i] = sum_of_die_hypotheses 

#	print(possibility_of_outcomes)

	outcome = choice(range(chosen_die))
	for die in dice:
		if outcome >= die:
			hypotheses[die] = 0
		else:
			hypotheses[die] = hypotheses[die] / (die * possibility_of_outcomes[outcome])

#	print(hypotheses)

	if cast < 5:
		print('Casting the chosen die... Outcome: {:}'.format(cast+1))
		print('The updated dice probabilities are:')
		for die in dice:
			print('\t{:2d}: {:.2f}%'.format(die,hypotheses[die] * 100))

		print()

if cast > 5:
    print('The final probabilities are:')             
    for die in dice:
        print('\t{:2d}: {:.2f}%'.format(die, hypotheses[die] * 100))
# Here is a possible output:
# Enter the desired number of times a randomly chosen die will be cast: 2
# This is a secret, but the chosen die is the one with 4 faces
# Casting the chosen die... Outcome: 4
# The updated dice probabilities are:
# 4: 37.04%
# 6: 24.69%
# 8: 18.52%
# 12: 12.35%
# 20: 7.41%
# Casting the chosen die... Outcome: 1
# The updated dice probabilities are:
# 4: 54.18%
# 6: 24.08%
# 8: 13.55%
# 12: 6.02%
# 20: 2.17%