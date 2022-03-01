def validaCPF(CPF):
  # foi criado 3 vetor/lista:

  #cpf irá receber o CPF
  cpf = []

  #primeiroDigito irá receber o cálculo para verificiar se o primeiro digito é válido
  primeiroDigito = []

  #segundoDigito irá receber o cálculo para verificiar se o segundo digito é válido
  segundoDigito = []

# Um laço que percorrer a variável CPF e tranforma para inteiro e coloca esses valores no vetor cpf
  for n in CPF:
      cpf.append(int(n))
  
  tam = len(cpf)

  if tam > 11:
    quit("CPF Inválido")
  
  
  # Contadores
  i = 0

  #posição igual
  psi = 0

  #primeiro Digito
  pd = 10

  #segundo Digito
  sd = 11

  #Flag
  igual  = False

  #Verifica se todos os digitos são iguais
  while psi < (11-1):
    if (cpf[psi] == cpf[psi+1]) and (cpf[psi-1] == cpf[psi]):
      igual = True
    psi += 1

  if igual:
    quit("CPF Inválido")

 
  

  
  # Percorre o vetor cpf e multiplica cada posição de 10 até 2. Após percorrer, adiciona esses novos valores no vetor primeiroDigito  

  while i < 9:
    primeiroDigito.append(cpf[i]*pd)
    i += 1
    pd -= 1
  
  # print(cpf[0:9:1])
  # print(primeiroDigito)

  # Está fazendo a soma dos números, que estão dentro do vetor primeiroDigito e multiplicando por 10, e depois pegando o resto da divisão por 11  

  soma = (sum(primeiroDigito)*10) % 11
  if soma == cpf[9]:
      i = 0
      #Repete os mesmo passos que estão descritos na linha 47
      while i < 10:
        segundoDigito.append(cpf[i]*sd)
        i += 1
        sd -= 1
      #Repete o mesmo passo que está descrito na linha 57
      somaSD = (sum(segundoDigito)*10) % 11
      
      if somaSD == cpf[10]:
        print("CPF Válido")
      else:
        print("CPF Inválido")
        
  else:
     print("CPF Inválido")

     





CPF = input('Digite o CPF: ')
validaCPF(CPF)


  

