print('Digite algo: ',end="")
v= input()

print('O tipo primitivo desse valor é ',type(v))
print('Só tem espaços ?',v.isspace())
print('É número ?',v.isnumeric())
print('É alfabético ?',v.isalpha())
print('É alfanumérico ?',v.isalnum())
print('Está em maiúscula ?', v.isupper())
print('Está em minúscula ?', v.islower())
print('Está capitalizada ?', v.istitle())
