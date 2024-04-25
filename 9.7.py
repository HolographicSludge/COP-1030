def main():
	print()
	# instantiate 2 new students: one w/ some initial quiz scores, and one w/o
	nerd = Student("Nerd", 0.95, 1.00, 0.983)
	jock = Student("Jock")
	# add a few new quiz scores to both students
	nerd.addQuiz(0.89999)
	jock.addQuiz(0.65, 1.10, 0, 0.728)
	# print both students' names, total scores, & avg. scores
	print(f"{nerd.getName()}: {nerd.getAverageScore():.1%} avg., {(nerd.getTotalScore()*100):.1f} pts. total")
	print(f"{jock.getName()}: {jock.getAverageScore():.1%} avg., {(jock.getTotalScore()*100):.1f} pts. total")
	print()
	return


class Student:

	# when creating a new student object, name is required but scores are optional
	def __init__(self, name, *quizScores):
		self._name = name
		self._quizScores = []
		for score in quizScores:
			self.addQuiz(score)
		return

	def getName(self):
		return (self._name).title()
	
	# adds a new score to the list of quiz scores
	def addQuiz(self, *score):
		for x in score:
			# check if each score passed in is a number
			if type(x)==int or type(x)==float:
				# check if each score passed in is a valid percentage
				# (i made the max score 150% instead of 100% since extra credit exists sometimes)
				if x>=0.00 and x<=1.50:
					self._quizScores.append(x)
			# raise exception if an invalid value is passed in
				else: raise ValueError("Quiz scores must be a valid percentage")
			else: raise TypeError("Quiz scores must be a numerical value (int or float)")
		return

	def getTotalScore(self):
		return float(sum(self._quizScores))
	
	def getAverageScore(self):
		import statistics
		return statistics.fmean(self._quizScores)


main()