# Importamos metodo reduce
from functools import reduce 
# Leemos el archivo data.csv
content = open('./data.csv').read()
# Iniciamos un contador
count = 0
# inciamos un array
balance = []
for line in content.splitlines():
  # Si no es la primera linea
  if count > 0:
    # Dividimos la linea por cada ","
    parts = line.split(',')
    item = {"id": parts[0], "tipo": parts[1], "monto": float(parts[2])}
    # Agregamos al array
    balance.append(item)
  # Aumentamos en contador
  count = count + 1
# Calculamos el balance total Crédito - Débito
totalBalance = reduce(lambda x, y: x + y["monto"] if y["tipo"] == "Crédito" else x - y["monto"], balance, 0)
# Hallamos la operación con monto mayor
maxAmount = reduce(lambda x, y: y if y["monto"] > x["monto"] else x, balance)
# Contamos las operaciones por tipo: Crédito y Débito
countTypes = reduce(lambda x, y: {
  "Crédito": x["Crédito"] + 1 if y["tipo"] == "Crédito" else x["Crédito"], 
  "Débito": x["Débito"] + 1 if y["tipo"] == "Débito" else x["Débito"]
  },
  balance,
  { "Crédito": 0, "Débito": 0}
)
# Mostramos el mensaje final
print(f'''
Reporte de Transacciones
--------------------------------------------------
Balance Final: %s
Transacción de Mayor Monto: ID %s - %s
Conteo de transacciones: Crédito: %s Débito: %s
''' % (totalBalance, maxAmount["id"], maxAmount["monto"], countTypes["Crédito"], countTypes["Débito"]))
