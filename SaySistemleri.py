print("""Seçmek istediyiniz emeliyyatin kodunu daxil edin:
1 => 2-lik say sisteminden 8-lik say sistemine\t\t2 => 2-lik say sisteminden 10-luq say sistemine
3 => 2-lik say sisteminden 16-lıq say sistemine\t\t4 => 8-lik say sisteminden 2-lik say sistemine
5 => 8-lik say sisteminden 10-luq say sistemine\t\t6 => 8-lik say sisteminden 16-lık say sistemine
7 => 10-luq say sisteminden 2-lik say sistemine\t\t8 => 10-luq say sisteminden 8-lik say sistemine
9 => 10-luq say sisteminden 16-lik say sistemine\t\t10 => 16-lıq say sisteminden 2-lik say sistemine
11 => 16-lıq say sisteminden 8-lik say sistemine\t\t12 => 16-lıq say sisteminden 10-luq say sistemine
13 => Say sistemleri haqqinda ümumi melumat\t\tq => Çıxış
_____________________________________________________________________________________
""")





############################################################  #####   #####  #####   ################################################################################
############################################################  ##  ##  ###    ####    ################################################################################
############################################################  #####   #####  ##      ################################################################################


def _2to8(a):
	allowed = ( "0" , "1")
	while True:
		try:
			if a=='q':
				break

			for i in a:
				if i not in allowed:
					print ("Sadece 0 ve 1-lerden istifade ede bilersiniz!")
					quit()
		
			a=int(a)
			l=list()
		
			while a>0:
				n=a%1000
				if n==1:
					n=1
				elif n==10:
					n=2
				elif n==11:
					n=3
				elif n==100:
					n=4
				elif n==101:
					n=5
				elif n==110:
					n=6
				elif n==111:
					n=7
				l.append(n)
				a=a//1000
			l=l[::-1]
			l = ''.join(map(str, l)) 
			return (l)
			print("___________________________________________________________")
		except ( ValueError ):
			print ("Sadece 0 ve 1-lerden istifade ede bilersiniz!")


##########


def _2to10(a):
	allowed = ('0' , '1')
	while True:
			try:
					result = 0
					l = list()

					for s in a:
							if s not in allowed:
									print("Sadece 0 ve 1-lerden istifade ede bilersiniz!")
									quit()

					if ( a != 'q' ):
							a = int ( a )
							while ( a > 0 ):
									r = a % 10
									a = a // 10
									l.append ( r )
							u = len (l)
							for j in range ( 0 , u ):
									m=l[j]
									if (m==1):
										result = result + (2**j)
							return(result)
							print ("___________________________________________________________")

					else:
							break
				
			except (ValueError):
					print ("Sadece 0 ve 1-lerden istifade ede bilersiniz!")
					print ("___________________________________________________________")


##########
def _2to16(a):
	allowed = ("1" , "0")
	while True:
		try:
			if a=='q':
				break
	
			for s in a:
				if s not in allowed:
					print("Sadece 0 ve 1-lerden istifade ede bilersiniz!")
					quit()

			a=int(a)
			l=list()
	
			while a>0:
				n=a%10000
				if n==1:
					n=1
				elif n==10:
					n=2
				elif n==11:
					n=3
				elif n==100:
					n=4
				elif n==101:
					n=5
				elif n==110:
					n=6
				elif n==111:
					n=7
				elif n==1000:
					n=8
				elif n==1001:
					n=9
				elif n==1010:
					n='A'
				elif n==1011:
					n='B'
				elif n==1100:
					n='C'
				elif n==1101:
					n='D'
				elif n==1110:
					n='E'
				elif n==1111:
					n='F'
	
				l.append(n)
				a=a//10000
			l=l[::-1]
			l = ''.join(map(str, l))
			return(l)
			print("___________________________________________________________")
		except(ValueError):
			print ("Sadece 0 ve 1-lerden istifade ede bilersiniz!")
			print ("___________________________________________________________")


##########


