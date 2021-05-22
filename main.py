import sys, copy
from node import Node, BinOp, UnOp, VarChar, InstructionBlock, IntVal, NoOp, FullNodeException, NoChildException, UnknownOperation, StringVal, BoolVal
from symbol import SymbolTable

class Token(object):

    def __init__(self, tipo: str, value: int):
        self.tipo = tipo
        self.value = value

class Tokenizer(object):

    def __init__(self, origin: str):
        self.origin = origin
        self.position = 0
        self.actual = Token("", 0)

    def selectNext(self):
        # Lê o próximo token e atualiza o atributo atual
        self.actual.value = self.origin[self.position]
        self.position += 1
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"

        if (self.actual.value.isnumeric()):
            self.actual.tipo = "int"
            return
        elif (self.actual.value == "+"):
            self.actual.tipo = "soma"
            return
        elif (self.actual.value == "-"):
            self.actual.tipo = "sub"
            return
        elif (self.actual.value == " " or self.actual.value == "\t"):
            self.actual.tipo = "espaco"
            return
        elif (self.actual.value == "*"):
            self.actual.tipo = "mult"
            return
        elif (self.actual.value == "/"):
            self.actual.tipo = "div"
            return
        elif (self.actual.value == "("):
            self.actual.tipo = "open_parentheses"
            return
        elif (self.actual.value == ")"):
            self.actual.tipo = "close_parentheses"
            return
        elif (self.actual.value == "{"):
            self.actual.tipo = "open_brackets"
            return
        elif (self.actual.value == "}"):
            self.actual.tipo = "close_brackets"
            return
        elif (self.actual.value == "="):
            self.actual.tipo = "equals"
            return
        elif (self.actual.value == ">"):
            self.actual.tipo = "greater"
            return
        elif (self.actual.value == "<"):
            self.actual.tipo = "lesser"
            return
        elif (self.actual.value == "!"):
            self.actual.tipo = "neg"
            return
        elif (self.actual.value == "|"):
            self.actual.tipo = "or"
            return
        elif (self.actual.value == "&"):
            self.actual.tipo = "and"
            return
        elif (self.actual.value == '"'):
            self.actual.tipo = "aspas"
            return
        elif (self.actual.value in alphabet):
            self.actual.tipo = "caractere"
            return
        else:
            raise KeyError()

class PrePro(object):

    def __init__(self):
        pass

    def filter(self, code):
        new_code = ""
        comment_flag = False
        i, j = 0, 0
        new_fullCode = []

        while (i < len(code)):
            j = 0
            while (j < len(code[i])):
                if (comment_flag):
                    if (code[i][j] == "*" and code[i][j+1] == "/"):
                        comment_flag = False
                        j += 2
                        continue
                else:
                    if (code[i][j] == "/" and code[i][j+1] == "*"):
                        comment_flag = True
                        j += 1
                    else:
                        new_code += code[i][j]
                j+=1
            i += 1

            if (comment_flag):
                raise KeyError
            if (len(new_code) > 0):
                new_fullCode.append(new_code)

            comment_flag = False
            new_code = ""
            
        return new_fullCode
    
    def separateLines(self, code):
        lines = []
        new_line = ""
        j = 0
        self.openedBrackets = []
        pointer = 0
        # Procura o primeiro bloco
        initialBlock = False
        while (len(code) > 0):
            if (("{" in code[0]) and (code[0][:code[0].index('{')+1].replace(' ', '') == "{")):
                initialBlock = True
                break
            del code[0]
        if not initialBlock:
            raise KeyError("Bloco de comando deve iniciar com um '{'")
        while (j < len(code)):
            space = 0
            # canBeOpenBrackets = False
            pontoEVirgulaFlag = False
            # print(f"linha: '{code[j]}'")

            for i in code[j]:
                # print(f"\tchar: '{i}'")
                if (i == "\n"):
                    if (space == 1):
                        space = 2
                    new_line += ""
                elif (i == "{"):
                    new_line += i
                    lines.append(new_line)
                    new_line =  ""
                    self.openedBrackets.append(False)
                    pointer += 1
                elif (i == ";"): 
                    lines.append(new_line)
                    new_line =  ""
                    pontoEVirgulaFlag = True
                elif (len(self.openedBrackets) > 0 and (not self.openedBrackets[pointer-1]) and i == "}"):
                    if (len(new_line.replace(" ", "")) > 0 and not pontoEVirgulaFlag):
                        raise KeyError("Faltou um ';'")
                    new_line += i
                    lines.append(new_line)
                    new_line = ""
                    del self.openedBrackets[pointer - 1]
                    pointer -= 1
                else:
                    if (i.isnumeric() and space == 0):
                        space = 1
                    elif (i == " " and space == 1):
                        space = 2
                    elif ((i.isnumeric() or i == " " or i == "\n") and space == 2):
                        raise KeyError
                    else:# elif (space == 2):
                        space = 0
                    new_line += i
            j += 1

        if (len(new_line.replace(" ", "")) > 0 and not pontoEVirgulaFlag):
            raise KeyError("Faltou um ';'")

        if(len(new_line.replace(" ","")) == 0):
            new_line = ""

        if (len(new_line) > 0):
            raise KeyError

        for bracket in self.openedBrackets:
            if not bracket:
                raise KeyError
        return lines
        
