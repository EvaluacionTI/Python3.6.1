#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	02Feb2018
# Objetivo			:	Introducción a Python
# Fecha Edición		:
# Descripción		:
# Numeric Literals (Types : Integers, floating point numbers and imaginary numbers)
#**********************************************************************************
# Enteros literales
# integer      ::=  decinteger | bininteger | octinteger | hexinteger
# decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
# bininteger   ::=  "0" ("b" | "B") (["_"] bindigit)+
# octinteger   ::=  "0" ("o" | "O") (["_"] octdigit)+
# hexinteger   ::=  "0" ("x" | "X") (["_"] hexdigit)+
# nonzerodigit ::=  "1"..."9"
# digit        ::=  "0"..."9"
# bindigit     ::=  "0" | "1"
# octdigit     ::=  "0"..."7"
# hexdigit     ::=  digit | "a"..."f" | "A"..."F"

# Flotante literales
#******************
# floatnumber   ::=  pointfloat | exponentfloat
# pointfloat    ::=  [digitpart] fraction | digitpart "."
# exponentfloat ::=  (digitpart | pointfloat) exponent
# digitpart     ::=  digit (["_"] digit)*
# fraction      ::=  "." digitpart
# exponent      ::=  ("e" | "E") ["+" | "-"] digitpart

# Literales imaginarios
# imagnumber ::=  (floatnumber | digitpart) ("j" | "J")

#==============================================================================
print("Enteros Literales : ")

valor1 = 7
valor2 = -3
valor3 = 2147483647
valor4 = 79228162514264337593543950336
valor5 = 0o177
valor6 = 0o377
valor7 = 0xdeadbeef
valor8 = 100_000_000_000
valor9 = 0b100110111
valor10 = 0b_1110_0101
print(valor1)
print(valor2)
print(valor3)
print(valor4)
print("Octal = ", valor5)
print("Octal = ", valor6)
print(valor7)
print(valor8)
print(valor9)
print(valor10)

print("Flotante Literales : ")
valor1 = 10
valor2 = 10.
valor3 = .001
valor4 = 1e100
valor5 = 3.15e-10
valor6 = 0e0
valor7 = 3.14_15_93
print(valor1)
print(valor2)
print(valor3)
print(valor4)
print(valor5)
print(valor6)
print(valor7)

print("Imaginary Literals : ")
valor1 = 3.14j;
valor2 = 10.j;
valor3 = 10j
valor4 = .001j
valor5 = 1e100j
valor6 = 3.14e-10j
valor7 = 3.14_15_93j
print(valor1)
print(valor2)
print(valor3)
print(valor4)
print(valor5)
print(valor6)
print(valor7)