def _8to2(a):
	allowed = ("0","1","2","3","4","5","6","7")
	while True:
		try:
			if (a=="q"):
				break

		
			for i in a:
				if i not in allowed:
					print ("0, 1, 2, 3, 4, 5, 6, 7 reqemlerinden istifade ede bilersiniz!")
					quit()
				
			a=int(a)
			l=list()
			while a>0:
				n=a%10
				if n==0:
					n='000'
				elif n==1:
					n='001'
				elif n==2:
					n='010'
				elif n==3:
					n='011'
				elif n==4:
					n='100'
				elif n==5:
					n='101'
				elif n==6:
					n='110'
				elif n==7:
					n='111'
				l.append(n)
				a=a//10
			
			l=l[::-1]
			l = ''.join(map(str, l))
			return l
			print("___________________________________________________________")
		except ( ValueError ):
			print ("0, 1, 2, 3, 4, 5, 6, 7 reqemlerinden istifade ede bilersiniz!")
			print("___________________________________________________________")


##########


def _8to10(a):
	allowed = ("0","1","2","3","4","5","6","7")
	while True:
		try:
			result = 0
			l = list()

			for s in a:
				if s not in allowed:
					print ("0, 1, 2, 3, 4, 5, 6, 7 reqemlerinden istifade ede bilersiniz!")
					quit()

			if ( a == 'q' ):
				break
			a = int ( a )
			while ( a > 0 ):
				r = a % 10
				a = a // 10
				l.append ( r )
				u = len (l)
				for j in range ( 0 , u ):
					m=l[j]
					if (m==1):
						result = result + 1*(8**j)
					elif (m==2):
						result = result + 2*(8**j)
					elif (m==3):
						result = result + 3*(8**j)
					elif (m==4):
						result = result + 4*(8**j)
					elif (m==5):
						result = result + 5*(8**j)
					elif (m==6):
						result = result + 6*(8**j)
					elif (m==7):
						result = result + 7*(8**j)
					return (result)
					return ("___________________________________________________________")
			  
		except (ValueError):
			print ("0, 1, 2, 3, 4, 5, 6, 7 reqemlerinden istifade ede bilersiniz!")
			print ("___________________________________________________________")


###########


def _8to16(a):
	allowed = ("0","1","2","3","4","5","6","7")
	while True:
		try:
			if (a=="q"):
				break

		
			for i in a:
				if i not in allowed:
					print ("0, 1, 2, 3, 4, 5, 6, 7 reqemlerinden istifade ede bilersiniz!")
					quit()
				
			a=int(a)
			l=list()
			while a>0:
				n=a%10
				if n==0:
					n='000'
				elif n==1:
					n='001'
				elif n==2:
					n='010'
				elif n==3:
					n='011'
				elif n==4:
					n='100'
				elif n==5:
					n='101'
				elif n==6:
					n='110'
				elif n==7:
					n='111'
				l.append(n)
				a=a//10

			
			l=l[::-1]
			l = ''.join(map(str, l))
			a=l
	
			a=int(a)
			c=list()
	
			while a>0:
				n=a%10000
				if n==1:
					n=1
				elif n==10:
					n=2
				elif n==11:
					n=3
				elif n==100:
					n=4
				elif n==101:
					n=5
				elif n==110:
					n=6
				elif n==111:
					n=7
				elif n==1000:
					n=8
				elif n==1001:
					n=9
				elif n==1010:
					n='A'
				elif n==1011:
					n='B'
				elif n==1100:
					n='C'
				elif n==1101:
					n='D'
				elif n==1110:
					n='E'
				elif n==1111:
					n='F'

				c.append(n)
				a=a//10000
			c=c[::-1]
			c = ''.join(map(str, c))
			return(c)
		
		except ( ValueError ):
			print ("0, 1, 2, 3, 4, 5, 6, 7 reqemlerinden istifade ede bilersiniz!")


##########


def _10to2(a):
	while True:
		try:
			l=list()
			if a=="q":
				break
			
			
			a=int(a)
			while a>=0 and a>=1:
				e=a%2
				a=a//2
				l.append(e)
			l=l[::-1]
			l = ''.join(map(str, l))
			return (l)
		except ValueError:
			print("Eded daxil edin herf ya da isare yox.")


