import os
import math
	
def Menu():
        print ("1. Sum of Multiples of 3 and 5.")
        print ("2. Sum of Even Fibonnaci Numbers.")
        print ("3. Largest Prime Factor")
        print ("4. Palindrome Products")
        print ("5. Smallest Multiple")
        print ("6. Sum & Square Difference")
        print ("7. The Nth Prime")
        print ("8. Largest Product in a Series")
        print ("9. Pythagorean")
        print ("10. Sum of Primes")
        print ("Press Q to Quit")

def Response():
        response = input("Enter the action you would like to perform: ")
        return response

def Wait():
        wait = input("Press any key to continue...")

def Primes(n):
        #this doesn't work for really large n but those are really big n and I don't think my wee computer can handle 'em anyways.
        #generates all the primes less than the given n
        results = []
        #generate n True
        sieve = [True] * n
        for p in range(2, n):
                # if true
                if sieve[p]:
                        for i in range(p**2, n, p):
                                sieve[i] = False
        # results will only contain those left over as True
        for prime in range(2, n):
                if sieve[prime]:
                        results.append(prime)
        return results

def PythagoreanProducts(n):
        result = 0
        #this is definitely at least half awful.
        for c in range(1, n):
                for b in range (1, c):
                        for a in range(1, b):
                                if a + b >= c or c + a >= b or c + b >= a:
                                        pass
                                if a**2 + b**2 != c**2:
                                        pass
                                elif a + b + c != n:
                                        pass
                                else:
                                        print (a, b, c)
                                        result = a*b*c
                                        return result
        return result

def MultiplesOfThreesAndFives():
        print ("This function will sum all of the natural numbers below a certain number, n, that are multiples of threes and fives.")
        n = int(input("Set n equal to: "))
        summation = 0
        for x in range(1,n):
                #this is easy and you should understand it.
                if x%3 == 0 or x%5 == 0:
                        summation += x
                else:
                        pass
        print (summation)
        Wait()
        os.system('cls')

def EvenFibonacci():
        print ("This function will sum all the values of the Fibonnaci sequence less than a natural number n...")
        n = int(input("Set n equal to: "))
        #I'm literally assuming that the user will input n > 2
        #the var names should be clear. if not, mess around with it and soon all will be clear. 
        fibonaccisum = 2
        fibonaccifirst = 1
        fibonnaccisecond = 2
        while fibonaccifirst < n:
                fibonaccinext = fibonaccifirst + fibonnaccisecond
                fibonaccilast = fibonnaccisecond
                if fibonaccinext % 2 == 0:
                        fibonaccisum += fibonaccinext
                fibonaccifirst = fibonaccilast
                fibonnaccisecond = fibonaccinext
        print (fibonaccisum)
        Wait()
        os.system('cls')

def LargestPrime():
        print ("Every natural number is product of primes. A prime number is a number than can be divided by only 1 and itself. This function will determine the largest of the prime factors for a number n.")
        n = int(input("Set n equal to: "))
        #if there's no natural number able to fit the following conditions then n is prime
        largeprime = n
        # the arbritary addition of four is to account for very small numbers... does this actually account for all numbers... probably not.
        primes = Primes(int(n**.5)+4)
        for prime in primes[:int(n**.5)+4:]:
                if n%prime == 0:
                        largeprime = prime
                else:
                        pass
        #despite it's hopes and dreams, 1 will never be prime
        if largeprime == 1:
                print (str(n) + " is not a prime. By the very definition of prime. Try again silly user.")
        elif largeprime == n:
                print (str(n) + " is a prime!")
        else:
                print (str(n) + " is not a prime. It's largest prime factor is " + str(largeprime))
        Wait()
        os.system('cls')

def PalindromeProduct():
        print ("A palindromic number reads the same both ways. Find the largest palindrome from the product of two natural numbers with n digits")
        n = int(input("Set n equal to: "))
        palindrome = 0
        for x in range(10**(n-1),10**n - 1):
                for y in range(x, 10**n):
                        product = x * y
                        compared = list(str(product))
                        if compared == compared[::-1]:
                                if product > palindrome:
                                        palindrome = product
        print (palindrome)
        Wait()
        os.system('cls')

