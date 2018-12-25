def get_input(filename):
	with open('input/' + filename) as f:
		content = [line.strip() for line in f.readlines()]
	return content