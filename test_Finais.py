import subprocess

def test_3():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal(){int x1;
    x1 = 3;
    int y2;
    y2 = 4;
    int z_final;
    z_final = x1 + y2;
    imprimir(z_final);}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "7\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_19():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal(){
    int x1;
    int y2;
    int z_final;
    x1 = 8;
    y2 = 5;
    z_final = (x1 + y2) * ---37;
    imprimir(z_final);}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "-481\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_22():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    se ((1==1) || (1==0)){
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_23():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    int f;
    f = 5;
    se (f == 5){
        imprimir(f);
    }
}
""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "5\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_24():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    se ((1==1) && (1==0)){
        imprimir(0);
    }
    senao{
        imprimir(1);
    }
}
""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_25():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    se ((1<2) || (0>2)){
        imprimir(1);
    }
    senao{
        imprimir(0);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_26():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    se (! (1==0)) {
        imprimir(1);
    }
    senao{
        imprimir(0);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_27():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    se (! (((1>0) || (1==0)) && (0==9))){
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_28():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    int a;
    a = 0;
    enquanto (a < 3){
        a = a +1;
        imprimir(a);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n2\n3\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_29():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    int a;
    a = 1;
    enquanto (a < 3){
        a = a +1;
        imprimir(a);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "2\n3\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_30():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    int a;
    int b;
    a = 0;
    b = 1;
    enquanto ((a < 99999) && (b ==1)){
        a = a +1;
        imprimir(a);
        se (a == 5){
            b = 0;
        }
    }
    imprimir(a);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n2\n3\n4\n5\n5\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_33():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{   
    se (((1==1) || (1==1) || (1==1)) || ((1==0) && (1==0) && (1==0))){
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_34():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{   
    se (-5 < 4){
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_39():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    imprimir(1);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_40():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{

    se (10 < 20) {
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_41():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    
    se (30 < 20) {
    imprimir(0);
    }
    senao{
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_43():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int principal()
{
    se (0 >1)
        imprimir(1);
    imprimir(0);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "0\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_75():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Ok, pode nao ter retornar*/
int exibe(){
    int x;
    x = 5;
    imprimir(x);
}

int principal(){
    exibe();
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "5\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_76():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Passagem parametro*/
int exibe(int x){
    imprimir(x);
}

int principal(){
    exibe(8);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "8\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_81():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Ok: Dois parametros*/
int exibe(int x, int y){
    imprimir(x*y);
}


int principal(){
    exibe(5, 3);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "15\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_82():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Ok: Dois parametros*/
int exibe(int x, int y){
    int z;
    z = x*y;
    imprimir(z);
}


int principal(){
    exibe(5, 3);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "15\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_83():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Ok: Tres parametros*/
int exibe(int x, int y, int z){
    imprimir(x+y+z);
}


int principal(){
    exibe(2, 3, 4);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "9\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_85():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Ok: retornar orexp*/
int soma(int x, int y){
    retornar x + y;
}


int principal(){
    int x;
    x = soma(2,3);
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "5\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_89():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int qualquer(){
    int x;
    x = 8;
    retornar x;
}


int principal(){
    int x;
    x = 3;
    imprimir(x);
    int y;
    y = qualquer();
    imprimir(y);
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "3\n8\n3\n"
    print("Expected output:", expected)
    assert output == expected.encode()

# def test_90():
#     with open("testes/issues_test.cbr", "w") as f:
#         f.write("""int qualquer(){
#     int x;
#     x = 8;
#     retornar x;
# }

# /*Erro: ja foi declarada funcao com este identseicador*/
# int qualquer(){
#     int x;
#     x = 10;
#     retornar x;
# }


# int principal(){
#     int y;
#     y = qualquer();
#     imprimir(y);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 principal.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     print(err.decode())
#     assert "KeyError" in err.decode()

def test_92():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Ok: para eval quando encontra retornar*/

int qualquer(){
    int x;
    x = 10;
    
    imprimir(x);    
    retornar x;
    
    imprimir(x*2);
}


int principal(){
    int y;
    y = qualquer();
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "10\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_93():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""/*Ok*/

int soma(int x, int y)
{
    int res;
    res = x + y;
    retornar res;    
}

bool comparaSoma()
{
    bool res;
    int x;
    x = 3;
    
    res = soma(x,2) == 8;
    
    retornar res;
}


int principal()
{
    int x;
    bool z;
    
    z = comparaSoma();
    x = z;
    imprimir(x);
    
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "0\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_95():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int soma(int x, int y)
{
    int res;
    res = x + y;
    retornar res;    
}

int principal()
{
    int x;
    soma(3,5);/*Ok fazer isso*/
    x = soma(3,5);
    imprimir(x);
    
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "8\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_97():
    with open("testes/issues_test.cbr", "w") as f:
        f.write("""int serie(int x)
{
    se (x == 1) {
        retornar x;
    }senao{
    	retornar x + serie(x-1);
    }
    
}

int principal()
{
    int x;
    x = 5;
    imprimir(serie(x));
    
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.cbr", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "15\n"
    print("Expected output:", expected)
    assert output == expected.encode()