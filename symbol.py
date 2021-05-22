class SymbolTable(object):
    """
    Classe com o propósito de ser um dicionário de símbolos dentro de um mesmo código
    """
    def __init__(self):
        self.symbols = {}

    def setVariable(self, var, value, tipo):
        if (tipo not in ["bool", "palavra", "int"]):
            raise KeyError(f"Não foi possível identificar o tipo '{tipo}'.")
        self.symbols[var] = [value, tipo]
        
    def getVariable(self, var):
        if (var not in self.symbols):
            raise KeyError(f"A variável '{var}' não foi inicializada.")
        return self.symbols[var]

    def updateValue(self, var, newValue):
        try:
            self.symbols[var][0] = newValue
        except KeyError as e:
            print(f"A variável '{var}' não é conhecida ou não foi declarada")
        
