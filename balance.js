const fs = require('fs');

let content = fs.readFileSync('./data.csv', 'utf8');
let lines = content.trim().split('\n');

// Convertimos a objetos
let operations = lines
  .slice(1) // omitir encabezado
  .map(line => {
    let [id, tipo, monto] = line.split(',');
    return { id: parseInt(id), tipo, monto: parseFloat(monto)};
  });

// Calculamos el balance total Crédito - Débito
let totalBalance = operations.reduce((x, y) => {
  return y.tipo === 'Crédito' ? x + y.monto : x - y.monto;
}, 0);

// Hallamos la operación con monto mayor
let maxAmount = operations.reduce((max, t) => {
  return t.monto > max.monto ? t : max;
});

// Contamos las operaciones por tipo: Crédito y Débito
let countTypes = operations.reduce((acc, t) => {
  acc[t.tipo] = (acc[t.tipo] || 0) + 1;
  return acc;
}, {});

// Mostramos el mensaje final
console.log("Reporte de Transacciones");
console.log("---------------------------------------------");
console.log(`Balance Final: ${totalBalance.toFixed(2)}`);
console.log(`Transacción de Mayor Monto: ID ${maxAmount.id} - ${maxAmount.monto.toFixed(2)}`);
console.log(`Conteo de Transacciones: Crédito: ${countTypes['Crédito'] || 0} Débito: ${countTypes['Débito'] || 0}`);