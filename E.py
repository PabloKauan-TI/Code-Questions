def somarNumeros(num):
    return sum(int(digito) for digito in str(num))

#recebe valores de numero de flores e posição de gertudre
entrada1 = input()
N, K = (int(number) for number in entrada1.split(' '))

#verifica os mesmos
if not 1<=N<=1000000:
    print('Valor fora do intervalo permitido')
    exit()
if not 1<=K<=1000000000:
    print('Valor fora do intervalo permitido')
    exit()
        
#recebe flores transformando em um vetor string3
P = input().split(' ')
for i in range(N):
    P[i] = int(P[i])

#verifica se foram listadas todas as alturas
if not len(P)==N:
    print('Não foi listado todos os brinquedos')
    exit()

flor = 0
for i in range(K):  
    P.sort(reverse=True)  
    if P[flor]==0 and flor<(N-1):
        flor+=1
    if P[flor]==0 and flor==(N-1):
        print(0)
        exit()
    if i==(K-1):
        R = somarNumeros(P[flor])
        print(R)
        exit()

    R = somarNumeros(P[flor])
    P[flor] = P[flor] - R