##########


def _10to8(a):
	while True:
		try:
			l=list()
			if a=="q":
				break
			else:
				a=int(a)
				while a>=0 and a>=1:
					e=a%8
					a=a//8
					l.append(e)
				l=l[::-1]
				l = ''.join(map(str, l))
				return(l)
		except ValueError:
			print("Eded daxil edin herf ya da isare yox.")


##########


def _10to16(a):
	while True:
		try:
			l=list()
			if a=="q":
				break
			else:
				a=int(a)
				while a>=0 and a>=1:
					e=a%16
					a=a//16
					if e==10:
						e='A'
					if e==11:
						e='B'
					if e==12:
						e='C'
					if e==13:
						e='D'
					if e==14:
						e='E'
					if e==15:
						e='F'
					l.append(e)
				l=l[::-1]
				l = ''.join(map(str, l))
				print(l)
		except ValueError:
			print("Eded daxil edin herf ya da isare yox.")


##########


def _16to8 (a):
	allowed = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f')
	while True:
		try:
			if a=='q':
				break
	
			for s in a:
				if s not in allowed:
					print("sadece 16liq koddan istifade ede bilersiniz!")
					quit()

			l=list(a)
			b=len(a)
			cavab=list()
		
			for i in range (0 , b):
				m=l[i]
				if m=='1':
					n='0001'
				elif m=='2':
					n='0010'
				elif m=='3':
					n='0011'
				elif m=='4':
					n='0100'
				elif m=='5':
					n='0101'
				elif m=='6':
					n='0110'
				elif m=='7':
					n='0111'
				elif m=='8':
					n='1000'
				elif m=='9':
					n='1001'
				elif m=='A' or m=='a':
					n='1010'
				elif m=='B' or m=='b':
					n='1011'
				elif m=='C' or m=='c':
					n='1100'
				elif m=='D' or m=='d':
					n='1101'
				elif m=='E' or m=='e':
					n='1110'
				elif m=='F' or m=='f':
					n='1111'
				cavab.append(n)
			cavab = ''.join(map(str, cavab))

			a=cavab
			a=int(a)
			l=list()
		
			while a>0:
				n=a%1000
				if n==1:
					n=1
				elif n==10:
					n=2
				elif n==11:
					n=3
				elif n==100:
					n=4
				elif n==101:
					n=5
				elif n==110:
					n=6
				elif n==111:
					n=7
				l.append(n)
				a=a//1000
			l=l[::-1]
			l = ''.join(map(str, l)) 
			print(l)
		except ( ValueError ):
			print ("Sadece 0 ve 1-lerden istifade ede bilersiniz!")

def _16to10(a):
	allowed = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f')
	while True:
		try:
			result = 0
			l=list(a)
			b=len(a)
			if ( a == 'q' ):
				break

			for s in a:
				if s not in allowed:
					print ("Sadece 16-lıq say sistemindeki eded ve herflerden istifade ede bilersiniz!")
					quit()
			l=l[::-1]
			for j in range (0 , b):
				m=l[j]
				if (m=='1'):
					result = result + 1*(16**j)
				elif (m=='2'):
					result = result + 2*(16**j)
				elif (m=='3'):
					result = result + 3*(16**j)
				elif (m=='4'):
					result = result + 4*(16**j)
				elif (m=='5'):
					result = result + 5*(16**j)
				elif (m=='6'):
					result = result + 6*(16**j)
				elif (m=='7'):
					result = result + 7*(16**j)
				elif (m=='8'):
					result = result + 8*(16**j)
				elif (m=='9'):
					result = result + 9*(16**j)
				elif (m=='A' or m=='a'):
					result = result + 10*(16**j)
				elif (m=='B' or m=='b'):
					result = result + 11*(16**j)
				elif (m=='C' or m=='c'):
					result = result + 12*(16**j)
				elif (m=='D' or m=='d'):
					result = result + 13*(16**j)
				elif (m=='E' or m=='e'):
					result = result + 14*(16**j)
				elif (m=='F' or m=='f'):
					result = result + 15*(16**j)
			print ("cavab : " , result)
				
		except (ValueError):
			print ("Sadece 16-lıq say sistemindeki eded ve herflerden istifade ede bilersiniz!")
