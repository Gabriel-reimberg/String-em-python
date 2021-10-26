endereco = "rua pontal do paraná, 125, casa, estados, fazenda rio grande, paraná, 83830-464"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()

print(cep)