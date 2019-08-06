import pip
with open("real-requirements.txt") as f:
    for line in f:
		print line
        # call pip's main function with each requirement
        pip.main(['install','-U', line])