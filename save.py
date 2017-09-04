import shelve

FILENAME = 'score'

def save_score(data):

	filename = 'score_list'
	key = 'x'
	d = shelve.open(FILENAME)
	d[key] = data   
	d.close()

def load_score():
	
	filename = 'score_list'
	key = 'x'
	d = shelve.open(FILENAME)
	data = d[key]
	d.close()
	return data
