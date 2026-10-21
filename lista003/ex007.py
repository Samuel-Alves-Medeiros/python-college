servidores:dict = {
"servidor1": "online",
"servidor2": "offline",
"servidor3": "online",
"servidor4": "offline",
"servidor5": "online"
}

servidores_offline:int = 0
for k,v in servidores.items():
    if v == 'offline':
        servidores_offline+=1

print(f'existem {servidores_offline} servidores offline')