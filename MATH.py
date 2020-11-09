from math import sin, cos, tan, sqrt, pi
print("""#############################################################################
#\t\t\t\t\t\t\t\t\t          #
#\t\t\tRIYAZIYYAT ELMLERIN AÇARIDIR\t\t\t          #
#\t\t\t\t\t\t\t\t\t          #
#############################################################################""")
while True:
    print("""
-----------------------------------------------------------------------------------------------------------------------------------------

Seçmek istediyiniz riyazi emelin kodunu seçim yerine yazın:
1 => CEBR\t\t\t2 => HENDESE\t\t\t3 => ÇIXIŞ
""")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def toplama(a,b):
        return a+b

    
    def cixma(a,b):
        return a-b


    def vurma(a,b):
        return a*b


    def bolme(a,b):
        return a/b


    def kok(a,b):
        b=1/b
        return a**b


    def faktorial(a):
        for i in range (1,a):
            a=a*i
        return a


    def qy(a,b):
        return a**b


    def sinus(a):
        return sin(a)


    def kosinus(a):
        return cos(a)


    def tg(a):
        return tan(a)


    def dasahe(r):
        return pi*r*r


    def dauzun(r):
        return 2*pi*r


    def pifaqorhip(a,b):
        c=sqrt(a*a+b*b)
        return c
    def pifaqorkat(a,c):
        b=sqrt(c*c-a*a)
        return b


    def ucbucaqsahe(a,b,c):
        q=(a+b+c)/2
        return sqrt(q*(q-a)*(q-b)*(q-c))


    def parsahe(d1,d2):
        return (d1*d2)/2
    def parsahe2(a,ha):
        return a*ha


    def paraseth(a,b,c):
        return 2*(a*b+b*c+a*c)


    def parahecm(a,b,c):
        return a*b*c


    def silseth (r,h):
        a= 2*pi*r*r + 2*pi*r*h
        return a


    def silhecm (r,h):
        return pi*r*r*h


    def konusseth(r,l):
        return pi*r*r+pi*r*l


    def konushecm(r,h):
        return (1/3)*pi*r*r*h


    def pirseth (a,b,l):
        return (2/1)*(a+b)*l + (a*b)


    def pirhecm (a,b,h):
        return (1/3)*a*b*h


    def kureseth (r):
        return (4/3)*pi*r*r*r


    def kurehecm (r):
        return 4*pi*r*r
    

#----------------------------------------------------------------------------------------------------------------CEBR-------------------------------------------------------------------------------------------------------


    o=input('SEÇİM => ')
    if o=="1":
        print("""1 => Toplama\t\t\t2 => Çıxma
3 => Vurma\t\t\t4 => Bölme
5 => Kök alma\t\t\t6 => Faktorial
7 => Qüvvete yükseltme\t\t8 => Sinus                                                    
9 => Kosinus\t\t\t10 => Tangens                                               
11 => EBOB\t\t\t12 => EKOB
13 => Kvadrat tenliyin helli""")

        
        s=input('SEÇİM => ')
        if s=='1':
            e1=float(input('1-ci ededi daxil edin => '))
            e2=float(input('2-ci ededi daxil edin => '))
            print(toplama(e1,e2))

            
        elif s=='2':
            e1=float(input('1-ci ededi daxil edin => '))
            e2=float(input('2-ci ededi daxil edin => '))
            print(cixma(e1,e2))

            
        elif s=='3':
            e1=float(input('1-ci ededi daxil edin => '))
            e2=float(input('2-ci ededi daxil edin => '))
            print(vurma(e1,e2))

            
        elif s=='4':
            e1=float(input('1-ci ededi daxil edin => '))
            e2=float(input('2-ci ededi daxil edin => '))
            print(bolme(e1,e2))

            
        elif s=='5':
            e1=float(input('Kök almaq istediyin ededi daxil edin => '))
            e2=float(input('Neçe dereceden kök almaq istediyinizi daxil edin => '))
            print(kok(e1,e2))

            
        elif s=='6':
            e1=int(input('Ededi daxil edin => '))
            print(faktorial(e1))

            
        elif s=='7':
            e1=float(input('Qüvvete yükseltmek istediyiniz ededi daxil edin => '))
            e2=float(input('Neçe dereceden qüvvete yükseltmek istediyinizi daxil edin => '))
            print(qy(e1,e2))

            
        elif s=='8':
            e1=float(input('Ededi daxil edin (rad) => '))
            print(sinus(e1))

            
        elif s=='9':
            e1=float(input('Ededi daxil edin (rad) => '))
            print(kosinus(e1))

            
        elif s=='10':
            e1=float(input('Ededi daxil edin (rad) => '))
            print(tg(e1))

#EBOB
        elif s=='11':
            a=int(input('1-ci ededi daxil et => '))
            b=int(input('2-ci ededi daxil et => '))
            l=list()
            if a>b:
                for i in range (1,a+1):
                    if a%i==0 and b%i==0:
                        l.append(i)
                print(max(l))
            elif a<b:
                for j in range (1,b+1):
                    if a%j==0 and b%j==0:
                        l.append(j)
                print(max(l))

#EKOB
        elif s=='12':
            a=int(input('1-ci ededi daxil et => '))
            b=int(input('2-ci ededi daxil et => '))
            l=list()
            if a>b:
                for i in range (a,a*b+1):
                    if i%a==0 and i%b==0:
                        l.append(i)
                print(min(l))
            elif a<b:
                for j in range (b,a*b+1):
                    if j%a==0 and j%b==0:
                        l.append(j)
                print(min(l))


        elif s=='13':
            a=float(input('a-nı daxil edin => '))
            b=float(input('b-ni daxil edin => '))
            c=float(input('c-ni daxil edin => '))
            d=b*b-4*a*c
            if d>0:
                x1=(-b+sqrt(d))/(2*a)
                x2=(-b-sqrt(d))/(2*a)
                print(x1,' ',x2)
            elif d==0:
                x1=x2=(-b)/(2*a)
                print(x1)
            else:
                print('Tam helli yoxdur')
        else:
            print('Düzgün seçim edin.')

