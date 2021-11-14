import fonctions as fct


n, p, q = fct.getBobParameters()
phi, e, d = fct.getAliceParameters(p, q)

cryptMessage = fct.encryptMessage(n, e)
decryptedMessage = fct.decryptMessage(cryptMessage, n, d)
print('Decrypted message : ' + str(decryptedMessage))


crackedMessage = fct.crackMessage(cryptMessage, n, e)
print('Cracked message : ' + str(crackedMessage))