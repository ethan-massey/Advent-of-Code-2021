
''' PART 1 '''
def get_increasing_depths(datafile):

	depths = open(datafile, "r").readlines()

	# total of measurements > than previous measurement
	total = 0

	for i in range(1, len(depths)):
		format_depth = int(depths[i].strip('\n'))
		prev_format_depth = int(depths[i-1].strip('\n'))
		# if measurement > previous measurement
		if format_depth > prev_format_depth:
			total += 1

	return total


print(get_increasing_depths("depths.txt"))

###################################################################
''' PART 2 '''

# window of size 3
def get_increasing_window_depths(datafile):

	depths = open(datafile, "r").readlines()
	# format lines because I'm tired of typing so much
	for i in range(0, len(depths)):
		depths[i] = int(depths[i].strip('\n'))

	# total of measurements > than previous measurement
	total = 0
	# get first window
	current_sum = sum([depths[0], depths[1], depths[2]])
	previous_sum = current_sum

	for i in range(3, len(depths)):
		# shift
		current_sum -= depths[i-3]
		current_sum += depths[i]

		if(current_sum > previous_sum):
			total += 1

		previous_sum = current_sum

	return total

print(get_increasing_window_depths("depths.txt"))
