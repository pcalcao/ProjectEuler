from math import sqrt, ceil
import itertools

def is_prime(n):
	if n == 1 or n == 2: #basic case
		return True
	if n % 2 == 0:
		return False
	for i in range (3, int(sqrt(int(n)))+1,2):
		if n % i == 0:
			return False
	return True

def nth_prime(nth):
	first_prime = 2
	count = 1
	for prime_candidate in itertools.count(3, 2):
		if is_prime(prime_candidate):
			count +=1 
			if count == nth:
				return prime_candidate

def erastot_sieve(n):
  siv=range(n+1)
  siv[1]=0
  sqn=int(round(n**0.5))
  for i in range(2,sqn+1):
    if siv[i]!=0:
        siv[2*i:n/i*i+1:i]=[0]*(n/i-1)
  return filter(None,siv)
