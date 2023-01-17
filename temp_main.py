import matplotlib.pyplot as plt

import random
import numpy as np


STEPS = 100
NUM_MEMBERS = 1000
NUM_SKILLS = 3


def random_activity() -> list:
	return [random.random() for _ in range(NUM_SKILLS)]


def calc_progress(member, activity) -> float:
	return max(np.dot(member, activity), 0.0)


def best_member_for(activity, members) -> float:
	dot_products = []
	for m in members:
		dot_products.append(np.dot(m, activity))

	max_dot_product = max(dot_products)
	index = dot_products.index(max_dot_product)

	best = members[index]

	return best


def main() -> None:
	members = list()

	# Initialise the organisation
	for m in range(NUM_MEMBERS):
		new_member = [random.random() for _ in range(NUM_SKILLS)]
		members.append(new_member)

	# Run simulation
	cond_1 = 0.0
	cond_1_history = [cond_1]

	cond_2 = 0.0
	cond_2_history = [cond_2]

	for s in range(STEPS):
		activity = random_activity()

		# Condition 1
		random_member_1 = random.choice(members)
		cond_1 += calc_progress(activity, random_member_1)
		cond_1_history.append(cond_1)

		# Condition 2
		chosen_member = best_member_for(activity, members)
		cond_2 += calc_progress(activity, chosen_member)
		cond_2_history.append(cond_2)

	plt.plot(list(range(len(cond_1_history))), cond_1_history, 'r')
	plt.plot(list(range(len(cond_1_history))), cond_2_history, 'b')
	plt.show()



if __name__ == '__main__':
	main()