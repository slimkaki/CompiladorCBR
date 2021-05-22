import subprocess

def test_1():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int x;
    x = 10;
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "10\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_2():
    # Deveria apontar KeyError
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    x=10;
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    print(err.decode())
    assert "raise KeyError" in err.decode()
    # assert "Faltou um ';'" in err.decode()

def test_3():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    palavra minhapalavra;
    minhapalavra = "abacate";
    imprimir(minhapalavra);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "abacate\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_4():
    # Deveria apontar KeyError
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int x;
    x = 10;
    bool x;
    x = false;
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    print(err.decode())
    assert "raise KeyError" in err.decode()

def test_5():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int x;
    x = 1;
    bool y;
    y = x + true;
    imprimir(y);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n" # Não deveria ser '2'?
    print("Expected output:", expected)
    assert output == expected.encode()

def test_6():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    bool x;
    x = false;
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "0\n" # Não deveria ser 'false'?
    print("Expected output:", expected)
    assert output == expected.encode()    

def test_7():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    bool x;
    x = 2 == 2;
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n" # não deveria ser 'true'?
    print("Expected output:", expected)
    assert output == expected.encode()

def test_8():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
            int x;
bool y;
palavra z;
x = 1;
y = x || true;
z = "x:";
imprimir(x + y);
imprimir(z);
        }""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "2\nx:\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_9():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
            int x;
bool y;
palavra z;
x = 1;
y = x || true;
z = "x:";
imprimir(x + y);
imprimir(z);
imprimir(x + z); /* ERROR */
        }""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "\n"
    print("Expected output:", expected)
    assert "raise KeyError" in err.decode()

def test_10():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{

    imprimir(5*5);
    imprimir(5/5);
    imprimir(0/5);
    imprimir(1/2);
    imprimir(50*50);
        }""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "25\n1\n0\n0\n2500\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_11():
    with open("testes/inputs/actual_in.txt", "w") as f:
        f.write("42\n")
        f.close()

    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int x;
    x = entrada();
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/actual_in.txt", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "42\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_12():
    with open("testes/inputs/actual_in.txt", "w") as f:
        f.write("2\n8\n")
        f.close()
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int x;
    x = entrada();
    x = entrada();
    imprimir(x);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/actual_in.txt", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "8\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_13():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
  int x;
  x = true;
  se (x){
    imprimir(42);
  }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "42\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_14():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int a;
    a = 0;
    enquanto (a < 3){
        a = a +1;
        imprimir(a);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n2\n3\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_15():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int a;
    a = 1;
    enquanto (a < 3){
        a = a +1;
        imprimir(a);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "2\n3\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_16():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
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
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n2\n3\n4\n5\n5\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_17():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
  bool x;
  x = true;
  se (x){
    imprimir(42);
  }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "42\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_18():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{   
    se (((true) || (true) || (true)) || ((false) && (false) && (false))){
        imprimir(42);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "42\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_19():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    bool a;
    bool b;
    bool c;
    bool d;
    bool e;
    bool f;
    a = true;
    b = true;
    c = true;
    d = false;
    e = true;
    f = true;
    se (((a) || (b) || (c)) || ((d) && (e) && (f))){
        imprimir(42);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "42\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_20():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    int y;
    y = true+1;
    imprimir(y);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "2\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_21():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    bool x;
    int y;
    x = false+1;
    y = x;
    imprimir(y);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_22():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
  se(2){
    imprimir(42);
  }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "42\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_23():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
  se(2 || false){
    imprimir(42);
  }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "42\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_24():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    palavra msg;
    msg = "oi";
    se (msg == "oi") {
        imprimir("sim");
    } senao {
        imprimir("nao");
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "sim\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_25():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    se (true || false){
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_26():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    se (true && (1==1)){
        imprimir(1);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_27():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    se (true && (!(1==1))){
        imprimir(1);
    }
    senao{
        imprimir(2);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "2\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_28():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    palavra msg;
    msg = "tchau";
    se (msg == "oi") {
        imprimir("sim");
    } senao {
        imprimir("nao");
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "nao\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_29():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    bool a;
    int b;
    int c;
    
    b = 789;
    c = 689;

    a = (b && c) + 1;
    c = a;
    
    imprimir(c);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_30():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    bool a;
    int b;
    int c;
    
    b = 789;
    c = 689;

    a = (b && c) + 1;
    c = a + 1;
    
    imprimir(c);
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "2\n"
    print("Expected output:", expected)
    assert output == expected.encode()

def test_31():
    with open("testes/issues_test.c", "w") as f:
        f.write("""{
    bool a;
    int b;
    int c;
    
    b = 32;
    c = 32;
    a = true;

    se ((b && c) == a) {
    	imprimir(1);
    }senao{
    	imprimir(2);
    }
}""")
        f.close()
    p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    expected = "1\n"
    print("Expected output:", expected)
    assert output == expected.encode()
# def test_26():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     se (! (1==0)) {
#         imprimir(1);
#     }
#     senao{
#         imprimir(0);
#     }
# }
# """)
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_27():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     se (! (((1>0) || (1==0)) && (0==9))){
#         imprimir(1);
#     }
# }
# """)
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_30(): # Loop infinito - Arrumar
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{   
#     a = 0;
#     b = 1;
#     enquanto ((a < 99999) && (b ==1)){
#         a = a +1;
#         imprimir(a);
#         se (a == 5){
#             b = 0;
#         }
#     }
#     imprimir(a);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n2\n3\n4\n5\n5\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_34(): # -> Ainda tá dando erro, arrumar
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{   
#     se (-5 < 4){
#         imprimir(1);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_35():
#     with open("testes/inputs/issues_in.txt", "w") as f:
#         f.write("2\n")
#         f.close()
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     x = entrada();
#     imprimir(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_36():
#     with open("testes/inputs/issues_in.txt", "w") as f:
#         f.write("2\n3\n")
#         f.close()
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     x = entrada();
#     x = entrada();
#     imprimir(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "3\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_37():
#     with open("testes/inputs/issues_in.txt", "w") as f:
#         f.write("2\n")
#         f.close()
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     x = entrada();
#     y = x*2;
#     imprimir(y);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "4\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_38():
#     with open("testes/inputs/issues_in.txt", "w") as f:
#         f.write("2\n3\n")
#         f.close()
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     x = entrada();
#     y = entrada();
#     imprimir(x+y);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "5\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_43():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     se (0 >1)
#         imprimir(1);
#     imprimir(0);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "0\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()