# First Turing Machine Simulator

# I have not learned how to label Turing Machines but when I do I will be able to label this one

# This one prints 01010101010101010 ...

# Found in Petzold book

# This machine has four m-configurations: b, c, k, e and can print two symbols 0, and 1
#######################################################################################
# 		Configuration 								Behaviour
# 	m-config.		symbol 					operations		final m-config.
# 		b 				None					P0, R 			c
#  		c 				None 					R 				e
# 		e 				None 					P1, R 			k
# 		k 				None 					R 				b
#######################################################################################

print('Hey there')