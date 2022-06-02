# First Turing Machine Simulator

# I have not learned how to label Turing Machines but when I do I will be able to label this one

# This one prints 01010101010101010 ...

# Found in Petzold book

# This machine has four m-configurations: b, c, k, e and can print two symbols 0, and 1
# P0 means print 0 on tape, R means move right one square on tape; P1 prints a 1, instead
#######################################################################################
# 		Configuration 								Behaviour
# 	m-config.		symbol 					operations		final m-config.
# 		b 				None					P0, R 			c
#  		c 				None 					R 				e
# 		e 				None 					P1, R 			k
# 		k 				None 					R 				b
#######################################################################################

# Implementation mapping of the Turing Tape.
# On the one hand there is the Turing Tape- entries in this case can be None, 0, or 1.
# On the other hand there is how we can implement the Turing Tape. Here is the implementation
# 	which maybe needs to be improved later:
#	
#	an 'X' means None
# 	a position in the array that does not exist yet is the same as a None in that position
#	for purposes of memory, this simulator will only create positions in the array when needed


tape = ['X'] # Turing machine tape starts with a single None value
head_position = 0 # Turing Machine head starts at position 0 on the initialized None value

lifetime = 100 # Number of Turing Machine steps before discontinuing to avoid infinite loops
age = 0 # Turing machine step counter

m_config = 'b' # Initialize m-config

while age < lifetime:
	if m_config == 'b':
		tape[head_position] = '0'
		m_config = 'c'

	elif m_config == 'c':
		m_config = 'e'

	elif m_config == 'e':
		tape[head_position] = '1'
		m_config = 'k'

	else:
		m_config = 'b'

	head_position += 1
	tape.append('X')
	print(tape)
	age += 1





