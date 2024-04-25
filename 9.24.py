def main():
	print()
	# instantiate a new message object
	msg = Message("John Smith", "Jane Doe")
	# add a few lines to the message
	msg.append("Good morning,", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.", "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu.", "Sincerely, John")
	# print the complete message
	print(msg.toString())
	print()


class Message:

	def __init__(self, sender, recipient):
		self._sender = sender
		self._recipient = recipient
		self._body = []
		return

	def getSender(self):
		return self._sender
	
	def getRecipient(self):
		return self._recipient
	
	def getBody(self):
		return self._body
	
	def getBody(self, lineNum):
		return self._body[lineNum]

	# appends each arg to the message's body
	# (i made append use a *arg b/c lazy lol)
	def append(self, *newLine):
		for line in newLine:
			self._body.append(str(line).strip())
		return

	# returns the complete message as a single string
	def toString(self):
		# copy sender & recipient to a string var
		msgString = f"From: {self._sender}\nTo: {self._recipient}\n"
		# appends each line in the body to the string, preceded by a linefeed
		for line in self._body:
			msgString += '\n' + str(line)
		# return the complete message string
		return msgString


main()