##########


def _16to2(a):
	allowed = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f')
	while True:
		try:
			if a=='q':
				break
	
			for s in a:
				if s not in allowed:
					print("sadece 16liq koddan istifade ede bilersiniz!")
					quit()

			l=list(a)
			b=len(a)
			cavab=list()
	
			for i in range (0 , b):
				m=l[i]
				if m=='1':
					n='0001'
				elif m=='2':
					n='0010'
				elif m=='3':
					n='0011'
				elif m=='4':
					n='0100'
				elif m=='5':
					n='0101'
				elif m=='6':
					n='0110'
				elif m=='7':
					n='0111'
				elif m=='8':
					n='1000'
				elif m=='9':
					n='1001'
				elif m=='A' or m=='a':
					n='1010'
				elif m=='B' or m=='b':
					n='1011'
				elif m=='C' or m=='c':
					n='1100'
				elif m=='D' or m=='d':
					n='1101'
				elif m=='E' or m=='e':
					n='1110'
				elif m=='F' or m=='f':
					n='1111'
				cavab.append(n)
			cavab = ''.join(map(str, cavab))
			print(cavab)
		except(ValueError):
			pass


   

#################################################################  ##  ##   ######    #####   #######################################################################
#################################################################  ####     ##  ##    ##  ##  #######################################################################
#################################################################  ##  ##   ######    #####   #######################################################################

while True:
	try:
		n=input("Emeliyyatı daxil edin...\n=>")
		if (n=='1'):
			a=input("2-lik kodu daxil edin...\n=>")
			print(_2to8(a))
			print("_____________________________________________________________________________________")
		elif (n=='2'):
			a=input("2-lik kodu daxil edin...\n=>")
			print(_2to10(a))
			print("_____________________________________________________________________________________")
		elif (n=='3'):
			a=input("2-lik kodu daxil edin...\n=>")
			print(_2to16(a))
			print("_____________________________________________________________________________________")
		elif (n=='4'):
			a=input("8-lik kodu daxil edin...\n=>")
			print(_8to2(a))
			print("_____________________________________________________________________________________")
		elif (n=='5'):
			a=input("8-lik kodu daxil edin...\n=>")
			print(_8to10(a))
			print("_____________________________________________________________________________________")
		elif (n=='6'):
			a=input("8-lik kodu daxil edin...\n=>")
			print(_8to16(a))
			print("_____________________________________________________________________________________")
		elif (n=='7'):
			a=input("10-luq kodu daxil edin...\n=>")
			print(_10to2(a))
			print("_____________________________________________________________________________________")
		elif (n=='8'):
			a=input("10-luq kodu daxil edin...\n=>")
			print(_10to8(a))
			print("_____________________________________________________________________________________")
		elif (n=='9'):
			a=input("10-luq kodu daxil edin...\n=>")
			print(_10to16(a))
			print("_____________________________________________________________________________________")
		elif (n=='10'):
			a=input("16-lıq kodu daxil edin...\n=>")
			print(_16to2(a))
			print("_____________________________________________________________________________________")
		elif (n=="11"):
			a=input("16-lıq kodu daxil edin...\n=>")
			print(_16to8(a))
			print("_____________________________________________________________________________________")
		elif (n=="12"):
			a=input("16-lıq kodu daxil edin...\n=>")
			print(_16to10(a))
			print("_____________________________________________________________________________________")
		elif (n=="13"):
			print("say sisemleri haqqinda melumat...")
			print("_____________________________________________________________________________________")
		elif (n=='q'):
			quit()
		else:
			print("Düzgün seçim edin!!!")
	except(ValueError):
		print("Düzgün seçim edin...")
