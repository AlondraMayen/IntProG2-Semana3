//Un estudiante desea conocer el monto total que deberá pagar para poder matricularse en una universidad. La institución realiza tres tipos de cobros:
Algoritmo  calcular_pago_matricula
    Definir prematricula, matricula, valor_semestre, porcentaje_semestre, total_pagar Como Real
	Definir nombre_completo Como Caracter
    // Solicitar datos al estudiante
    Escribir "Ingrese su nombre: "
	Leer nombre_completo
	Escribir "Ingrese el valor de la prematrícula (dolares): "
    Leer prematricula
    Escribir "Ingrese el valor de la matrícula (dolares): "
    Leer matricula
    Escribir "Ingrese el valor total del semestre (dolares): " 
    Leer valor_semestre
    // Calcular el 25% del semestre
    porcentaje_semestre= valor_semestre * 0.25 //Ya que el procentaje es de 25%
    // Calcular el total a pagar
    total_pagar = prematricula + matricula + porcentaje_semestre
    // Mostrar el monto total a pagar
    Escribir "El monto total que deberá pagar es: ", total_pagar " $."
FinProceso