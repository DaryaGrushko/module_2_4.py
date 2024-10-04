#Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Дан список чисел =', numbers)
print('Задание: используя этот список составьте второй список primes, содержащий только простые числа.',
      '\nА так же третий список not_primes, содержащий все не простые числа.')
primes = [] #только простые числа
not_primes = [] #все не простые числа
is_not_prime = False

for i in numbers:
    is_not_prime = False

    if i != 1:
        for j in range(2, i):
            #print('Щаг i=', i, 'j=', j, ' i%j = ', i % j, 'is_not_prime=', is_not_prime)
            if i % j == 0:
                is_not_prime = True # делится нацело
                #print ('!!!is_not_prime=',  is_not_prime)
        if is_not_prime == True:
            not_primes.append(i)
        elif is_not_prime == False:
            primes.append(i)
    else :
        continue
print ('Простые числа = ', primes)
print ('Непростые числа = ',  not_primes)
