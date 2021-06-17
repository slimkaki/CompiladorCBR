class Node:
    """
    Classe abstrata ou interface.
    Modelo para as classes a seguir
    """
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def Evaluate(self):
        raise NotImplementedError

class BinOp(Node):
    """
    Binary Operation
    """
    def Evaluate(self):
        """
        Override da função da classe node(
        Deve fazer a operação de seus dois filhos
        """
        if (len(self.children) < 2):
            raise NoChildException(f"Nó BinOp de valor '{self.value}' possui {len(self.children)} filho(s)")
        a = self.children[0].Evaluate()
        b = self.children[1].Evaluate()

        if (isinstance(a, str)):
            if (a in ["True", "False", "verdadeiro", "falso"]):
                a = str(a).lower() == "verdadeiro"
            elif (a.isnumeric()):
                a = int(a)
        if(isinstance(b, str)):
            if (b in ["True", "False", "verdadeiro", "falso"]):
                b = str(b).lower() == "verdadeiro"
            elif (b.isnumeric()):
                b = int(b)

        if (self.value == "+"):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a+b)
        elif (self.value == "-"):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a-b)
        elif (self.value == "*"):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a*b)
        elif (self.value == "/"):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a/b)
        elif (self.value == ">"):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a>b)
        elif (self.value == "<"):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a<b)
        elif (self.value == "=="):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a==b)
        elif (self.value == ">="):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a>=b)
        elif (self.value == "<="):
            if ((isinstance(a, int) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, int)) or 
                (isinstance(a, bool) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, bool))):
                raise KeyError(f"Não é possível realizar a operação de '{self.value}' entre '{a}' e '{b}'")
            return (a<=b)
        elif (self.value == "!="):
            return (a!=b)
        elif (self.value == "||"):
            return bool(a or b)
        elif (self.value == "&&"):
            return bool(a and b)
        else:
            raise UnknownOperation(f"Não foi possível identificar o que '{a} {self.value} {b}' significa.")

    def addChild(self, filho):
        """
        Só pode ter até 2 filhos
        """
        if (len(self.children) >= 2):
            raise FullNodeException(f"O nó '{self.value}' já possui 2 filhos")
        self.children.append(filho)
    
    def getLeftChild(self):
        return self.children[0]

    def getRightChild(self):
        return self.children[1]

    def getAllChild(self):
        return self.children
    
    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent

class UnOp(Node):
    """
    Unary Operation
    """
    def Evaluate(self):
        """
        Override da função da classe node
        """
        if (len(self.children) < 1):
            raise NoChildException(f"O nó '{self.value}' não possui filhos ainda")
        
        a = self.children[0].Evaluate()
        if (self.value == "+"):
            return a
        elif (self.value == "-"):
            return -a
        elif (self.value == "!"):
            if (isinstance(a, int) and a in [0, 1]):
                return (not a)
            elif (a == "verdadeiro"):
                return "falso"
            elif (a == "falso"):
                return "verdadeiro"
            raise KeyError(f"O valor '{a}' não é 0 ou 1")
            

    def addChild(self, filho):
        """
        Só pode ter até 1 filho
        """
        if (len(self.children) >= 1):
            raise FullNodeException(f"O nó '{self.value}'' já possui 1 filho")
        self.children.append(filho)
    
    def getChild(self):
        return self.children[0]

    def getAllChild(self):
        return self.children

    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent

class VarChar(Node):
    def Evaluate(self):
        """
        Override da função da classe node
        """
        return self.children[0].Evaluate()

    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent

    def addChild(self, Node):
        if (len(self.children) >= 1):
            raise FullNodeException(f"O nó '{self.value}' já possui 1 filho")
        self.children.append(Node)

    def getChild(self):
        return self.children[0]

    def getAllChild(self):
        return self.children
    
    def updateChild(self, newNode):
        del self.children[0]
        self.addChild(newNode)

    
class InstructionBlock(Node):
    """
    Instruction Operation
    """
    def Evaluate(self):
        """
        TODO: Override da função da classe node
        """
        return self.children[0].Evaluate()
        

    def addChild(self, filho):
        if (len(self.children) >= 1):
            raise FullNodeException(f"O nó '{self.value}' já possui 1 filho")
        self.children.append(filho)

    def getChild(self):
        return self.children[0]

    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent

class IntVal(Node):
    """
    Integer value
    """
    def Evaluate(self):
        """
        Override da função da classe node
        """
        return int(self.value)

    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent

class BoolVal(Node):
    def Evaluate(self):
        """
        Override da função da classe node
        """
        return str(self.value).lower() == "verdadeiro"
        
    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent

    def addChild(self, Node):
        if (len(self.children) >= 1):
            raise FullNodeException(f"O nó '{self.value}' já possui 1 filho")
        self.children.append(Node)

    def getChild(self):
        return self.children[0]

    def getAllChild(self):
        return self.children
    
    def updateChild(self, newNode):
        del self.children[0]
        self.addChild(newNode)

class StringVal(Node):
    def Evaluate(self):
        """
        Override da função da classe node
        """
        return self.value

    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent

    def addChild(self, Node):
        if (len(self.children) >= 1):
            raise FullNodeException(f"O nó '{self.value}' já possui 1 filho")
        self.children.append(Node)

    def getChild(self):
        return self.children[0]

    def getAllChild(self):
        return self.children
    
    def updateChild(self, newNode):
        del self.children[0]
        self.addChild(newNode)

class NoOp(Node):
    """
    No operation (Dummy)
    """
    def Evaluate(self):
        """
        Override da função da classe node
        """
        return
    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent
    

class FullNodeException(Exception):
    """
    Classe para exception
    """
    def __init__(self, message):
        self.message = message
    def __string__(self):
        return self.message

class NoChildException(Exception):
    """
    Classe para exceptions
    """
    def __init__(self, message):
        self.message = message
    def __string__(self):
        return self.message      

class UnknownOperation(Exception):
    """
    Classe para exceptions
    """
    def __init__(self, message):
        self.message = message
    def __string__(self):
        return self.message

# if __name__ == '__main__':
#     n1 = InstructionBlock("while")
#     n2 = BinOp(">")
#     n1.addChild(n2)
#     n2.setParent(n1)

#     n3 = VarChar("x")
#     n4 = IntVal(1)
#     n3.addChild(n4)
#     n4.setParent(n3)
#     n2.addChild(n3)
#     n3.setParent(n2)

#     n5 = IntVal(5)
#     n2.addChild(n5)
#     n5.setParent(n2)

#     print(n1.Evaluate())

#     n6 = VarChar("x")
#     n7 = IntVal(2)


