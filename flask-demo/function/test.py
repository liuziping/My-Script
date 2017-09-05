def maker(M):
	def action(X):
		return X**M
	
	return action

f = maker(3)
print f(2)
