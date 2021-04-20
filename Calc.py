"Invert Keys and Values"
def invert(d):
	return {v: k for k, v in d.items()}

"Date Format"
def format_date(date):
    	return ''.join(reversed(date.split('/')))

"Expensive Orders"
def expensive_orders(d, p):
    	return {k: v for k, v in d.items() if v > p}

"Emphasise the Words"    
def emphasise(txt):
    	return ' '.join(w[0].upper()+w[1:].lower() for w in txt.split())

"Reversible Inclusive List Ranges"
def reversible_inclusive_list(s, e):
    	return list(range(s, e+1)) or list(range(s, e-1, -1))
