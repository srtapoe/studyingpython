# data atual
from datetime import date, timedelta

data_hoje = date.today()

data_futura = data_hoje + timedelta(+2)

print(f'A data de hoje eh {data_hoje}')
print(f'A data daqui 2 dias será {data_futura}')
