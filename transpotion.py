import math

key = input("Enter Key :- ")

# Decryption code
def decryptMessage(cipher):
	msg = ""
	k_indx = 0

	# track msg indices
	msg_indx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)

	# calculate column of the matrix
	col = len(key)	
	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))
	key_lst = sorted(list(key))

	# create an empty matrix to
	# store deciphered message
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	# Arrange the matrix column wise according
	# to permutation order by adding into new matrix
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1

	# convert decrypted msg matrix into a string
	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot",
						"handle repeating words.")

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg

# Driver Code
msg = input("Enter message for encrept:- ")

cipher = encryptMessage(msg)
print("Encrypted Message: {}".
			format(cipher))

print("Decryped Message: {}".
	format(decryptMessage(cipher)))

# This code is contributed by Aditya K
