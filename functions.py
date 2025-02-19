number = 0
roman = {
    1:"I",
    5:"V",
    10:"X",
    50:"L",
    100:"C",
    500:"D",
    1000:"M"
}

def request_number():
    """
    Solicita un numero y luego devuelve dicho numero.
    Si el usuario no ingresa un numero valido:
        1. Devuelve ValueError.
        2. Vuelve a solicitar un numero al usuario.
    Si el usuario ingresa un numero valido, devuelve dicho numero.
    """
    global number
    while True:
        try:
            number = int(input("Ingrese un numero positivo: "))
            if number < 0:
                raise ValueError(f'Usted ingreso un numero negativo: "{number}"')
            return number
        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese un numero valido: ')

def small_numbers_to_roman(sequence:list)->str:
    """
    Recibe una lista de numeros.
    Convierte los numeros a romanos.
    Devuelve en una sola cadena todos los numeros romanos concatenados.
    Funciona correctamente hasta 3999 inclusive.
    """
    result = ""  
    base = int("1"+ ("0" * (len(sequence)-1)))
    for index,number in enumerate(sequence):
        n = sequence[index] // base
        if n <= 3:
            result += n * roman[1*base]
        elif n == 4:
            result += roman[1*base] + roman[5*base]
        elif n < 9:
            result += roman[5*base] + (n - 5) * roman[1*base]
        elif n == 9:
            result += roman[1*base] + roman[10*base]
        base = base // 10
    return result

def big_numbers_to_roman(sequence:list)->str:
    """
    Recibe una lista de numeros.
    Convierte los numeros a romanos.
    Devuelve en una sola cadena todos los numeros romanos concatenados.
    Funciona con numeros superiores a 3999.
    """
    inverted = sequence[::-1]
    result = []
    count = len(inverted)-1
    for number in inverted:
        temp = separate_in_units(number)
        result.append(small_numbers_to_roman(temp))
        if number != 0:
            result.append("*"*count)
        count -= 1
    return "".join(result)

def separate_in_units(n:int)->list:
    """
    Recibe un numero entero.
    Devuelve en una lista la descomposicion de dicho numero.
    """
    string = str(n)
    units = []
    count = 1
    for i in string:
        units.append(int(i + ("0" * (len(string) - count))))
        count += 1
    return units

def separate_in_thousands(n:int)->list:
    in_thousands = []
    resto = n % 1000
    cociente = n // 1000
    while cociente >= 1000:
        in_thousands.append(resto)
        n = cociente 
        resto = n % 1000
        cociente = n // 1000
    if cociente <= 3:
        in_thousands.append(n)
    else:
        in_thousands.append(resto)
        in_thousands.append(cociente)
    return in_thousands

def to_roman(n:int)->str:
    if n >= 4000:
        separated = separate_in_thousands(n)
        return big_numbers_to_roman(separated)
    else:
        separated = separate_in_units()
        return small_numbers_to_roman(separated)

def start_program():
    numero = request_number()
    roman = to_roman(numero)
    return print(roman)