def SmallestMultiple():
        print ("Provide the smallest number than can be divided by 1 to n with a remainder equal to 0. ")
        #ahoho a product of primes problem
        n = int(input("Set n equal to: "))
        product = 1
        primes = Primes(n+1)
        for prime in primes:
                #basic logarithms. i could iterate of n to 0 by -1 but that's super wasteful.
                for m in range(int(math.log(n,prime)), 0, -1):
                        if prime**m > n:
                                pass
                        else:
                                product *= (prime**m)
                                break
        print (product)
        Wait()
        os.system('cls')

def SumSquareDifference():
        print ("For a natural number n, provide the difference between (1+...+n)**2 - (1**2 + ... + n**2)")
        n = int(input("Set n equal to: "))
        #fairly easy to figure out. subtract out the squares and all you have left are the inner products.
        #it's basically the quadratic formula.
        #but not actually. 
        difference = 0
        for x in range(1, n + 1):
                for y in range (0, x):
                        difference += x * y
        difference = 2 * difference
        print (difference)
        Wait()
        os.system('cls')

def NthPrime():
        print ("For a natural number n, print out the nth prime number")
        n = int(input("Set n equal to: "))
        count = 1
        nprime  = 2
        #this is ugly and i'm sorry. :/
        if n == 1:
                pass
        else:
                count = 2
                nprime = 3
                primes = [2,3]
                while count < n:
                        nprime += 2
                        modulo = []
                        for prime in primes:
                                modulo.append(nprime%prime)
                        if 0 in modulo:
                                pass
                        else:
                                primes.append(nprime)
                                count += 1
        #this could be better
        #what could be better than to have your people well fed?
        print (nprime)
        Wait()
        os.system('cls')

def PythagoreanProduct():
        print ("Determine just one Pythagorean Triplet that sums to the number n (if it exists) and then the product of that triplet")
        n = int(input("Set n equal to: "))
        result = PythagoreanProducts(n)
        if result == 0:
                print ("No Pythogorean Triplet exists for the sum of n")
        else:
                print ("The product is " + str(result))
        Wait()
        os.system('cls')

def LargestProductInSeries():
        print ("Determine the greatest product of n adjacent digits in the following number:")
        number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
        print (number)
        n = int(input("Set n equal to: "))
        number = list(number)
        i = 0
        count = 0
        total = len(number)-n+1
        largestproduct = 1
        #you know, i honestly didn't expect this one to work on the first try. 
        while count < total:
                product = 1
                for num in number[i:n]:
                        num = int(num)
                        product *= num
                if product > largestproduct:
                        largestproduct = product
                i+= 1
                n+= 1
                count+=1
        print (largestproduct)
        Wait()
        os.system('cls')

def SumPrimes():
        print ("Sum the prime numbers below a given number n.")
        n = int(input("Set n equal to: "))
        primes = Primes(n)
        total = 0
        for number in primes:
                total +=number 
        print (total)
        Wait()
        os.system('cls')
        
os.system('cls')
print ("Welcome to Katherine Short's solutions for the Euler project")
print ("Language : Python 3.4.3")
Wait()
os.system('cls')

# dictionary someday?
# if elif looks stupid. and will be a painnnnnn.
while True:
        Menu()
        answer = Response()
        if (answer == "1"):
                os.system('cls')
                MultiplesOfThreesAndFives()
        elif (answer == "2"):
                os.system('cls')
                EvenFibonacci()
        elif (answer == "3"):
                os.system('cls')
                LargestPrime()
        elif (answer == "4"):
                os.system('cls')
                PalindromeProduct()
        elif (answer == "5"):
                os.system('cls')
                SmallestMultiple()
        elif (answer == "6"):
                os.system('cls')
                SumSquareDifference()
        elif (answer =="7"):
                os.system('cls')
                NthPrime()
        elif (answer =="8"):
                os.system('cls')
                LargestProductInSeries()
        elif (answer =="9"):
                os.system('cls')
                PythagoreanProduct()
        elif (answer =="10"):
                os.system('cls')
                SumPrimes()
        elif (answer == "Q"):
                print ("Hope you enjoyed the Math!")
                break
        else:
                os.system('cls')
