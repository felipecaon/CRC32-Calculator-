#definindo polinomio para calculo de um CRC de 32 bits 
#1110 1101 1011 1000 1000 0011 0010 0000
#Fonte: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
POLINOMIO = 0xEDB88320

def crc32(palavra):
	#criando tabela do crc com 256 posicoes
	tabelaCRC = [0]*256

	#inicia construcao da tabela CRC32
	for i in range(256):
		posicao = i
		for j in range(8):
			if posicao & 1: #operador & realiza AND
				posicao = (posicao >> 1) ^ POLINOMIO #realiza shift de bits
			else:
				posicao >>= 1 #realiza shift de bits
		tabelaCRC[i] = posicao

	#0000 0000 1111 1111 1111 1111 1111 1111 1111 1111
	crc = 0xffffffff
	for c in palavra:
		crc = (crc >> 8) ^ tabelaCRC[(crc ^ ord(c)) & 0xff]
	return hex(crc ^ 0xfffffffF)

resultado = crc32("felipe")
print resultado.upper()