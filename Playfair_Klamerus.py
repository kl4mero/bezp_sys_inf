#!/usr/bin/env python3

klucz=input("Wprowadź proszę klucz:\n")
klucz=klucz.replace(" ", "") #metoda zamiana https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_replace
klucz=klucz.upper() #metoda na duże litery https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_upper

def matrix(x,y,inicjacja):
	return [[inicjacja for i in range(x)] for j in range(y)]

rezultat=list() #lista https://www.w3schools.com/python/trypython.asp?filename=demo_ref_list

#literujemy w kluczu
for c in klucz: 
	if c not in rezultat:
		if c=='J':
			rezultat.append('I')
		else:
			rezultat.append(c)
flaga=0

for i in range(65,91): 
	if chr(i) not in rezultat:
		if i==73 and chr(74) not in rezultat:
			rezultat.append("I")
			flaga=1
		elif flaga==0 and i==73 or i==74:
			pass
		else:
			rezultat.append(chr(i))

#zmienna k - zerowa
k=0
#macierz
macierzLokalna=matrix(5,5,0) 
for i in range(0,5): 
	for j in range(0,5):
		macierzLokalna[i][j]=rezultat[k]
		k+=1
		
def indeksLokalny(c):
	loc=list()
	if c=='J':
		c='I'
	for i ,j in enumerate(macierzLokalna): #numerca listy #https://www.w3schools.com/python/trypython.asp?filename=demo_ref_enumerate
		for k,l in enumerate(j):
			if c==l:
				loc.append(i) #dodawanie do listy https://www.w3schools.com/python/trypython.asp?filename=demo_ref_list_append
				loc.append(k)
				return loc
 
#szyfrowanie			
def szyfruj(): 
	wiadomosc=str(input("Podaj wiadomość:\n"))
	wiadomosc=wiadomosc.upper()
	wiadomosc=wiadomosc.replace(" ", "")             
	i=0
	for s in range(0,len(wiadomosc)+1,2): #len = liczba zankow, elem. #https://www.w3schools.com/python/trypython.asp?filename=demo_ref_len
		if s<len(wiadomosc)-1:
			if wiadomosc[s]==wiadomosc[s+1]:
				wiadomosc=wiadomosc[:s+1]+'X'+wiadomosc[s+1:]
	if len(wiadomosc)%2!=0:
		wiadomosc=wiadomosc[:]+'X'
	print("Zaszyfrowany tekst:\n",end=' ')
	while i<len(wiadomosc):
		loc=list()
		loc=indeksLokalny(wiadomosc[i])
		loc1=list()
		loc1=indeksLokalny(wiadomosc[i+1])
		if loc[1]==loc1[1]:
			print("{}{}".format(macierzLokalna[(loc[0]+1)%5][loc[1]],macierzLokalna[(loc1[0]+1)%5][loc1[1]]),end=' ')
		elif loc[0]==loc1[0]:
			print("{}{}".format(macierzLokalna[loc[0]][(loc[1]+1)%5],macierzLokalna[loc1[0]][(loc1[1]+1)%5]),end=' ')  
		else:
			print("{}{}".format(macierzLokalna[loc[0]][loc1[1]],macierzLokalna[loc1[0]][loc[1]]),end=' ')    
		i=i+2        
	
#odszyfruj
def odszyfruj():  
	wiadomosc=str(input("Podaj zaszyfrowaną wiadomość:\n"))
	wiadomosc=wiadomosc.upper()
	wiadomosc=wiadomosc.replace(" ", "")
	print("Pierwotna wiadomość:",end=' ') 
	i=0
	while i<len(wiadomosc):
		loc=list()
		loc=indeksLokalny(wiadomosc[i])
		loc1=list()
		loc1=indeksLokalny(wiadomosc[i+1])
		if loc[1]==loc1[1]:
			print("{}{}".format(macierzLokalna[(loc[0]-1)%5][loc[1]],macierzLokalna[(loc1[0]-1)%5][loc1[1]]),end=' ')
		elif loc[0]==loc1[0]:
			print("{}{}".format(macierzLokalna[loc[0]][(loc[1]-1)%5],macierzLokalna[loc1[0]][(loc1[1]-1)%5]),end=' ')  
		else:
			print("{}{}".format(macierzLokalna[loc[0]][loc1[1]],macierzLokalna[loc1[0]][loc[1]]),end=' ')    
		i=i+2
		
while(1):
	wyborMenu=int(input("\n Wybierz opcję:\n 1.Szyfruj \n 2.Odszyfruj \n 3.EXIT!\n"))
	if wyborMenu==1:
		szyfruj()
	elif wyborMenu==2:
		odszyfruj()
	elif wyborMenu==3:
		exit()
	else:
		print("\n Popraw odpowiedź, wprowadź: \n 1.Szyfruj \n 2.Odszyfruj \n 3.EXIT!\n")
		