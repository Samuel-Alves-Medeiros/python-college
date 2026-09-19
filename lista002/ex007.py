tentativas:list[str] = ["1234", "senha1", "abc123", "qwerty", "123456", "letmein", "senha123", "admin", "12345", "iloveyou"]
contador: int = 1
for tentativa in tentativas:
    print(f'tentativa {contador} : {tentativa}')
    contador+=1