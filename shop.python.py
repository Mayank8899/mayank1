print('            Welcome To Shop  ')
print('Pick The Option ')
def main():
    print('Press 1:-- For Enter in The Menu Of Store')
    print('Press 0:-- For Exit The Store')
main()
x=int(input('Pick Your Option:--'))
while x!=0:
    if(x==1):
        print('Press 1:-- for Mobile' )
        print('Press 2:-- for headset')
        print('Press 3:-- for Laptop')

        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Mobile~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        a=int(input('Pick Your option :-'))
        if(a==1):
            print('Press 1. for Poco')
            print('Press 2. for Redmi')
            print('Press 3. for OnePlus')
            b=int(input('Enter Your Choice :-'))
            if(b==1):
                print('DIWALI OFFER 1O% OFF in POCO Phone')
                print('Press 1. for  POCO F1')
                print('Press 2. for  POCO F2')
                print('Press 3. for  POCO F3')
                c=int(input('Enter Your Choice :-'))          
                if(c==1):
                    print('Press 1. for POCO F1 Blue ')
                    print('Press 2. for POCO F1 Red ')
                    print('Press 3. for POCO F1 Black')
                    d=int(input('Enter Your Choice d :-'))
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F1 Blue is 18k  ')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F1 Blue is 20k')
                        e=int(input('Enter The variant of POCO F1 Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F1 Blue :-'))
                            f=18000
                            print('Price for 6GB/128GB Storage Variant for POCO F1 Blue is Rs:-',f)
                            g=18000*z
                            print('Price for Quantity of 6GB/128GB Storage Variant for POCO F1 Blue is Rs:-'
                                  ,g)
                            h=g*10/100
                            i=g-h
                            j=i*20/100
                            k=i-j
                            L=g*5/100
                            T1=k+L
                            print('DIWALI OFFER 10% OFF ')
                            print('DIWALI OFFER Price for POCO F1 Blue                     Rs:- -',h)
                            print('Additional Discount 20%                                 Rs:- -',j)
                            print('GSt 5%                                                  Rs:- +',L)
                            print('Total Amount is     Rs:-   ',T1)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F1 Blue :-'))
                            f=20000
                            g=20000*z
                            print('Price for 8GB/256GB Storage Variant for POCO F1 Blue is Rs:-',f)
                            print('Price for Quantity of 8GB/256GB Storage Variant for POCO F1 Blue is Rs:-'
                                  ,g)
                            h=g*10/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 10% OFF ')
                            print('DIWALI OFFER Price for POCO F1 Blue                     Rs:- -',h)
                            print('Additional Discount 10%                                 Rs:- -',j)
                            print('GSt 5%                                                  Rs:- +',L)
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                            
                                     
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F1 Red is 19k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F1 Red is 21k')
                        e=int(input('Enter The variant of POCO F1 Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F1 Red :-'))
                            if(5>z):
                                f=19000
                                g=19000*z
                                print('Price for 6GB/128GB Storage Variant for POCO F1 Red is Rs:-',f)
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F1 red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*12/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Red                      Rs:- -',h)
                                print('Additional Discount 12%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=19000
                                g=19000*z
                                print('Price for 6GB/128GB Storage Variant for POCO F1 Red is Rs:-',f)
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F1 red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Red                      Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F1 Red :-'))
                            if(5>z):
                                f=21000
                                g=21000*z
                                print('Price for 8GB/256GB Storage Variant for POCO F1 Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F1 red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*10/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Red                      Rs:- -',h)
                                print('Additional Discount 10%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=21000
                                g=21000*z
                                print('Price for 8GB/256GB Storage Variant for POCO F1 Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F1 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*12/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Red                      Rs:- -',h)
                                print('Additional Discount 12%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                        else:
                            print()
                            print()
                            hello()
                            d=int(input('Enter Your Choice d :-'))       

                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F1 Black is 15k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F1 Black is 16k')
                        e=int(input('Enter The variant of POCO F1 Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F1 Black :-'))
                            if(5>z):
                                f=15000
                                g=15000*z
                                print('Price for 6GB/128GB Storage Variant for POCO F1 Black is Rs:-',f)
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F1 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*5/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Black                      Rs:- -',h)
                                print('Additional Discount 5%                                    Rs:- -',j)
                                print('GSt 5%                                                    Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=15000
                                g=15000*z
                                print('Price for 6GB/128GB Storage Variant for POCO F1 Black is Rs:-',f)
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F1 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*10/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Black                    Rs:- -',h)
                                print('Additional Discount 10%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                          
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F1 Black :-'))
                            if(5>z):
                                f=16000
                                g=16000*z
                                print('Price for 8GB/256GB Storage Variant for POCO F1 Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F1 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*8/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Black                      Rs:- -',h)
                                print('Additional Discount 8%                                    Rs:- -',j)
                                print('GSt 5%                                                    Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=16000
                                g=16000*z
                                print('Price for 8GB/256GB Storage Variant for POCO F1 Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F1 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*12/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F1 Black                      Rs:- -',h)
                                print('Additional Discount 12%                                   Rs:- -',j)
                                print('GSt 5%                                                    Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                if(c==2):
                    print('Press 1. for POCO F2 blue ')
                    print('Press 2. for POCO F2 red ')
                    print('Press 3. for POCO F2 black')
                    d=int(input('Enter Your Choice  :-'))
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F2 Blue is 30k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F2 Blue is 35k')
                        e=int(input('Enter The variant of POCO F2 Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F2 Blue :-'))
                            if(5>z):
                                f=30000
                                print('price for 6GB/128GB Storage Variant for POCO F2 Blue is Rs:-',f)
                                g=30000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F2 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*12/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Blue                     Rs:- -',h)
                                print('Additional Discount 12%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=30000
                                print('Price for 6GB/128GB Storage Variant for POCO F2 Blue is Rs:-',f)
                                g=30000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F2 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Blue                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F2 Blue :-'))
                            if(5>z):
                                f=35000
                                print('Price for 8GB/256GB Storage Variant for POCO F2 Blue is Rs:-',f)
                                g=35000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F2 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*10/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Blue                     Rs:- -',h)
                                print('Additional Discount 10%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=20000
                                g=20000*z
                                print('Price for 8GB/256GB Storage Variant for POCO F2 Blue is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F2 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Blue                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F2 Red is 32k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F2 Red is 36k')
                        e=int(input('Enter The variant of POCO F2 Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F2 Red :-'))
                            if(5>z):
                                f=32000
                                print('price for 6GB/128GB Storage Variant for POCO F2 Red is Rs:-',f)
                                g=32000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F2 red  is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*10/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 red                      Rs:- -',h)
                                print('Additional Discount 10%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=32000
                                print('Price for 6GB/128GB Storage Variant for POCO F2 red is Rs:-',f)
                                g=32000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F2 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*12/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Red                      Rs:- -',h)
                                print('Additional Discount 12%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F2 Red :-'))
                            if(5>z):
                                f=36000
                                print('Price for 8GB/256GB Storage Variant for POCO F2 Red is Rs:-',f)
                                g=36000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F2 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*10/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Red                      Rs:- -',h)
                                print('Additional Discount 10%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=20000
                                g=20000*z                        
                                print('Price for 8GB/256GB Storage Variant for POCO F2 Red  is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F2 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Red                      Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F2 Black is 40k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F2 Black is 42k')
                        e=int(input('Enter The variant of POCO F2 Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F2 Black :-'))
                            if(5>z):
                                f=40000
                                print('price for 6GB/128GB Storage Variant for POCO F2 Black is Rs:-',f)
                                g=40000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F2 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*5/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Black                    Rs:- -',h)
                                print('Additional Discount 5%                                  Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=40000
                                print('Price for 6GB/128GB Storage Variant for POCO F2 Black is Rs:-',f)
                                g=40000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F2 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*12/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Black                    Rs:- -',h)
                                print('Additional Discount 12%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F2 Black :-'))
                            if(5>z):
                                f=42000
                                print('Price for 8GB/256GB Storage Variant for POCO F2 Black is Rs:-',f)
                                g=42000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F2 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*5/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 Black                    Rs:- -',h)
                                print('Additional Discount 5%                                  Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=42000
                                g=42000*z                        
                                print('Price for 8GB/256GB Storage Variant for POCO F2 Black  is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F2 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*10/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F2 black                    Rs:- -',h)
                                print('Additional Discount 10%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                if(c==3):
                    print('Press 1. for POCO F3 blue ')
                    print('Press 2. for POCO F3 red ')
                    print('Press 3. for POCO F3 black')
                    d=int(input('Enter Your Choice  :-')) 
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F3 Blue is 20k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F3 Blue is 21k')
                        e=int(input('Enter The variant of POCO F3 Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F3 Blue :-'))
                            if(5>z):
                                f=20000
                                print('price for 6GB/128GB Storage Variant for POCO F3 Blue is Rs:-',f)
                                g=20000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F3 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Blue                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=20000
                                print('Price for 6GB/128GB Storage Variant for POCO F3 Blue is Rs:-',f)
                                g=20000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F3 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Blue                     Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F3 Blue :-'))
                            if(5>z):
                                f=21000
                                print('Price for 8GB/256GB Storage Variant for POCO F3 Blue is Rs:-',f)
                                g=21000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F3 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*5/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Blue                     Rs:- -',h)
                                print('Additional Discount 5%                                  Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=21000
                                g=21000*z                        
                                print('Price for 8GB/256GB Storage Variant for POCO F3 Blue  is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F3 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*10/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Blue                     Rs:- -',h)
                                print('Additional Discount 10%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')     
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F3 Red is 30k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F3 Red is 36k')
                        e=int(input('Enter The variant of POCO F3 Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F3 Red :-'))
                            if(5>z):
                                f=30000
                                print('price for 6GB/128GB Storage Variant for POCO F3 Red is Rs:-',f)
                                g=30000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F3 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Red                      Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=30000
                                print('Price for 6GB/128GB Storage Variant for POCO F3 Red is Rs:-',f)
                                g=30000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F3 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Red                      Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F3 Red :-'))
                            if(5>z):
                                f=36000
                                print('Price for 8GB/256GB Storage Variant for POCO F3 Red is Rs:-',f)
                                g=36000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F3 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Red                      Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=36000
                                g=36000*z                        
                                print('Price for 8GB/256GB Storage Variant for POCO F3 Red  is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F3 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Red                      Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                                print('Including GST')     
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for POCO F3 Black is 40k')
                        print('Press 2. for  8GB/256GB Storage Variant for POCO F3 Black is 46k')
                        e=int(input('Enter The variant of POCO F3 Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for POCO F3 Black :-'))
                            if(5>z):
                                f=40000
                                print('price for 6GB/128GB Storage Variant for POCO F3 Black is Rs:-',f)
                                g=40000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F3 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Black                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=40000
                                print('Price for 6GB/128GB Storage Variant for POCO F3 Black is Rs:-',f)
                                g=40000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for POCO F3 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Black                      Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for POCO F3 Black :-'))
                            if(5>z):
                                f=46000
                                print('Price for 8GB/256GB Storage Variant for POCO F3 Black is Rs:-',f)
                                g=46000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F3 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Black                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=46000
                                g=46000*z                        
                                print('Price for 8GB/256GB Storage Variant for POCO F3 Black  is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for POCO F3 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for POCO F3 Black                    Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
            if(b==2):
                print('DIWALI OFFER 2O% OFF in REDMI Phone')
                print('Press 1. for  REDMI 11')
                print('Press 2. for  REDMI 12')
                print('Press 3. for  REDMI 13')
                c=int(input('Enter Your Choice :-'))
                if(c==1):
                    print('Press 1. for REDMI 11 blue ')
                    print('Press 2. for REDMI 11 red ')
                    print('Press 3. for REDMI 11 black')
                    d=int(input('Enter Your Choice  :-')) 
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 11 Blue is 20k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 11 Blue is 21k')
                        e=int(input('Enter The variant of REDMI 11 Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 11 Blue :-'))
                            if(5>z):
                                f=20000
                                print('price for 6GB/128GB Storage Variant for REDMI 11 Blue  is Rs:-',f)
                                g=20000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 11 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Blue                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=20000
                                print('Price for 6GB/128GB Storage Variant for REDMI 11 Blue is Rs:-',f)
                                g=20000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 11 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Blue                    Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 11 Blue :-'))
                            if(5>z):
                                f=21000
                                print('Price for 8GB/256GB Storage Variant for REDMI 11 Blue is Rs:-',f)
                                g=21000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 11 BLUE is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Blue                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)

                                print('Including GST')
                            if(5<=z):
                                f=21000
                                g=21000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 11 Blue is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 11 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Blue                    Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 11 Red is 22k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 11 Red is 24k')
                        e=int(input('Enter The variant of REDMI 11 Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 11 Red  :-'))
                            if(5>z):
                                f=22000
                                print('price for 6GB/128GB Storage Variant for REDMI 11 Red  is Rs:-',f)
                                g=22000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 11 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Red                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=22000
                                print('Price for 6GB/128GB Storage Variant for REDMI 11 Red is Rs:-',f)
                                g=22000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 11 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Red                     Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                         
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 11 Red :-'))
                            if(5>z):
                                f=24000
                                print('Price for 8GB/256GB Storage Variant for REDMI 11 Red is Rs:-',f)
                                g=24000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 11 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Red                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=24000
                                g=24000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 11 Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 11 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Red                     Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 11 Black is 25k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 11 Black is 28k')
                        e=int(input('Enter The variant of REDMI 11 Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 11 Black  :-'))
                            if(5>z):
                                f=25000
                                print('price for 6GB/128GB Storage Variant for REDMI 11 Black  is Rs:-',f)
                                g=25000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 11 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Black                   Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=25000
                                print('Price for 6GB/128GB Storage Variant for REDMI 11 Black is Rs:-',f)
                                g=25000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 11 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Black                   Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 11 Black :-'))
                            if(5>z):
                                f=28000
                                print('Price for 8GB/256GB Storage Variant for REDMI 11 Black is Rs:-',f)
                                g=28000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 11 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Black                   Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=24000
                                g=24000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 11 Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 11 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 11 Black                   Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                     
                if(c==2):
                    print('Press 1. for REDMI 12 blue ')
                    print('Press 2. for REDMI 12  red ')
                    print('Press 3. for REDMI 12 black')
                    d=int(input('Enter Your Choice  :-'))
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 12 Blue is 20k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 12 Blue is 21k')
                        e=int(input('Enter The variant of REDMI 12 Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 12 Blue :-'))
                            if(5>z):
                                f=20000
                                print('price for 6GB/128GB Storage Variant for REDMI 12 Blue  is Rs:-',f)
                                g=20000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 12 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Blue                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=20000
                                print('Price for 6GB/128GB Storage Variant for REDMI 12 Blue is Rs:-',f)
                                g=20000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 12 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Blue                    Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 12 Blue :-'))
                            if(5>z):
                                f=21000
                                print('Price for 8GB/256GB Storage Variant for REDMI 12 Blue is Rs:-',f)
                                g=21000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 12 BLUE is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Blue                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=21000
                                g=21000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 12 Blue is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 12 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Blue                    Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 12 Red is 22k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 12 Red is 24k')
                        e=int(input('Enter The variant of REDMI 12 Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 12 Red  :-'))
                            if(5>z):
                                f=22000
                                print('price for 6GB/128GB Storage Variant for REDMI 12 Red  is Rs:-',f)
                                g=22000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 12 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Red                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=22000
                                print('Price for 6GB/128GB Storage Variant for REDMI 12 Red is Rs:-',f)
                                g=22000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 12 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Red                     Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                         
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 12 Red :-'))
                            if(5>z):
                                f=24000
                                print('Price for 8GB/256GB Storage Variant for REDMI 12 Red is Rs:-',f)
                                g=24000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 12 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Red                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=24000
                                g=24000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 12 Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 12 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Red                     Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 12 Black is 25k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 12 Black is 28k')
                        e=int(input('Enter The variant of REDMI 12 Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 12 Black  :-'))
                            if(5>z):
                                f=25000
                                print('price for 6GB/128GB Storage Variant for REDMI 12 Black  is Rs:-',f)
                                g=25000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 12 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Black                   Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=25000
                                print('Price for 6GB/128GB Storage Variant for REDMI 12 Black is Rs:-',f)
                                g=25000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 12 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Black                   Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                         
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 12 Black :-'))
                            if(5>z):
                                f=28000
                                print('Price for 8GB/256GB Storage Variant for REDMI 12 Black is Rs:-',f)
                                g=28000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 12 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Black                   Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=24000
                                g=24000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 12 Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 12 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 12 Black                   Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')           
                            
                if(c==3):
                    print('Press 1. for REDMI 13 blue ')
                    print('Press 2. for REDMI 13 red ')
                    print('Press 3. for REDMI 13 black')
                    d=int(input('Enter Your Choice  :-'))
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 13 Blue is 12k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 13 Blue is 15k')
                        e=int(input('Enter The variant of REDMI 13 Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 13 Blue :-'))
                            if(5>z):
                                f=12000
                                print('price for 6GB/128GB Storage Variant for REDMI 13 Blue  is Rs:-',f)
                                g=12000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 13 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Blue                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=12000
                                print('Price for 6GB/128GB Storage Variant for REDMI 13 Blue is Rs:-',f)
                                g=12000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 13 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Blue                    Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 13 Blue :-'))
                            if(5>z):
                                f=15000
                                print('Price for 8GB/256GB Storage Variant for REDMI 13 Blue is Rs:-',f)
                                g=15000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 13 BLUE is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Blue                    Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=15000
                                g=15000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 13 Blue is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 13 Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Blue                    Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 13 Red is 17k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 13 Red is 20k')
                        e=int(input('Enter The variant of REDMI 13 Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 13 Red  :-'))
                            if(5>z):
                                f=17000
                                print('price for 6GB/128GB Storage Variant for REDMI 13 Red  is Rs:-',f)
                                g=17000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 13 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Red                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=17000
                                print('Price for 6GB/128GB Storage Variant for REDMI 13 Red is Rs:-',f)
                                g=17000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 13 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Red                     Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 13 Red :-'))
                            if(5>z):
                                f=20000
                                print('Price for 8GB/256GB Storage Variant for REDMI 13 Red is Rs:-',f)
                                g=20000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 13 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Red                     Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=20000
                                g=20000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 13 Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 13 Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Red                     Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for REDMI 13 Black is 23k')
                        print('Press 2. for  8GB/256GB Storage Variant for REDMI 13 Black is 24k')
                        e=int(input('Enter The variant of REDMI 12 Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for REDMI 12 Black  :-'))
                            if(5>z):
                                f=23000
                                print('price for 6GB/128GB Storage Variant for REDMI 13 Black  is Rs:-',f)
                                g=23000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 13 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Black                   Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=23000
                                print('Price for 6GB/128GB Storage Variant for REDMI 13 Black is Rs:-',f)
                                g=23000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for REDMI 13 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Black                   Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                         
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for REDMI 13 Black :-'))
                            if(5>z):
                                f=24000
                                print('Price for 8GB/256GB Storage Variant for REDMI 13 Black is Rs:-',f)
                                g=24000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 13 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Black                   Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=24000
                                g=24000*z                        
                                print('Price for 8GB/256GB Storage Variant for REDMI 13 Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for REDMI 13 Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for REDMI 13 Black                   Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
          
            if(b==3):
                print('DIWALI OFFER 15% OFF in OnePlus Phone')
                print('Press 1. for  OnePlus 10T')
                print('Press 2. for  OnePlus 10 Pro')
                print('Press 3. for  OnePlus 10R')
                c=int(input('Enter Your Choice :-'))
                if(c==1):
                    print('Press 1. for OnePlus 10T blue ')
                    print('Press 2. for OnePlus 10T red ')
                    print('Press 3. for OnePlus 10T black')
                    d=int(input('Enter Your Choice :-'))
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10T Blue is 50k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10T Blue is 52k')
                        e=int(input('Enter The variant of OnePlus 10T Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10T Blue :-'))
                            if(5>z):
                                f=50000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10T Blue  is Rs:-',f)
                                g=50000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10T Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Blue                 Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=50000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10T Blue is Rs:-',f)
                                g=50000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10T Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Blue                 Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10T Blue :-'))
                            if(5>z):
                                f=52000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10T is Rs:-',f)
                                g=52000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10T BLUE is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Blue                 Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=52000
                                g=52000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10T Blue is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10T Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Blue                 Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10T Red is 54k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10T Red is 56k')
                        e=int(input('Enter The variant of OnePlus 10T Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10T Red  :-'))
                            if(5>z):
                                f=54000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10T Red  is Rs:-',f)
                                g=54000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10T Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Red                  Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=54000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10T Red is Rs:-',f)
                                g=54000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10T Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Red                  Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                         
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10T Red :-'))
                            if(5>z):
                                f=56000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10T Red is Rs:-',f)
                                g=56000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10T Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Red                  Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=56000
                                g=56000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10T Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10T Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Red                  Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10T Black is 53k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10T Black is 56k')
                        e=int(input('Enter The variant of OnePlus 10T Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10T Black  :-'))
                            if(5>z):
                                f=53000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10T Black  is Rs:-',f)
                                g=53000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10T Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Black                Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=53000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10T Black is Rs:-',f)
                                g=53000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10T Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Black                Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                         
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10T Black :-'))
                            if(5>z):
                                f=56000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10T Black is Rs:-',f)
                                g=56000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10T Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Black                Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=56000
                                g=56000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10T Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10T Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10T Black                Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                 
                if(c==2):
                    print('Press 1. for OnePlus 10 Pro blue ')
                    print('Press 2. for OnePlus 10 Pro Red ')
                    print('Press 3. for OnePlus 10 Pro black')
                    d=int(input('Enter Your Choice  :-'))
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10 Pro Blue is 50k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10 Pro Blue is 52k')
                        e=int(input('Enter The variant of OnePlus 10T Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10 Pro Blue :-'))
                            if(5>z):
                                f=50000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10 Pro Blue  is Rs:-',f)
                                g=50000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10 Pro Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Blue              Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=50000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10 Pro Blue is Rs:-',f)
                                g=50000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10 Pro Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Blue              Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10 Pro Blue :-'))
                            if(5>z):
                                f=52000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10 Pro is Rs:-',f)
                                g=52000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10 Pro BLUE is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Blue              Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=52000
                                g=52000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10 Pro Blue is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10 Pro Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Blue              Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10 Pro Red is 54k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10 Pro Red is 56k')
                        e=int(input('Enter The variant of OnePlus 10T Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10 Pro Red  :-'))
                            if(5>z):
                                f=54000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10 Pro Red  is Rs:-',f)
                                g=54000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10 Pro Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Red               Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=54000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10 Pro Red is Rs:-',f)
                                g=54000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10 Pro Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Red               Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                         
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10 Pro Red :-'))
                            if(5>z):
                                f=56000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10 Pro Red is Rs:-',f)
                                g=56000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10 Pro Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Red               Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=56000
                                g=56000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10 Pro Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10 Pro Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Red               Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10 Pro Black is 53k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10 Pro Black is 56k')
                        e=int(input('Enter The variant of OnePlus 10T Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10 Pro Black  :-'))
                            if(5>z):
                                f=53000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10 Pro Black  is Rs:-',f)
                                g=53000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10 Pro Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Black             Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=53000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10 Pro Black is Rs:-',f)
                                g=53000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10 Pro Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Black             Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10 Pro Black :-'))
                            if(5>z):
                                f=56000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10 Pro Black is Rs:-',f)
                                g=56000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10 Pro Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Black             Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=56000
                                g=56000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10 Pro Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10 Pro Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10 Pro Black             Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
            
                if(c==3):
                    print('Press 1. for OnePlus 10R blue ')
                    print('Press 2. for OnePlus 10R red ')
                    print('Press 3. for OnePlus 10R black')
                    d=int(input('Enter Your Choice  :-'))
                    if(d==1):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10R Blue is 50k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10R Blue is 52k')
                        e=int(input('Enter The variant of OnePlus 10T Blue :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10R Blue :-'))
                            if(5>z):
                                f=50000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10R Blue  is Rs:-',f)
                                g=50000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10R Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Blue                 Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=50000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10R Blue is Rs:-',f)
                                g=50000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10R Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Blue                 Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10R Blue :-'))
                            if(5>z):
                                f=52000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10R is Rs:-',f)
                                g=52000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10R BLUE is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Blue                 Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=52000
                                g=52000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10R Blue is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10R Blue is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Blue                 Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==2):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10R Red is 54k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10R Red is 56k')
                        e=int(input('Enter The variant of OnePlus 10T Red :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10R Red  :-'))
                            if(5>z):
                                f=54000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10R Red  is Rs:-',f)
                                g=54000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10R Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Red                  Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=54000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10R Red is Rs:-',f)
                                g=54000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10R Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Red                  Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                  
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10R Red :-'))
                            if(5>z):
                                f=56000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10R Red is Rs:-',f)
                                g=56000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10R Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Red                  Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=56000
                                g=56000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10R Red is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10R Red is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Red                  Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                    if(d==3):
                        print('Press 1. for  6GB/128GB Storage Variant for OnePlus 10R Black is 53k')
                        print('Press 2. for  8GB/256GB Storage Variant for OnePlus 10R Black is 56k')
                        e=int(input('Enter The variant of OnePlus 10T Black :-'))
                        if(e==1):
                            z=int(input('Quantity for 6GB/128GB Storage Variant for OnePlus 10R Black  :-'))
                            if(5>z):
                                f=53000
                                print('price for 6GB/128GB Storage Variant for OnePlus 10R Black  is Rs:-',f)
                                g=53000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10R Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Black                Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is   Rs:-   ',T)
                                print('Including GST')
                            if(5<=z):
                                f=53000
                                print('Price for 6GB/128GB Storage Variant for OnePlus 10R Black is Rs:-',f)
                                g=53000*z
                                print('Price for Quantity of 6GB/128GB Storage Variant for OnePlus 10R Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Black                Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is     Rs:-   ',T)
                                print('Including GST')
                
                        if(e==2):
                            z=int(input('Quantity for 8GB/256GB Storage Variant for OnePlus 10R Black :-'))
                            if(5>z):
                                f=56000
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10R Black is Rs:-',f)
                                g=56000*z
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10R Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*15/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Black                Rs:- -',h)
                                print('Additional Discount 15%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                print('Total Amount is    Rs:-  ',T)
                                print('Including GST')
                            if(5<=z):
                                f=56000
                                g=56000*z                        
                                print('Price for 8GB/256GB Storage Variant for OnePlus 10R Black is Rs:-',f)
                                print('Price for Quantity of 8GB/256GB Storage Variant for OnePlus 10R Black is Rs:-'
                                      ,g)
                                h=g*10/100
                                i=g-h
                                j=i*20/100
                                k=i-j
                                L=g*5/100
                                T=k+L
                                print('DIWALI OFFER 10% OFF ')
                                print('DIWALI OFFER Price for OnePlus 10R Black                Rs:- -',h)
                                print('Additional Discount 20%                                 Rs:- -',j)
                                print('GSt 5%                                                  Rs:- +',L)
                                
                                print('Total Amount is   Rs:-  ',T)
                                print('Including GST')
                if(b==4):
                    break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Headphones~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~             
        elif(a==2):
            print('Press 1. for CosmicByte Headphones')
            print('Press 2. for HyperX Headphones')
            print('Press 3. for Boat Headphones')
            b=int(input('Enter Your Choice :-'))
            if(b==1):
                print('DIWALI OFFER 25% OFF on  CosmicByte Headphones')
                print('Press 1. for  CosmicByte Wired Gaming Headphones')
                print('Press 2. for CosmicByte Wireless Gaming Headphones ')
                c=int(input('Enter Your Choice :-'))
                if(c==1):
                    print('Press 1. for Cosmic Byte Blazar Gaming Headphones Rs-1000')
                    print('press 2. for Cosmic Byte Equinox Neutrino Headphones Rs-1200')
                    d=int(input('Enter Your Choice :-  '))
                    if(d==1):
                        print('Press 1. for Cosmic Byte Blazar Gaming  Headphones Blue ')
                        print('Press 2. for Cosmic Byte Blazar Gaming  Headphones Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for Cosmic Byte Blazar Gaming  Headphones Blue :-'))
                            f=1000
                            g=1000*z                        
                            print('Price for Cosmic Byte Blazar Gaming  Headphones Blue is Rs:-',f)
                            print('Price for Cosmic Byte Blazar Gaming  Headphones Blue is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*20/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print('DIWALI OFF Price for Cosmic Byte Blazar Gaming  Headphones  Blue   Rs:- -',h)
                            print('Additional Discount 20%                                            Rs:- -',j)
                            print('GSt 5%                                                             Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for Cosmic Byte Blazar Gaming  Headphones Red :-'))
                            f=1000
                            g=1000*z                        
                            print('Price for  Cosmic Byte Blazar Gaming  Headphones Red is Rs:-',f)
                            print('Price for  Cosmic Byte Blazar Gaming  Headphones Red is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*20/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print(' DIWALI OFF for Cosmic Byte Blazar Gaming  Headphones Red   Rs:- -',h)
                            print('Additional Discount 20%                                     Rs:- -',j)
                            print('GSt 5%                                                      Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                    if(d==2):
                        print('Press 1. for Cosmic Byte Equinox Neutrino Headphones Silver ')
                        print('Press 2. for Cosmic Byte Equinox Neutrino Headphones Orange ')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for Cosmic Byte Equinox Neutrino Headphones Silver :-'))
                            f=1200
                            g=1200*z                        
                            print('Price for  Cosmic Byte Equinox Neutrino Headphones Silver is Rs:-',f)
                            print('Price for  Cosmic Byte Equinox Neutrino Headphones Silver is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print('DIWALI OFF Cosmic Byte Equinox Neutrino Headphones Silver   Rs:- -',h)
                            print('Additional Discount 15%                                     Rs:- -',j)
                            print('GSt 5%                                                      Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for Cosmic Byte Equinox Neutrino Headphones Orange :-'))
                            f=1200
                            g=1200*z                        
                            print('Price for Cosmic Byte Equinox Neutrino Headphones Orange is Rs:-',f)
                            print('Price for Cosmic Byte Equinox Neutrino Headphones Orange is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print(' DIWALI OFF for Cosmic Byte Equinox Neutrino Headphones Orange  Rs:- -',h)
                            print('Additional Discount 15%                                         Rs:- -',j)
                            print('GSt 5%                                                          Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                if(c==2):
                    print('Press 1. for Cosmic Byte Oberon  Wireless Gaming Headphone Rs-2000')
                    print('press 2. for Cosmic Byte Ersa Wireless Gaming Headphone Rs-2200')
                    d=int(input('Enter Your Choice :-  '))
                    if(d==1):
                        print('Press 1. for Cosmic Byte Oberon  Wireless Gaming Headphone Black ')
                        print('Press 2. for Cosmic Byte Oberon  Wireless Gaming Headphone Red ')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for Cosmic Byte Oberon  Wireless Gaming Headphone Black :-'))
                            f=2000
                            g=2000*z                        
                            print('Price for Cosmic Byte Oberon  Wireless Gaming Headphone Black is Rs:-',f)
                            print('Price for Cosmic Byte Oberon  Wireless Gaming Headphone Black is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print(' DIWALI OFF for Cosmic Byte Oberon Wireless Gaming Headphone Black  Rs:- -',h)
                            print('Additional Discount 10%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for Cosmic Byte Oberon  Wireless Gaming Headphone Red :-'))
                            f=2000
                            g=2000*z                        
                            print('Price for Cosmic Byte Oberon  Wireless Gaming Headphone Red is Rs:-',f)
                            print('Price for Cosmic Byte Oberon  Wireless Gaming Headphone Red is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print(' DIWALI OFF for Cosmic Byte Oberon Wireless Gaming Headphone Red  Rs:- -',h)
                            print('Additional Discount 10%                                           Rs:- -',j)
                            print('GSt 5%                                                            Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                    if(d==2):
                        print('Press 1. for Cosmic Byte Ersa Wireless Gaming Headphone Black ')
                        print('Press 2. for Cosmic Byte Ersa Wireless Gaming Headphone Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for Cosmic Byte Ersa Wireless Gaming Headphone Black :-'))
                            f=2200
                            g=2200*z                        
                            print('Price for Cosmic Byte Ersa Wireless Gaming Headphone Black is Rs:-',f)
                            print('Price for Cosmic Byte Ersa Wireless Gaming Headphone Black is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*25/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print(' DIWALI OFF for Cosmic Byte Ersa Wireless Gaming Headphone Black Rs:- -',h)
                            print('Additional Discount 25%                                          Rs:- -',j)
                            print('GSt 5%                                                           Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for Cosmic Byte Ersa Wireless Gaming Headphone Red :-'))
                            f=2200
                            g=2200*z                        
                            print('Price for Cosmic Byte Ersa Wireless Gaming Headphone Red is Rs:-',f)
                            print('Price for Cosmic Byte Ersa Wireless Gaming Headphone Red is Rs:-',g)
                            h=g*25/100
                            i=g-h
                            j=i*25/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 25% OFF ')
                            print(' DIWALI OFF for Cosmic Byte Ersa Wireless Gaming Headphone Red   Rs:- -',h)
                            print('Additional Discount 25%                                          Rs:- -',j)
                            print('GSt 5%                                                           Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
            if(b==2):
                print('DIWALI OFFER 30% OFF on  HyperX Headphones')
                print('Press 1. for  HyperX Wired Gaming Headphones')
                print('Press 2. for HyperX Wireless Gaming Headphones ')
                c=int(input('Enter Your Choice :-'))
                if(c==1):
                    print('Press 1. for HyperX Cloud Stinger Gaming Headphones Rs-5000')
                    print('press 2. for HyperX Cloud Stinger 2  Gaming Headset Rs-10000')
                    d=int(input('Enter Your Choice :-  '))
                    if(d==1):
                        print('Press 1. for HyperX Cloud Stinger Gaming  Headphones Blue ')
                        print('Press 2. for HyperX Cloud Stinger Gaming  Headphones Red  ')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for HyperX Cloud Stinger Gaming Headphones Blue :-'))
                            f=5000
                            g=5000*z                        
                            print('Price for HyperX Cloud Stinger Gaming Headphones Blue is Rs:-',f)
                            print('Price for HyperX Cloud Stinger Gaming Headphones Blue is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*15/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print(' DIWALI OFF for HyperX Cloud Stinger Gaming Headphones Blue    Rs:- -',h)
                            print('Additional Discount 15%                                        Rs:- -',j)
                            print('GSt 5%                                                         Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for HyperX Cloud Stinger Gaming Headphones Red :-'))
                            f=5000
                            g=5000*z                        
                            print('Price for HyperX Cloud Stinger Gaming Headphones Red is Rs:-',f)
                            print('Price for HyperX Cloud Stinger Gaming Headphones Red is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*15/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print(' DIWALI OFF for HyperX Cloud Stinger Gaming Headphones Red     Rs:- -',h)
                            print('Additional Discount 15%                                        Rs:- -',j)
                            print('GSt 5%                                                         Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                    if(d==2):
                        print('Press 1. for HyperX Cloud Stinger 2 Gaming  Headphones Blue')
                        print('Press 2. for HyperX Cloud Stinger 2 Gaming  Headphones orange')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for HyperX Cloud Stinger 2 Gaming  Headphones Blue :-'))
                            f=10000
                            g=10000*z                        
                            print('Price for HyperX Cloud Stinger 2 Gaming  Headphones Blue is Rs:-',f)
                            print('Price for HyperX Cloud Stinger 2 Gaming  Headphones Blue is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*20/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print(' DIWALI OFF for HyperX Cloud Stinger 2 Gaming  Headphones Blue  Rs:- -',h)
                            print('Additional Discount 20%                                         Rs:- -',j)
                            print('GSt 5%                                                          Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for HyperX Cloud Stinger 2 Gaming  Headphones orange :-'))
                            f=10000
                            g=10000*z                        
                            print('Price for HyperX Cloud Stinger 2 Gaming  Headphones orange is Rs:-',f)
                            print('Price for HyperX Cloud Stinger 2 Gaming  Headphones orange is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*20/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print(' DIWALI OFF for HyperX Cloud Stinger 2 Gaming  Headphones orange Rs:- -',h)
                            print('Additional Discount 20%                                          Rs:- -',j)
                            print('GSt 5%                                                           Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                if(c==2):
                    print('Press 1. for HyperX Cloud Alpha Wireless Gaming Headphones Rs-8000')
                    print('press 2. for HyperX Cloud Flight Wireless  Gaming Headset Rs-15000')
                    d=int(input('Enter Your Choice :-  '))
                    if(d==1):
                        print('Press 1. for   HyperX Cloud Alpha Wireless Gaming  Headphones Blue')
                        print('Press 2. for   HyperX Cloud Alpha Wirelessr Gaming  Headphones Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for HyperX Cloud Alpha Wireless Gaming  Headphones Blue :-'))
                            f=8000
                            g=8000*z                        
                            print('Price for HyperX Cloud Alpha Wireless Gaming  Headphones Blue is Rs:-',f)
                            print('Price for HyperX Cloud Alpha Wireless Gaming  Headphones Blue is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print(' DIWALI OFF for HyperX Cloud Alpha Wireless Gaming  Headphones Blue Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for HyperX Cloud Alpha Wireless Gaming  Headphones Red :-'))
                            f=8000
                            g=8000*z                        
                            print('Price for HyperX Cloud Alpha Wireless Gaming  Headphones Red is Rs:-',f)
                            print('Price for HyperX Cloud Alpha Wireless Gaming  Headphones Red is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print(' DIWALI OFF for HyperX Cloud Alpha Wireless  Gaming  Headphones Red Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                    if(d==2):
                        print('Press 1. for  HyperX Cloud Flight Wireless Gaming  Headphones Blue')
                        print('Press 2. for  HyperX Cloud Flight  Wirelessr Gaming  Headphones Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for HyperX Cloud Flight Wireless Gaming  Headphones Blue :-'))
                            f=15000
                            g=15000*z                        
                            print('Price for HyperX Cloud Flight Wireless Gaming  Headphones Blue is Rs:-',f)
                            print('Price for HyperX Cloud Flight Wireless Gaming  Headphones Blue is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print('DIWALI OFF for HyperX Cloud Flight Wireless Gaming  Headphones Blue Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for HyperX Cloud Flight  Wirelessr Gaming  Headphones Red :-'))
                            f=15000
                            g=15000*z                        
                            print('Price for HyperX Cloud Flight  Wirelessr Gaming  Headphones Red is Rs:-',f)
                            print('Price for HyperX Cloud Flight  Wirelessr Gaming  Headphones Red is Rs:-',g)
                            h=g*30/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 30% OFF ')
                            print('DIWALI OFF for HyperX Cloud Flight  Wirelessr Gaming Headphones Red Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
            if(b==3):
                print('DIWALI OFFER 40% OFF on  Boat Headphones')
                print('Press 1. for  Boat Wired Gaming Headphones')
                print('Press 2. for Boat Wireless Gaming Headphones ')
                c=int(input('Enter Your Choice :-'))
                if(c==1):
                    print('Press 1.  for BoAt BassHeads Gaming Headphones Rs-2000')
                    print('press 2.  for BoAt Rockerz  Gaming Headset Rs-4000')
                    d=int(input('Enter Your Choice :-  '))
                    if(d==1):
                        print('Press 1. for  BoAt BassHeads Gaming  Headphones Blue')
                        print('Press 2. for  BoAt BassHeads Gaming  Headphones Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for BoAt BassHeads Gaming  Headphones Blue :-'))
                            f=2000
                            g=2000*z                        
                            print('Price for BoAt BassHeads Gaming  Headphones Blue is Rs:-',f)
                            print('Price for BoAt BassHeads Gaming  Headphones Blue is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for BoAt BassHeads Gaming  Headphones Blue               Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for BoAt BassHeads Gaming  Headphones Red :-'))
                            f=2000
                            g=2000*z                        
                            print('Price for BoAt BassHeads Gaming  Headphones Red is Rs:-',f)
                            print('Price for BoAt BassHeads Gaming  Headphones Red is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for BoAt BassHeads Gaming  Headphones Red                Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                    if(d==2):
                        print('Press 1. for  BoAt Rockerz Gaming  Headphones Blue')
                        print('Press 2. for  BoAt Rockerz Gaming  Headphones Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for  BoAt Rockerz Gaming  Headphones Blue :-'))
                            f=4000
                            g=4000*z                        
                            print('Price for  BoAt Rockerz Gaming  Headphones Blue is Rs:-',f)
                            print('Price for  BoAt Rockerz Gaming  Headphones Blue is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for  BoAt Rockerz Gaming  Headphones Blue                Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for BoAt Rockerz Gaming  Headphones Red :-'))
                            f=4000
                            g=4000*z                        
                            print('Price for BoAt Rockerz Gaming  Headphones Red is Rs:-',f)
                            print('Price for BoAt Rockerz Gaming  Headphones Red is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for BoAt Rockerz Gaming  Headphones Red                  Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                if(c==2):
                    print('Press 1.  for BoAt Immortal Wireless Gaming Headphones Rs-4000')
                    print('press 2.  for BoAt BassHeads Wireless  Gaming Headset  Rs-3000')
                    d=int(input('Enter Your Choice :-  '))
                    if(d==1):
                        print('Press 1. for  BoAt Immortal Wireless Gaming  Headphones Blue')
                        print('Press 2. for  BoAt Immortal Wireless Gaming  Headphones Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for BoAt Immortal Wireless Gaming  Headphones Blue :-'))
                            f=4000
                            g=4000*z                        
                            print('Price for BoAt Immortal Wireless Gaming  Headphones Blue is Rs:-',f)
                            print('Price for BoAt Immortal Wireless Gaming  Headphones Blue is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for BoAt Immortal Wireless Gaming  Headphones Blue       Rs:- -',h)
                            print('Additional Discount 10%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for BoAt Immortal Wireless Gaming  Headphones Red :-'))
                            f=4000
                            g=4000*z                        
                            print('Price for BoAt Immortal Wireless Gaming  Headphones Red is Rs:-',f)
                            print('Price for BoAt Immortal Wireless Gaming  Headphones Red is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*12/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for BoAt Immortal Wireless Gaming  Headphones Red        Rs:- -',h)
                            print('Additional Discount 12%                                             Rs:- -',j)
                            print('GSt 5%                                                              Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                    if(d==2):
                        print('Press 1.  for  BoAt BassHeads Wireless Gaming  Headphones Blue')
                        print('Press 2.  for  BoAt BassHeads Wireless Gaming  Headphones Red')
                        e=int(input('Enter Your Choice :-'))
                        if(e==1):
                            z=int(input('Quantity for BoAt BassHeads Wireless Gaming  Headphones Blue :-'))
                            f=3000
                            g=3000*z                        
                            print('Price for BoAt BassHeads Wireless Gaming  Headphones Blue is Rs:-',f)
                            print('Price for BoAt BassHeads Wireless Gaming  Headphones Blue is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for BoAt BassHeads Wireless Gaming  Headphones Blue   Rs:- -',h)
                            print('Additional Discount 10%                                          Rs:- -',j)
                            print('GSt 5%                                                           Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
                        if(e==2):
                            z=int(input('Quantity for BoAt BassHeads Wireless Gaming  Headphones Red :-'))
                            f=3000
                            g=3000*z                        
                            print('Price for BoAt BassHeads Wireless Gaming  Headphones Red is Rs:-',f)
                            print('Price for BoAt BassHeads Wireless Gaming  Headphones Red is Rs:-',g)
                            h=g*40/100
                            i=g-h
                            j=i*10/100
                            k=i-j
                            L=g*5/100
                            T=k+L
                            print('DIWALI OFFER 40% OFF ')
                            print('DIWALI OFF for BoAt BassHeads Wireless Gaming  Headphones Red Rs:- -',h)
                            print('Additional Discount 10%                                       Rs:- -',j)
                            print('GSt 5%                                                        Rs:- +',L)    
                            print('Total Amount is   Rs:-  ',T)
                            print('Including GST')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Laptop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                    
        elif(a==3):
              print('DIWALI OFFER 5O% OFF on Laptop')    
              print('Press 1. for ACER Laptop')
              print('Press 2. for ASUS Laptop')
              b=int(input('Enter Your Choice :-'))
              if(b==1):
                  print('Press 1. for  AMD ACER Laptop')
                  print('Press 2. for  Intel Acer Laptop')
                  c=int(input('Enter Your Choice :-'))
                  if(c==1):
                      print('Press 1. for Acer Aspire Rs-40000')
                      print('Press 2. for Acer Aspire 3 Rs-60000')
                      d=int(input('Enter Your Choice :-'))
                      if(d==1):
                          print('Press 1.  for  Acer Aspire White')
                          print('Press 2.  for  Acer Aspire Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for Acer Aspire White :-'))
                              f=40000
                              g=40000*z                        
                              print('Price for Acer Aspire White is Rs:-',f)
                              print('Price for Acer Aspire White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*10/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for Acer Aspire White                      Rs:- -',h)
                              print('Additional Discount 10%                               Rs:- -',j)
                              print('GSt 5%                                                Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for Acer Aspire Black :-'))
                              f=40000
                              g=40000*z                        
                              print('Price for Acer Aspire Black is Rs:-',f)
                              print('Price for Acer Aspire Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*10/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  Acer Aspire Black                        Rs:- -',h)
                              print('Additional Discount 10%                                  Rs:- -',j)
                              print('GSt 5%                                                   Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                      if(d==2):
                          print('Press 1.  for  Acer Aspire 3 White')
                          print('Press 2.  for  Acer Aspire 3 Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for Acer Aspire 3 White :-'))
                              f=60000
                              g=60000*z                        
                              print('Price for Acer Aspire 3 White is Rs:-',f)
                              print('Price for Acer Aspire 3 White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*10/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  Acer Aspire 3 White                   Rs:- -',h)
                              print('Additional Discount 10%                               Rs:- -',j)
                              print('GSt 5%                                                Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for Acer Aspire 3 Black :-'))
                              f=60000
                              g=60000*z                        
                              print('Price for Acer Aspire 3 Black is Rs:-',f)
                              print('Price for Acer Aspire 3 Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*10/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  Acer Aspire 3 Black                    Rs:- -',h)
                              print('Additional Discount 10%                                Rs:- -',j)
                              print('GSt 5%                                                 Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                  if(c==2):
                      print('Press 1. for Acer Aspire 5 Rs-45000')
                      print('Press 2. for Acer Aspire Lite Rs-52000')
                      d=int(input('Enter Your Choice :-'))
                      if(d==1):
                          print('Press 1.  for  Acer Aspire  5 White')
                          print('Press 2.  for  Acer Aspire  5 Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for Acer Aspire  5 White :-'))
                              f=45000
                              g=45000*z                        
                              print('Price for Acer Aspire  5 White is Rs:-',f)
                              print('Price for Acer Aspire  5 White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*15/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  Acer Aspire  5 White                  Rs:- -',h)
                              print('Additional Discount 15%                               Rs:- -',j)
                              print('GSt 5%                                                Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for Acer Aspire  5 Black :-'))
                              f=45000
                              g=45000*z                        
                              print('Price for Acer Aspire  5 Black is Rs:-',f)
                              print('Price for Acer Aspire  5 Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*15/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  Acer Aspire 5 Black                  Rs:- -',h)
                              print('Additional Discount 15%                              Rs:- -',j)
                              print('GSt 5%                                               Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                      if(d==2):
                          print('Press 1.  for  Acer Aspire Lite White')
                          print('Press 2.  for  Acer Aspire Lite Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for  Acer Aspire Lite White :-'))
                              f=52000
                              g=52000*z                        
                              print('Price for  Acer Aspire Lite White is Rs:-',f)
                              print('Price for  Acer Aspire Lite White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*15/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  Acer Aspire Lite White                 Rs:- -',h)
                              print('Additional Discount 15%                                Rs:- -',j)
                              print('GSt 5%                                                 Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for Acer Aspire Lite Black :-'))
                              f=52000
                              g=52000*z                        
                              print('Price for Acer Aspire Lite Black is Rs:-',f)
                              print('Price for Acer Aspire Lite Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*15/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  Acer Aspire Lite Black                 Rs:- -',h)
                              print('Additional Discount 15%                                Rs:- -',j)
                              print('GSt 5%                                                 Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
              if(b==2):
                  print('Press 1. for  AMD ASUS Laptop')
                  print('Press 2. for  Intel ASUS Laptop')
                  c=int(input('Enter Your Choice :-'))
                  if(c==1):
                      print('Press 1. for ASUS Vivobook Go 14 Rs-30000')
                      print('Press 2. for ASUS Vivobook Flip 14 Rs-50000')
                      d=int(input('Enter Your Choice :-'))
                      if(d==1):
                          print('Press 1.  for  ASUS Vivobook Go 14 White')
                          print('Press 2.  for  ASUS Vivobook Go 14 Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for ASUS Vivobook Go 14 White :-'))
                              f=30000
                              g=30000*z                        
                              print('Price for ASUS Vivobook Go 14 White is Rs:-',f)
                              print('Price for ASUS Vivobook Go 14 White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for ASUS Vivobook Go 14 White                Rs:- -',h)
                              print('Additional Discount 20%                                 Rs:- -',j)
                              print('GSt 5%                                                  Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for ASUS Vivobook Go 14 Black :-'))
                              f=30000
                              g=30000*z                        
                              print('Price for ASUS Vivobook Go 14 Black is Rs:-',f)
                              print('Price for ASUS Vivobook Go 14 Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for ASUS Vivobook Go 14 Black                  Rs:- -',h)
                              print('Additional Discount 20%                                   Rs:- -',j)
                              print('GSt 5%                                                    Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                      if(d==2):
                          print('Press 1.  for  ASUS Vivobook Flip 14 White')
                          print('Press 2.  for  ASUS Vivobook Flip 14 Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for  ASUS Vivobook Flip 14 White :-'))
                              f=50000 
                              g=50000*z                        
                              print('Price for  ASUS Vivobook Flip 14 White is Rs:-',f)
                              print('Price for  ASUS Vivobook Flip 14 White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  ASUS Vivobook Flip 14 White              Rs:- -',h)
                              print('Additional Discount 20%                                  Rs:- -',j)
                              print('GSt 5%                                                   Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for  ASUS Vivobook Flip 14 Black :-'))
                              f=50000
                              g=50000*z                        
                              print('Price for  ASUS Vivobook Flip 14 Black is Rs:-',f)
                              print('Price for  ASUS Vivobook Flip 14 Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  ASUS Vivobook Flip 14 Black             Rs:- -',h)
                              print('Additional Discount 20%                                 Rs:- -',j)
                              print('GSt 5%                                                  Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                  if(c==2):
                      print('Press 1. for ASUS Chromebook Rs-55000')
                      print('Press 2. for ASUS Vivobook 14 Rs-65000')
                      d=int(input('Enter Your Choice :-'))
                      if(d==1):
                          print('Press 1.  for  ASUS Chromebook White')
                          print('Press 2.  for  ASUS Chromebook Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for  ASUS Chromebook White :-'))
                              f=55000
                              g=55000*z                        
                              print('Price for  ASUS Chromebook White is Rs:-',f)
                              print('Price for  ASUS Chromebook White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for  ASUS Chromebook White                    Rs:- -',h)
                              print('Additional Discount 20%                                  Rs:- -',j)
                              print('GSt 5%                                                   Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for   ASUS Chromebook Black :-'))
                              f=55000
                              g=55000*z                        
                              print('Price for   ASUS Chromebook Black is Rs:-',f)
                              print('Price for   ASUS Chromebook Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for   ASUS Chromebook Black                 Rs:- -',h)
                              print('Additional Discount 20%                                Rs:- -',j)
                              print('GSt 5%                                                 Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                      if(d==2):
                          print('Press 1.  for ASUS Vivobook 14 White')
                          print('Press 2.  for ASUS Vivobook 14 Black')
                          e=int(input('Enter Your Choice :-'))
                          if(e==1):
                              z=int(input('Quantity for ASUS Vivobook 14 White :-'))
                              f=65000
                              g=65000*z                        
                              print('Price for ASUS Vivobook 14 White is Rs:-',f)
                              print('Price for ASUS Vivobook 14 White is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for ASUS Vivobook 14 W                       Rs:- -',h)
                              print('Additional Discount 20%                                 Rs:- -',j)
                              print('GSt 5%                                                  Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')
                          if(e==2):
                              z=int(input('Quantity for ASUS Vivobook 14 Black :-'))
                              f=65000
                              g=65000*z                        
                              print('Price for ASUS Vivobook 14 Black is Rs:-',f)
                              print('Price for ASUS Vivobook 14 Black is Rs:-',g)
                              h=g*50/100
                              i=g-h
                              j=i*20/100
                              k=i-j
                              L=g*5/100
                              T=k+L
                              print('DIWALI OFFER 50% OFF ')
                              print('DIWALI OFF for ASUS Vivobook 14 Black                      Rs:- -',h)
                              print('Additional Discount 20%                                    Rs:- -',j)
                              print('GSt 5%                                                     Rs:- +',L)    
                              print('Total Amount is   Rs:-  ',T)
                              print('Including GST')                    

        else:
            print()

        print()
        main()
        x=int(input('Pick Your Option:--'))
print('Thank You For visiting in  Shop ')
print('Visit Again')