class Parser(object):

    def __init__(self):
        self.parentheses_counter = 0
        self.reservedWords = ["imprimir", "se", "senao", "caso", "enquanto", "entrada", "int", "bool", "palavra", "false", "true"]
        self.equalFlag = False
        self.flagIfCondition = False
        self.jump = False
        self.jumpLoop = False
        self.isAConditionLine = False
        self.conditions = {}
        self.lastCondition = False
        self.conditionsState = []
        self.isALoop = False
        self.isACommandBlockCondition = True
        self.insideTheCondition = [False, False]
        self.stringLine = False
        self.varEqual = None
        self.aspasFlag = False
        # self.a = 0

    def parseExpression(self, mToken, rerun = False):
        tamanho = len(mToken.origin)
        allNodes = []
        actualNodes = []
        flagEspaco = 0
        actual_int = []
        valor_atual, pot = 0, 0
        movedPositions = 0
        myActualVar = ""
        myActualType = ""
        myVars = []
        orAndFlag = False
        weAreOnALoop = weAreOnAIf = False
        lessOrGreat = 0                 # 1 caso seja '>=' e -1 caso seja '<=' senão é 0
        negFlag = False
        isATypeDeclaration = False
        # print("\n==================================================")
        # print(f"agora vamo de: '{mToken.origin}'")
        while (mToken.position < tamanho):
            mToken.selectNext()
            movedPositions += 1
            # print(f"allNodes = {allNodes}")
            # print(f"actualNodes = {actualNodes}")
            # print(f"flagEspaco = {flagEspaco}")
            # print(f"actual = '{mToken.actual.value}'\n")
            if (mToken.actual.tipo == "int"):
                if (flagEspaco == 0):
                    flagEspaco = 1
                elif (flagEspaco == 2):
                    raise KeyError
                if (len(myActualVar) > 0 and pot == 0):
                    myActualVar += mToken.actual.value
                    continue
                if (self.insideTheCondition[0] and not self.insideTheCondition[1] and not self.isACommandBlockCondition and not self.jump):
                    # é uma condição de uma linha
                    return

                actual_int.append(mToken.actual.value)

            elif (mToken.actual.tipo == "caractere"):
                if (flagEspaco == 3):
                    if (myActualVar == "caso" and mToken.origin[movedPositions-1:movedPositions+1] == "se"):
                        flagEspaco = 0
                        myActualVar += " "
                    elif (myActualVar == "bool"):
                        flagEspaco = 0
                        myActualType = myActualVar
                        isATypeDeclaration = True
                        myActualVar = ""
                    elif (myActualVar == "palavra"):
                        flagEspaco = 0
                        myActualType = myActualVar
                        isATypeDeclaration = True
                        myActualVar = ""
                    elif (myActualVar == "int"):
                        flagEspaco = 0
                        myActualType = myActualVar
                        isATypeDeclaration = True
                        myActualVar = ""
                
                if (self.insideTheCondition[0] and not self.insideTheCondition[1] and not self.isACommandBlockCondition and not self.jump):
                    # é uma condição de uma linha
                    return
                if (len(allNodes) > 0 and isinstance(allNodes[-1], IntVal) and self.isACommandBlockCondition):
                    raise KeyError
                if (len(actual_int) > 0):
                    raise KeyError
                myActualVar += mToken.actual.value
                continue

            elif (mToken.actual.tipo == "aspas"):
                # É uma string
                if (self.aspasFlag):
                    self.aspasFlag = False
                    continue
                self.aspasFlag = True
                if (mToken.origin.count('"') > 2):
                    raise KeyError("Tem mais aspas do que o esperado")
                
                myString = mToken.origin[movedPositions:movedPositions+mToken.origin[movedPositions:].index('"')]
                n = StringVal(myString)
                allNodes.append(n)
                actualNodes.append(n)
                if (rerun):
                    movedPositions += len(myString)
                    mToken.position += len(myString)
                    continue

                break
            
            elif (mToken.actual.tipo == "equals"):
                if not self.equalFlag:
                    if (flagEspaco == 3):
                        flagEspaco = 0
                    if ((not self.isAConditionLine) and (not self.isALoopConditionLine)):
                        self.equalFlag = True
                        n = VarChar(myActualVar)
                        allNodes.append(n)
                        actualNodes.append(n)
                        myVars.append(n)
                        myActualVar = ""
                        self.varEqual = allNodes[0]
                        continue
                    else:
                        if (len(actual_int) > 0):
                            for i in range(len(actual_int)):
                                valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                            n = IntVal(valor_atual)
                            actualNodes.append(n)
                            allNodes.append(n)
                            valor_atual, pot = 0, 0
                            actual_int = []
                        
                        # Checa se tem alguma string
                        if (len(myActualVar) > 0 and not self.isALoopConditionLine):
                            if (myActualVar in ["false", "true"] and self.symbols.getVariable(allNodes[0].value)[1] == "bool"):
                                last_value = myActualVar
                                last_value_tipo = "bool"
                            else:
                                last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                                last_value_tipo = self.symbols.getVariable(myActualVar)[1]
                            if (last_value_tipo == "int"):
                                n = IntVal(last_value)
                            elif (last_value_tipo == "bool"):
                                n = BoolVal(last_value)
                            elif (last_value_tipo == "palavra"):
                                n = StringVal(last_value)

                            if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                                n.setParent(actualNodes[len(actualNodes)-1])
                                actualNodes[len(actualNodes)-1].addChild(n) # filho
                            else:
                                actualNodes.append(n)
                            allNodes.append(n)
                            myVars.append(n)
                            myActualVar = ""
                        
                        elif (len(myActualVar) > 0 and self.isALoopConditionLine):
                            # n = copy.copy(self.symbols.getVariable(myActualVar))
                            if (myActualVar in ["false", "true"] and self.symbols.getVariable(allNodes[0].value)[1] == "bool"):
                                last_value = myActualVar
                                last_value_tipo = "bool"
                                n = BoolVal(last_value)
                            else:
                                n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                            if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                                n.setParent(actualNodes[len(actualNodes)-1])
                                actualNodes[len(actualNodes)-1].addChild(n) # filho
                            else:
                                actualNodes.append(n)
                            allNodes.append(n)
                            myVars.append(n)
                            myActualVar = ""

                        self.equalFlag = True
                        self.varEqual = allNodes[0]
                        
                        if (lessOrGreat > 0):
                            # Caso Greater Equal
                            n = BinOp(">=")
                            n.addChild(actualNodes[len(actualNodes)-1])
                            actualNodes[len(actualNodes)-1].setParent(n)
                            del actualNodes[len(actualNodes)-1]
                            actualNodes.append(n)
                            allNodes.append(n)
                        elif (lessOrGreat < 0):
                            # Caso Lesser Equal
                            n = BinOp("<=")
                            n.addChild(actualNodes[len(actualNodes)-1])
                            actualNodes[len(actualNodes)-1].setParent(n)
                            del actualNodes[len(actualNodes)-1]
                            actualNodes.append(n)
                            allNodes.append(n)
                        elif (negFlag):
                            n = BinOp("!=")
                            n.addChild(actualNodes[len(actualNodes)-1])
                            actualNodes[len(actualNodes)-1].setParent(n)
                            del actualNodes[len(actualNodes)-1]
                            actualNodes.append(n)
                            allNodes.append(n)
                            negFlag = False
                                
                else:
                    if (((mToken.origin.count("=") > 2 and not rerun) or (mToken.origin.count("=") >= 2 and rerun)) and not self.isAConditionLine and mToken.origin[movedPositions-1:movedPositions+1] == "=="):
                        # Checa se tem algum número pra ser anotado
                        if (len(actual_int) > 0):
                            for i in range(len(actual_int)):
                                valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                            n = IntVal(valor_atual)
                            actualNodes.append(n)
                            allNodes.append(n)
                            valor_atual, pot = 0, 0
                            actual_int = []
                        
                        # Checa se tem alguma string       
                        if (len(myActualVar) > 0):
                            if (myActualVar in ["false", "true"] and self.symbols.getVariable(allNodes[0].value)[1] == "bool"):
                                last_value = myActualVar
                                last_value_tipo = "bool"
                            else:
                                last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                                last_value_tipo = self.symbols.getVariable(myActualVar)[1]
                            if (last_value_tipo == "int"):
                                n = IntVal(last_value)
                            elif (last_value_tipo == "bool"):
                                n = BoolVal(last_value)
                            elif (last_value_tipo == "palavra"):
                                n = StringVal(last_value)

                            if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                                n.setParent(actualNodes[len(actualNodes)-1])
                                actualNodes[len(actualNodes)-1].addChild(n) # filho
                            else:
                                actualNodes.append(n)
                            allNodes.append(n)
                            myVars.append(n)
                            myActualVar = ""

                        if (len(actualNodes) > 0 and ((isinstance(actualNodes[len(actualNodes)-1], IntVal) or (isinstance(actualNodes[len(actualNodes)-1], BoolVal)) or (isinstance(actualNodes[len(actualNodes)-1], StringVal))) or isinstance(actualNodes[len(actualNodes)-1], VarChar))):
                            # Cria Node
                            n = BinOp("==")
                            n.addChild(actualNodes[len(actualNodes)-1])
                            actualNodes[len(actualNodes)-1].setParent(n)
                            del actualNodes[len(actualNodes)-1]
                            actualNodes.append(n)
                            allNodes.append(n)
                            mToken.position += 1
                            movedPositions += 1
                        else:
                            raise KeyError
                        
                    elif (self.isAConditionLine or self.isALoopConditionLine):
                        # Checa se tem algum número pra ser anotado
                        if (len(actual_int) > 0):
                            for i in range(len(actual_int)):
                                valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                            n = IntVal(valor_atual)
                            actualNodes.append(n)
                            allNodes.append(n)
                            valor_atual, pot = 0, 0
                            actual_int = []
                        
                        # Checa se tem alguma string
                        if (len(myActualVar) > 0 and not self.isALoopConditionLine):
                            last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                            n = IntVal(last_value)
                            if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                                n.setParent(actualNodes[len(actualNodes)-1])
                                actualNodes[len(actualNodes)-1].addChild(n) # filho
                            else:
                                actualNodes.append(n)
                            allNodes.append(n)
                            myVars.append(n)
                            myActualVar = ""

                        elif (len(myActualVar) > 0 and self.isALoopConditionLine):
                            n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                            # n = IntVal(last_value)
                            if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                                n.setParent(actualNodes[len(actualNodes)-1])
                                actualNodes[len(actualNodes)-1].addChild(n) # filho
                            else:
                                actualNodes.append(n)
                            allNodes.append(n)
                            myVars.append(n)
                            myActualVar = ""
                        if (len(actualNodes) > 0 and (isinstance(actualNodes[len(actualNodes)-1], IntVal) or isinstance(actualNodes[len(actualNodes)-1], StringVal) or isinstance(actualNodes[len(actualNodes)-1], BoolVal) or isinstance(actualNodes[len(actualNodes)-1], VarChar))):
                            # Cria Node
                            n = BinOp("==")
                            n.addChild(actualNodes[len(actualNodes)-1])
                            actualNodes[len(actualNodes)-1].setParent(n)
                            del actualNodes[len(actualNodes)-1]
                            actualNodes.append(n)
                            allNodes.append(n)
                            self.equalFlag = False
                        else:
                            raise KeyError
                    else:
                        raise KeyError
                flagEspaco = 0
                continue

            elif (mToken.actual.tipo == "greater"):
                # Com certeza é BinOp

                # Checa se tem algum número pra ser anotado
                if (len(actual_int) > 0):
                    for i in range(len(actual_int)):
                        valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                    n = IntVal(valor_atual)
                    actualNodes.append(n)
                    allNodes.append(n)
                    valor_atual, pot = 0, 0
                    actual_int = []
                
                # Checa se tem alguma string
                if (len(myActualVar) > 0 and not self.isALoopConditionLine):
                    last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                    n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""
                
                elif (len(myActualVar) > 0 and self.isALoopConditionLine):
                    n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                    # n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""

                if (mToken.origin[movedPositions] != "="):
                    if (len(actualNodes) > 0 and (isinstance(actualNodes[len(actualNodes)-1], IntVal) or isinstance(actualNodes[len(actualNodes)-1], VarChar))):
                        # Checar se não há uma conta ou UnOp já existente
                        if (len(actualNodes) >= 2 and (isinstance(actualNodes[len(actualNodes)-2], UnOp) or isinstance(actualNodes[len(actualNodes)-2], BinOp))):
                            # Primeiro adiciona o IntVal/VarChar no UnOp/BinOp já existente
                            actualNodes[len(actualNodes) - 2].addChild(actualNodes[len(actualNodes) - 1])
                            actualNodes[len(actualNodes) - 1].setParent(actualNodes[len(actualNodes) - 2])
                            del actualNodes[len(actualNodes) - 1]
                        # Cria Node
                        n = BinOp(mToken.actual.value)
                        n.addChild(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].setParent(n)
                        del actualNodes[len(actualNodes)-1]
                        actualNodes.append(n)
                        allNodes.append(n)
                    else:
                        raise KeyError()
                else:
                    lessOrGreat = 1
                flagEspaco = 0

            elif (mToken.actual.tipo == "lesser"):
                # Com certeza é BinOp

                # Checa se tem algum número pra ser anotado
                if (len(actual_int) > 0):
                    for i in range(len(actual_int)):
                        valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                    n = IntVal(valor_atual)
                    actualNodes.append(n)
                    allNodes.append(n)
                    valor_atual, pot = 0, 0
                    actual_int = []
                
                # Checa se tem alguma string
                if (len(myActualVar) > 0 and not self.isALoopConditionLine):
                    last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                    n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""
                    
                elif (len(myActualVar) > 0 and self.isALoopConditionLine):
                    n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                    # n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""

                if (mToken.origin[movedPositions] != "="):
                    if (len(actualNodes) > 0 and (isinstance(actualNodes[len(actualNodes)-1], IntVal) or isinstance(actualNodes[len(actualNodes)-1], VarChar) or isinstance(actualNodes[len(actualNodes)-1], StringVal) or isinstance(actualNodes[len(actualNodes)-1], BoolVal))):
                        # Checar se não há uma conta ou UnOp já existente
                        if (len(actualNodes) >= 2 and (isinstance(actualNodes[len(actualNodes)-2], UnOp) or isinstance(actualNodes[len(actualNodes)-2], BinOp))):
                            # Primeiro adiciona o IntVal/VarChar no UnOp/BinOp já existente
                            actualNodes[len(actualNodes) - 2].addChild(actualNodes[len(actualNodes) - 1])
                            actualNodes[len(actualNodes) - 1].setParent(actualNodes[len(actualNodes) - 2])
                            del actualNodes[len(actualNodes) - 1]
                            
                        # Cria Node
                        n = BinOp(mToken.actual.value)
                        n.addChild(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].setParent(n)
                        del actualNodes[len(actualNodes)-1]
                        actualNodes.append(n)
                        allNodes.append(n)

                    else:
                        raise KeyError()
                else:
                    lessOrGreat = -1
                flagEspaco = 0

            elif (mToken.actual.tipo == "or"):
                if (orAndFlag):
                    orAndFlag = False
                    continue
                # Checa se tem algum número pra ser anotado
                if (len(actual_int) > 0):
                    for i in range(len(actual_int)):
                        valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                    n = IntVal(valor_atual)
                    actualNodes.append(n)
                    allNodes.append(n)
                    valor_atual, pot = 0, 0
                    actual_int = []
                
                # Checa se tem alguma string
                if (len(myActualVar) > 0 and not (self.isAConditionLine or self.isALoopConditionLine)):
                    if (myActualVar in ["true", "false"] and self.symbols.getVariable(allNodes[0].value)[1] == "bool"):
                        last_value = myActualVar
                        last_value_tipo = "bool"
                    else:
                        last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                        last_value_tipo = self.symbols.getVariable(myActualVar)[1]
                    if (last_value_tipo == "int"):
                        n = IntVal(last_value)
                    elif (last_value_tipo == "bool"):
                        n = BoolVal(last_value)
                    elif (last_value_tipo == "palavra"):
                        n = StringVal(last_value)

                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""
                
                elif (len(myActualVar) > 0 and (self.isAConditionLine or self.isALoopConditionLine)):
                    if (myActualVar in ["true", "false"]):
                        last_value = myActualVar
                        last_value_tipo = "bool"
                        n = BoolVal(last_value)
                    else:
                        n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""
                    
                elif (len(myActualVar) > 0 and self.isALoopConditionLine):
                    n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                    # n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""

                if (len(actualNodes) > 0 and (self.isAConditionLine or self.isALoopConditionLine or self.equalFlag) and mToken.origin[movedPositions-1:movedPositions+1] == "||"):
                    # Com certeza é BinOp
                    n = BinOp("||")
                    n.addChild(actualNodes[len(actualNodes)-1])
                    actualNodes[len(actualNodes)-1].setParent(n)
                    del actualNodes[len(actualNodes)-1]
                    actualNodes.append(n)
                    allNodes.append(n)
                    orAndFlag = True
                else:
                    raise KeyError
                flagEspaco = 0
                continue
            
            elif (mToken.actual.tipo == "and"):
                if (orAndFlag):
                    orAndFlag = False
                    continue
                # Checa se tem algum número pra ser anotado
                if (len(actual_int) > 0):
                    for i in range(len(actual_int)):
                        valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                    n = IntVal(valor_atual)
                    actualNodes.append(n)
                    allNodes.append(n)
                    valor_atual, pot = 0, 0
                    actual_int = []
                
                # Checa se tem alguma string
                if (len(myActualVar) > 0 and not (self.isAConditionLine or self.isALoopConditionLine)):
                    if (myActualVar in ["false", "true"]):
                        last_value = myActualVar
                        last_value_tipo = "bool"
                    else:
                    # print(f"type -> '{type(self.symbols.getVariable(myActualVar)[0])}'")
                        last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                        last_value_tipo = self.symbols.getVariable(myActualVar)[1]
                    if (last_value_tipo == "int"):
                        n = IntVal(last_value)
                    elif (last_value_tipo == "bool"):
                        n = BoolVal(last_value)
                    elif (last_value_tipo == "palavra"):
                        n = StringVal(last_value)

                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""
                
                elif (len(myActualVar) > 0 and (self.isAConditionLine or self.isALoopConditionLine)):
                    # n = copy.copy(self.symbols.getVariable(myActualVar))
                    if (myActualVar in ["false", "true"]):
                        last_value = myActualVar
                        last_value_tipo = "bool"
                        n = BoolVal(last_value)
                    else:
                        n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""
                    
                elif (len(myActualVar) > 0 and self.isALoopConditionLine):
                    n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                    # n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""

                if (len(actualNodes) > 0 and (self.isAConditionLine or self.isALoopConditionLine or self.equalFlag) and mToken.origin[movedPositions-1:movedPositions+1] == "&&"):
                    # Com certeza é BinOp
                    n = BinOp("&&")
                    n.addChild(actualNodes[len(actualNodes)-1])
                    actualNodes[len(actualNodes)-1].setParent(n)
                    del actualNodes[len(actualNodes)-1]
                    actualNodes.append(n)
                    allNodes.append(n)
                    orAndFlag = True
                else:
                    raise KeyError
                flagEspaco = 0
                continue

            elif (mToken.actual.tipo == "neg"):
                if ((mToken.origin[movedPositions-1:].replace(" ", "")[0:2] == "!=") and not negFlag):
                    negFlag = True
                    continue
                elif (negFlag):
                    raise KeyError
                # Checa se tem algum número pra ser anotado
                if (len(actual_int) > 0):
                    for i in range(len(actual_int)):
                        valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                    n = IntVal(valor_atual)
                    actualNodes.append(n)
                    allNodes.append(n)
                    valor_atual, pot = 0, 0
                    actual_int = []
                
                # Checa se tem alguma string
                if (len(myActualVar) > 0 and not self.isALoopConditionLine):
                    last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                    n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""
                    
                elif (len(myActualVar) > 0 and self.isALoopConditionLine):
                    n = copy.copy(self.symbols.getVariable(myActualVar)[0])
                    # n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""

                if (mToken.origin[movedPositions-1:].replace(" ", "")[0:2] == "!(" and (self.isAConditionLine or self.isALoopConditionLine or self.equalFlag)):
                    # Com certeza é UnOp
                    n = UnOp(mToken.actual.value)
                    if (len(actualNodes) > 0 and (isinstance(actualNodes[len(actualNodes)-1], UnOp) or isinstance(actualNodes[len(actualNodes)-1], BinOp))):
                        try:
                            n.setParent(actualNodes[len(actualNodes)-1])
                            if ((actualNodes[len(actualNodes)-1].getParent() == None) and len(actualNodes) >= 2):
                                actualNodes[len(actualNodes)-1].setParent(actualNodes[len(actualNodes)-2])
                                actualNodes[len(actualNodes)-2].addChild(actualNodes[len(actualNodes)-1])
                                del actualNodes[len(actualNodes)-2]
                            actualNodes[len(actualNodes)-1].addChild(n)
                            del actualNodes[len(actualNodes)-1]
                        except FullNodeException:
                            raise KeyError
                    actualNodes.append(n)
                    allNodes.append(n)
                else:
                    raise KeyError
                flagEspaco = 0
                continue
            

            elif (mToken.actual.tipo == "soma" or mToken.actual.tipo == "sub"):
                # Pode ser BinOp ou UnOp
                # Primeiro checa se tem algum número para colocar no actualNodes
                if (len(actual_int) > 0):
                    for i in range(len(actual_int)):
                        valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                    n = IntVal(valor_atual)
                    actualNodes.append(n)
                    allNodes.append(n)
                    valor_atual, pot = 0, 0
                    actual_int = []
                
                if (len(myActualVar) > 0):
                    if (myActualVar in ["true", "false"]):
                        last_value = myActualVar
                        n = BoolVal(last_value)
                    else:
                        last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                        n = IntVal(last_value)
                    if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                        n.setParent(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].addChild(n) # filho
                    else:
                        actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""

                # Checa se é UnOp
                if (len(actualNodes) == 0 or isinstance(actualNodes[len(actualNodes)-1], UnOp) or (isinstance(actualNodes[len(actualNodes)-1], BinOp) and len(actualNodes[len(actualNodes)-1].getAllChild()) <= 1)):
                    # Caso onde a operacao revela ser uma operação unaria
                    n = UnOp(mToken.actual.value)
                    if (len(actualNodes) > 0 and (isinstance(actualNodes[len(actualNodes)-1], UnOp) or isinstance(actualNodes[len(actualNodes)-1], BinOp))):
                        try:
                            n.setParent(actualNodes[len(actualNodes)-1])
                            if ((actualNodes[len(actualNodes)-1].getParent() == None) and len(actualNodes) >= 2):
                                actualNodes[len(actualNodes)-1].setParent(actualNodes[len(actualNodes)-2])
                                actualNodes[len(actualNodes)-2].addChild(actualNodes[len(actualNodes)-1])
                                del actualNodes[len(actualNodes)-2]
                            actualNodes[len(actualNodes)-1].addChild(n)
                            del actualNodes[len(actualNodes)-1]
                        except FullNodeException:
                            raise KeyError
                    actualNodes.append(n)
                    allNodes.append(n)

                # Caso nao seja UnOp, deve ser BinOp
                elif (len(actualNodes) > 0):
                    if not self.isAConditionLine or not self.isALoopConditionLine:
                        if (isinstance(actualNodes[0], BinOp) and len(actualNodes) > 1):
                            actualNodes[0].addChild(actualNodes[1])
                            actualNodes[1].setParent(actualNodes[0])
                            del actualNodes[1]
                        # Caso a operação seja Binária
                        n = BinOp(mToken.actual.value)
                        
                        n.addChild(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].setParent(n)
                        del actualNodes[len(actualNodes)-1]
                        
                        actualNodes.append(n)
                        allNodes.append(n)
                    else:
                        if (len(actualNodes) > 1 and isinstance(actualNodes[1], BinOp)):
                            actualNodes[1].addChild(actualNodes[2])
                            actualNodes[2].setParent(actualNodes[1])
                            del actualNodes[2]
                        # Caso a operação seja Binária
                        n = BinOp(mToken.actual.value)
                        
                        n.addChild(actualNodes[len(actualNodes)-1])
                        actualNodes[len(actualNodes)-1].setParent(n)
                        del actualNodes[len(actualNodes)-1]
                        
                        actualNodes.append(n)
                        allNodes.append(n)
                flagEspaco = 0

            elif (mToken.actual.tipo == "mult" or mToken.actual.tipo == "div"):
                # Com certeza é BinOp!
                if (len(actual_int) > 0):
                    for i in range(len(actual_int)):
                        valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
                    n = IntVal(valor_atual)
                    actualNodes.append(n)
                    allNodes.append(n)
                    valor_atual, pot = 0, 0
                    actual_int = []
                
                if (len(myActualVar) > 0):
                    if (myActualVar in ["true", "false"]):
                        last_value = myActualVar
                        n = BoolVal(last_value)
                    else:
                        last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                        n = IntVal(last_value)
                    actualNodes.append(n)
                    allNodes.append(n)
                    myVars.append(n)
                    myActualVar = ""

                if (len(actualNodes) == 0):
                    raise KeyError
                n = BinOp(mToken.actual.value)
                n.addChild(actualNodes[len(actualNodes)-1])
                actualNodes[len(actualNodes)-1].setParent(n)
                del actualNodes[len(actualNodes)-1]
                if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], BinOp)):
                    n.setParent(actualNodes[len(actualNodes)-1])
                    actualNodes[len(actualNodes)-1].addChild(n)
                    del actualNodes[len(actualNodes)-1]
                actualNodes.append(n)
                allNodes.append(n)
                flagEspaco = 0

            elif (mToken.actual.tipo == "espaco"):
                if (len(myActualVar) > 0):
                    flagEspaco = 3
                if (flagEspaco == 1):
                    flagEspaco = 2

            elif (mToken.actual.tipo == "open_parentheses"):
                if (len(myActualVar) > 0):
                    # print(f"myActualVar = {myActualVar}")
                    if (myActualVar == "imprimir"):
                        self.itIsAPrint = True
                    elif (myActualVar == "entrada"):
                        self.flagInputLn = True
                    elif (myActualVar == "se" or myActualVar == "caso se"):
                        self.isAConditionLine = True
                        self.flagIfCondition = True
                        self.jump = False
                        self.insideTheCondition = [True, True]
                        weAreOnAIf = True
                    elif (myActualVar == "enquanto"):
                        self.isALoop = True
                        self.isALoopConditionLine = True
                        self.jumpLoop = False
                        weAreOnALoop = True
                    else:
                        raise KeyError
                    myActualVar = ""
                self.parentheses_counter += 1
                newTokens = Tokenizer(origin = mToken.origin[mToken.position:])
                parenthesesNode, m = self.parseExpression(newTokens, True)
                try:
                    newInteger = int(parenthesesNode.Evaluate())
                    parenthesesNode = IntVal(newInteger)
                except:
                    if (isinstance(parenthesesNode, BoolVal) or str(parenthesesNode.Evaluate()) in ["True", "False"]):
                        newBoolean = str(parenthesesNode.Evaluate())
                        parenthesesNode = BoolVal(newBoolean.lower())
                    elif(isinstance(parenthesesNode, StringVal)):
                        newString = parenthesesNode.Evaluate()
                        parenthesesNode = StringVal(newString)

                if (self.itIsAPrint):
                    nPrint = InstructionBlock("imprimir")
                    parenthesesNode.setParent(nPrint)
                    nPrint.addChild(parenthesesNode)
                    self.symbols.setVariable("imprimir", nPrint, "palavra")
                elif (self.flagInputLn and self.equalFlag):
                    nReadln = InstructionBlock("entrada")
                    nReadln.addChild(parenthesesNode)
                    parenthesesNode.setParent(nReadln)
                    self.symbols.setVariable(myVars[0].value, nReadln, "int")
                    allNodes.append(nReadln)
                elif (self.isALoop and self.isALoopConditionLine and weAreOnALoop):
                    nWhile = InstructionBlock("enquanto")
                    if (parenthesesNode.value not in [">", "<", "==", ">=", "<=", "||", "&&", "!="] and parenthesesNode.value != 1 and parenthesesNode.value != 0):
                        raise KeyError
                    nWhile.addChild(parenthesesNode)
                    parenthesesNode.setParent(nWhile)
                    self.jumpLoop = parenthesesNode.Evaluate()
                    self.loopInfo[len(self.loopInfo) - 1].append(nWhile)
                    weAreOnALoop = False
                    
                elif (self.flagIfCondition and weAreOnAIf):
                    nIfBlock = InstructionBlock("se")
                    if (parenthesesNode.value not in [">", "<", "==", ">=", "<=", "||", "&&", "!=", "!", "true", "false"] and not isinstance(parenthesesNode.value, int)):
                        raise KeyError
                    nIfBlock.addChild(parenthesesNode)
                    parenthesesNode.setParent(nIfBlock)
                    self.lastCondition = self.jump = parenthesesNode.Evaluate()
                    self.isAConditionLine = False
                    self.conditionsState.append(False)
                    self.insideTheCondition = [True, False]
                    self.isACommandBlockCondition = False
                    weAreOnAIf = False

                movedPositions += m
                mToken.position += m
                if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                    parenthesesNode.setParent(actualNodes[len(actualNodes)-1])
                    actualNodes[len(actualNodes)-1].addChild(parenthesesNode) # filho
                elif (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], BinOp)):
                    parenthesesNode.setParent(actualNodes[len(actualNodes)-1])
                    actualNodes[len(actualNodes)-1].addChild(parenthesesNode) # filho direito
                else:
                    actualNodes.append(parenthesesNode)
                allNodes.append(parenthesesNode)

            elif(mToken.actual.tipo == "close_parentheses"):
                self.parentheses_counter -=1
                if (rerun):
                    break
                else:
                    raise KeyError

            elif (mToken.actual.tipo == "open_brackets"):
                if (myActualVar == "senao"):
                    self.isACommandBlockCondition = True
                    if not self.conditionsState[len(self.conditionsState) - 1]:
                        self.conditionsState[len(self.conditionsState) - 1] = True
                    else:
                        raise KeyError
                    self.flagIfCondition = True
                    self.jump = not self.lastCondition
                    return
                elif (self.flagIfCondition):
                    self.isACommandBlockCondition = True
                elif (mToken.origin.replace(" ", "") == "{"):
                    # Block init
                    return
                else:
                    continue

            elif (mToken.actual.tipo == "close_brackets"):
                if (self.isALoop and not self.flagIfCondition):
                    self.isACommandBlockCondition = True
                    # Re-run condition
                    self.isALoopConditionLine = True
                    newTokens = Tokenizer(origin = self.loopInfo[len(self.loopInfo)-1][0])
                    parenthesesNode, m = self.parseExpression(newTokens, True)
                    self.jumpLoop = parenthesesNode.Evaluate()
                    self.isALoopConditionLine = False
                    if (self.jumpLoop == "false" or self.jumpLoop == 0):
                        del self.loopInfo[len(self.loopInfo)-1]
                        self.isALoop = False
                        return
                    else:
                        self.iter = self.loopInfo[len(self.loopInfo)-1][1]
                        return
                # self.jump = False
                self.flagIfCondition = False
                return

            else:
                continue

        # Fora do loop principal, checa se todos os parenteses foram fechados
        if (self.parentheses_counter != 0 and not rerun):
            raise KeyError

        # Checa se falta algum valor final
        if (len(actual_int) > 0):
            for i in range(len(actual_int)):
                valor_atual += int(actual_int[i])*(10**((len(actual_int) - 1) - i))
            n = IntVal(valor_atual)
            if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                n.setParent(actualNodes[len(actualNodes)-1])
                actualNodes[len(actualNodes)-1].addChild(n) # filho
            elif (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], BinOp)):
                n.setParent(actualNodes[len(actualNodes)-1])
                actualNodes[len(actualNodes)-1].addChild(n) # filho direito
            else:
                
                actualNodes.append(n)
            allNodes.append(n)
            valor_atual, pot = 0, 0
            actual_int = []
        # Checa se falta alguma variável na conta final
        if (len(myActualVar) > 0 and not isATypeDeclaration):
            if ((self.isAConditionLine or self.isALoopConditionLine) and myActualVar in ["true", "false"]):
                last_value = myActualVar
                last_value_tipo = "bool"
            elif (myActualVar in ["true", "false"] and self.symbols.getVariable(self.varEqual.value)[1] == "bool"):
                last_value = myActualVar
                last_value_tipo = self.symbols.getVariable(self.varEqual.value)[1]
            elif (myActualVar in ["true", "false"] and self.symbols.getVariable(self.varEqual.value)[1] == "int"):
                if (myActualVar == "true"):
                    last_value = 1
                else:
                    last_value = 0
                last_value_tipo = self.symbols.getVariable(self.varEqual.value)[1]
            # elif (mToken.origin.count('"') == 2):
            #     print(f"[ANTES DE ADD] actualNodes = '{actualNodes}'")
            #     last_value = myActualVar
            #     last_value_tipo = "palavra"
            else:
                last_value = self.symbols.getVariable(myActualVar)[0].Evaluate()
                last_value_tipo = self.symbols.getVariable(myActualVar)[1]

            if (last_value_tipo == "int"):
                n = IntVal(last_value)
            elif (last_value_tipo == "bool"):
                n = BoolVal(str(last_value))
            elif (last_value_tipo == "palavra"):
                n = StringVal(last_value)

            if (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], UnOp)):
                n.setParent(actualNodes[len(actualNodes)-1])
                actualNodes[len(actualNodes)-1].addChild(n) # filho
            elif (len(actualNodes) > 0 and isinstance(actualNodes[len(actualNodes)-1], BinOp)):
                n.setParent(actualNodes[len(actualNodes)-1])
                actualNodes[len(actualNodes)-1].addChild(n) # filho direito
            else:
                actualNodes.append(n)
            allNodes.append(n)
            myVars.append(n)
            myActualVar = ""
        elif (isATypeDeclaration):
            # print(f"aqui -> '{mToken.origin}'")
            if (myActualVar in self.symbols.symbols):
                raise KeyError(f"A variável '{myActualVar}' já foi inicializada.")
            self.symbols.setVariable(myActualVar, None, myActualType)
            return
        # print("-------------fim------------------")
        # print(f"allNodes = {allNodes}")
        # print(f"actualNodes -> {actualNodes[0]}")
        # print("-------------fim------------------")
        if (len(actualNodes) == 2):
            if (isinstance(actualNodes[0], BinOp)):
                actualNodes[0].addChild(actualNodes[1])
                actualNodes[1].setParent(actualNodes[0])
                del actualNodes[0]
                if (isinstance(actualNodes[0], IntVal) or isinstance(actualNodes[0], BoolVal) or isinstance(actualNodes[0], StringVal)):
                    del actualNodes[0]
            elif (isinstance(actualNodes[0], UnOp)):
                actualNodes[0].addChild(actualNodes[1])
                actualNodes[1].setParent(actualNodes[0])
                del actualNodes[0]
                if (isinstance(actualNodes[0], IntVal) or isinstance(actualNodes[0], BoolVal) or isinstance(actualNodes[0], StringVal)):
                    del actualNodes[0]
        elif (len(actualNodes) > 2):
            while(len(actualNodes) > 2):
                # print(f"actualNodes = {actualNodes}")
                if (isinstance(actualNodes[0], VarChar)):
                    if (isinstance(actualNodes[1], BinOp)):
                        actualNodes[1].addChild(actualNodes[2])
                        actualNodes[2].setParent(actualNodes[1])
                        del actualNodes[1]
                        if (isinstance(actualNodes[0], IntVal) or isinstance(actualNodes[0], BoolVal) or isinstance(actualNodes[0], StringVal)):
                            del actualNodes[1]
                    elif (isinstance(actualNodes[1], UnOp)):
                        actualNodes[1].addChild(actualNodes[2])
                        actualNodes[2].setParent(actualNodes[1])
                        del actualNodes[1]
                        if (isinstance(actualNodes[0], IntVal) or isinstance(actualNodes[0], BoolVal) or isinstance(actualNodes[0], StringVal)):
                            del actualNodes[1]

        # Procurando o patriarca
        if (self.equalFlag and not self.flagInputLn):
            n = allNodes[1]
        elif (rerun and len(allNodes) == 0 and self.flagInputLn):
            x = int(input())
            nx = IntVal(x)
            return (nx, movedPositions)
        elif (isATypeDeclaration):
            # print("")
            pass
        else:
            n = allNodes[0]

        while(n.getParent() != None):
            n = n.getParent()

        if (rerun):
            return (n, movedPositions)
        elif not rerun and self.equalFlag:
            if (len(allNodes[0].children) == 0):
                # print(f"a children = {allNodes[0].children}")
                allNodes[0].addChild(n)
                n.setParent(allNodes[0])
            if (myVars[0].value not in self.reservedWords and myVars[0].value not in self.symbols.symbols):
                # try:
                #     self.symbols.getVariable(myVars[0].value)
                # self.symbols.setVariable(myVars[0].value, allNodes[0])
                
                # self.symbols.updateValue(myVars[0].value, allNodes[0])
                raise KeyError(f"A variável '{myVars[0].value}' não foi inicializada.")
            elif (myVars[0].value not in self.reservedWords and myVars[0].value in self.symbols.symbols):
                # print(type(self.symbols.getVariable(myVars[0].value)))
                # print(f"variavel '{myVars[0].value}' ja existe! Atualizando seu valor para: '{n.Evaluate()}'")
                # contentN = self.symbols.getVariable(myVars[0].value)
                if (isinstance(n, BinOp) or isinstance(n, BinOp)):
                    v = n.Evaluate()
                    if (str(v).isnumeric()):
                        if (self.equalFlag and self.symbols.getVariable(myVars[0].value)[1] == "bool"):
                            n = BoolVal(str(bool(v)).lower())
                        else:
                            n = IntVal(str(v))
                    elif (str(v) in ["True", "False"]):
                        n = BoolVal(str(v).lower())
                # print(f"ContentN = {contentN}")
                var_tipo = self.symbols.getVariable(myVars[0].value)[1]
                if (isinstance(n, IntVal) and var_tipo == "palavra"):
                    raise KeyError(f"A variável '{myVars[0].value}' é do tipo '{var_tipo}' e não 'int'.")
                elif (isinstance(n, BoolVal) and var_tipo == "palavra"):
                    raise KeyError(f"A variável '{myVars[0].value}' é do tipo '{var_tipo}' e não 'bool'.")
                elif (isinstance(n, StringVal) and var_tipo != "palavra"):
                    raise KeyError(f"A variável '{myVars[0].value}' é do tipo '{var_tipo}' e não 'palavra'.")

                if (not self.flagInputLn):                    
                    self.symbols.updateValue(myVars[0].value, n)
            else:
                raise KeyError
            return 1
        else:
            # print(f"[FINAL] b = {self.symbols.getVariable('b').Evaluate()}")
            return n
            
    def run(self, code):
        self.symbols = SymbolTable()
        pre_proc = PrePro()
        code = pre_proc.filter(codelines)

        lines = pre_proc.separateLines(code)
        self.loopInfo = []
        self.iter = 0
        while self.iter < len(lines):
            self.isAConditionLine = False
            self.isALoopConditionLine = False
            self.equalFlag = False
            self.aspasFlag = False
            self.varEqual = None
            self.insideTheCondition = [False, False]
            if (len(lines[self.iter].replace(" ", "")) == 0):
                self.iter += 1
                continue

            if ("enquanto" in lines[self.iter]):
                if (lines[self.iter].count("(") > 1):
                    index = 0
                    counter = 1
                    while (index < len(lines[self.iter])):
                        index = lines[self.iter].find(")", index)
                        if (index < 0):
                            raise KeyError
                        if (counter == lines[self.iter].count(")")):
                            break
                        index += 1
                        counter += 1
                    self.loopInfo.append([lines[self.iter][lines[self.iter].index('(')+1:index], self.iter])
                else:
                    self.loopInfo.append([lines[self.iter][lines[self.iter].index('('):lines[self.iter].index(')')+1], self.iter])
    
            if (self.flagIfCondition and not self.jump):
                # Fazer checagem se condição é one-liner ou multiple-liner
                if (self.isACommandBlockCondition):
                    if ("}" not in lines[self.iter]):
                        self.iter += 1
                        continue
                # else:
                    # print(f"procurando ponto e virgula: {lines[self.iter]}")
                    # if ("")
                # else:
                #     self.jump = False
                #     self.flagIfCondition = False

            self.itIsAPrint = False
            self.flagInputLn = False
            
            tokens = Tokenizer(origin = lines[self.iter])
            self.parseExpression(tokens)
            
            if (self.itIsAPrint):
                if (isinstance(self.symbols.getVariable("imprimir")[0], IntVal)):
                    print(int(self.symbols.getVariable("imprimir")[0].Evaluate()))
                else:
                    print(self.symbols.getVariable("imprimir")[0].Evaluate())
            self.iter += 1
            

if __name__ == '__main__':
    calculadora = Parser()
    filename = sys.argv[1]
    if (filename.endswith(".c")):
        try:
            f = open(filename, "r")
            codelines = f.readlines()
            calculadora.run(codelines)
        except FileNotFoundError:
            raise ValueError(f"O arquivo '{filename}' não foi encontrado")
    else:
        raise ValueError(f"O arquivo '{filename}' passado não possui a extensão '.c'")