#-----------------------------------------------------------------------------------------------------------HENDESE------------------------------------------------------------------------------------------------------- 

    elif o=="2":
        print("""1 => Üçbucağın sahesi\t\t2 => Paraleloqramın sahesi
3 => Paralelpiped\t\t\t4 => Silindr
5 => Konus\t\t\t6 => Piramida
7 => Küre\t\t\t\t8 => Pifaqor teoremi
9 => Dairenin sahesi\t\t10 => Çevrenin uzunluğu""")
        s=input('SEÇİM => ')
        if s=='1':
            print('1 => (a,b,c) istifade olunsun                          2 => (a,ha) istifade olunsun')
            print('3 => (a,b,bucaq ab) istifade olunsun')
            e=int(input('SEÇİM => '))
            if e==1:
                a=float(input('a => '))
                b=float(input('b => '))
                c=float(input('c => '))
                print('Cavab => ',ucbucaqsahe(a,b,c))
            elif e==2:
                a=float(input('a='))
                ha=float(input('a terefine cekilmis hundurluk => '))
                print('Cavab => ',(1/2)*a*ha)
            elif e==3:
                a=float(input('a = '))
                b=float(input('b = '))
                ab=float(input('bucaq ab= '))
                print('Cavab => ',(1/2)*a*b*sin(ab))
            else:
                print('Duzgun secim edin.')

                
        elif s=='2':
            print('1 => (d1,d2) istifade olunsun                            2 => (a,ha) istifade olunsun')
            e=int(input('SEÇİM => '))
            if e==1:
                d1=float(input('d1-i daxil edin => '))
                d2=float(input('d2-i daxil edin => '))
                print('Cavab => ',parsahe(d1,d2))
            elif e==2:
                 a=float(input('a = '))
                 ha=float(input('a terefine cekilmis hundurluk => '))
                 print('Cavab => ',parsahe2(a,ha))
            else:
                print('Duzgun secim edin.')

                
        elif s=='3':
            print('1 => Sethinin sahesi\t\t\t2 => Hecmi')
            e=int(input('SEÇİM => '))
            if e==1:
                a=float(input('a='))
                b=float(input('b='))
                c=float(input('c='))
                print('Cavab => ',paraseth(a,b,c))
            elif e==2:
                a=float(input('a='))
                b=float(input('b='))
                c=float(input('c='))
                print('Cavab => ',parahecm(a,b,c))
            else:
                print('Duzgun secim edin.')

                
        elif s=='4':
            print('1 => Sethinin sahesi\t\t\t2 => Hecmi')
            e=int(input('SEÇİM => '))
            if e==1:
                r=float(input('radius =>  '))
                h=float(input('h='))
                print('Cavab => ',silseth (r,h))
            elif e==2:
                r=float(input('radius =>  '))
                h=float(input('hundurluk => '))
                print('Cavab => ',silhecm(r,h))
            else:
                print('Duzgun secim edin.')

                
        elif s=='5':
            print('1 => Sethinin sahesi\t\t\t2 => Hecmi')
            e=int(input('SEÇİM => '))
            if e==1:
                r=float(input('radius =>  '))
                l=float(input('apofemin uzunlugunu daxil edin => '))
                print('Cavab => ',konusseth(r,l))
            elif e==2:
                r=float(input('radius =>  '))
                l=float(input('apofemin uzunlugunu daxil edin => '))
                print('Cavab => ', konushecm(r,l))
            else:
                print('Duzgun secim edin.')

                
        elif s=='6':
            print('1 => Sethinin sahesi\t\t\t2 => Hecmi')
            e=int(input('SEÇİM => '))
            if e==1:
                r=float(input('radius =>  '))
                h=float(input('hundurluk => '))
                print('Cavab => ',silseth (r,h))
            elif e==2:
                r=float(input('radius =>  '))
                h=float(input('hundurluk => '))
                print('Cavab => ',silhecm (r,h))
            else:
                print('Duzgun secim edin.')

                
        elif s=='7':
            print('1 => Sethinin sahesi\t\t\t2 => Hecmi')
            e=int(input('SEÇİM => '))
            if e==1:
                r=float(input('radius =>  '))
                print('Cavab => ',kureseth (r))
            elif e==2:
                r=float(input('radius => '))
                print('Cavab => ',kurehecm(r))
            else:
                print('Duzgun secim edin.')

                
        elif s=='8':
            print('1 => hipotenuzun tapilmasi          2 => katetin tapilmasi')
            e=int(input('SEÇİM => '))
            if e==1:
                a=float(input('1-ci kateti daxil edin => '))
                b=float(input('2-ci kateti daxil edin => '))
                print(pifaqorhip(a,b))
            elif e==2:
                a=float(input('kateti daxil et => '))
                c=float(input('hipotenuzu daxil edin => '))
                print(pifaqorkat(a,c))
            else:
                print('Duzgun secim edin.')


        elif s=='9':
            r=float(input('Radiusu daxil edin => '))
            print(dasahe(r))

        elif s=='10':
            r=float(input('Radiusu daxil edin => '))
            print(dauzun(r))
            

        else:
            print('Duzgun secim edin.')

                
    elif o=="3":
        break

    
    else:
        print("Duzgun secim edin.")
