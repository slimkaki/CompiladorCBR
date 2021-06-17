# import subprocess

# def test_1():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int x;
#     x = 10;
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "10\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_2():
#     # Deveria apontar KeyError
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     x=10;
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     print(err.decode())
#     assert "raise KeyError" in err.decode()
#     # assert "Faltou um ';'" in err.decode()

# def test_3():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     string minhaString;
#     minhaString = "abacate";
#     println(minhaString);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "abacate\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_4():
#     # Deveria apontar KeyError
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int x;
#     x = 10;
#     bool x;
#     x = false;
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     print(err.decode())
#     assert "raise KeyError" in err.decode()

# def test_5():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int x;
#     x = 1;
#     bool y;
#     y = x + true;
#     println(y);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_6():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     bool x;
#     x = false;
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "false\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()    

# def test_7():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     bool x;
#     x = 2 == 2;
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "true\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_8():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#             int x;
# bool y;
# string z;
# x = 1;
# y = x || true;
# z = "x:";
# println(x + y);
# println(z);
#         }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\nx:\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_9():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#             int x;
# bool y;
# string z;
# x = 1;
# y = x || true;
# z = "x:";
# println(x + y);
# println(z);
# println(x + z); /* ERROR */
#         }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "\n"
#     print("Expected output:", expected)
#     assert "raise KeyError" in err.decode()

# def test_10():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{

#     println(5*5);
#     println(5/5);
#     println(0/5);
#     println(1/2);
#     println(50*50);
#         }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "25\n1\n0\n0\n2500\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_11():
#     with open("testes/inputs/actual_in.txt", "w") as f:
#         f.write("42\n")
#         f.close()

#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int x;
#     x = readln();
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/actual_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "42\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_12():
#     with open("testes/inputs/actual_in.txt", "w") as f:
#         f.write("2\n8\n")
#         f.close()
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int x;
#     x = readln();
#     x = readln();
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/actual_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "8\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_13():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#   int x;
#   x = true;
#   if (x){
#     println(42);
#   }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "42\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_14():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int a;
#     a = 0;
#     while (a < 3){
#         a = a +1;
#         println(a);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n2\n3\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_15():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int a;
#     a = 1;
#     while (a < 3){
#         a = a +1;
#         println(a);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\n3\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_16():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int a;
#     int b;
#     a = 0;
#     b = 1;
#     while ((a < 99999) && (b ==1)){
#         a = a +1;
#         println(a);
#         if (a == 5){
#             b = 0;
#         }
#     }
#     println(a);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n2\n3\n4\n5\n5\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_17():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#   bool x;
#   x = true;
#   if (x){
#     println(42);
#   }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "42\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_18():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{   
#     if (((true) || (true) || (true)) || ((false) && (false) && (false))){
#         println(42);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "42\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_19():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     bool a;
#     bool b;
#     bool c;
#     bool d;
#     bool e;
#     bool f;
#     a = true;
#     b = true;
#     c = true;
#     d = false;
#     e = true;
#     f = true;
#     if (((a) || (b) || (c)) || ((d) && (e) && (f))){
#         println(42);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "42\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_20():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     int y;
#     y = true+1;
#     println(y);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_21():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     bool x;
#     int y;
#     x = false+1;
#     y = x;
#     println(y);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_22():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#   if(2){
#     println(42);
#   }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "42\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_23():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#   if(2 || false){
#     println(42);
#   }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "42\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_24():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     string msg;
#     msg = "oi";
#     if (msg == "oi") {
#         println("sim");
#     } else {
#         println("nao");
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "sim\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_25():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     if (true || false){
#         println(1);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_26():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     if (true && (1==1)){
#         println(1);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_27():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     if (true && (!(1==1))){
#         println(1);
#     }
#     else{
#         println(2);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_28():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     string msg;
#     msg = "tchau";
#     if (msg == "oi") {
#         println("sim");
#     } else {
#         println("nao");
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "nao\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_29():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     bool a;
#     int b;
#     int c;
    
#     b = 789;
#     c = 689;

#     a = (b && c) + 1;
#     c = a;
    
#     println(c);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_30():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     bool a;
#     int b;
#     int c;
    
#     b = 789;
#     c = 689;

#     a = (b && c) + 1;
#     c = a + 1;
    
#     println(c);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_31():
#     with open("testes/issues_test.c", "w") as f:
#         f.write("""{
#     bool a;
#     int b;
#     int c;
    
#     b = 32;
#     c = 32;
#     a = true;

#     if ((b && c) == a) {
#     	println(1);
#     }else{
#     	println(2);
#     }
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()
# # def test_26():
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{
# #     if (! (1==0)) {
# #         println(1);
# #     }
# #     else{
# #         println(0);
# #     }
# # }
# # """)
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "1\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_27():
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{
# #     if (! (((1>0) || (1==0)) && (0==9))){
# #         println(1);
# #     }
# # }
# # """)
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "1\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_30(): # Loop infinito - Arrumar
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{   
# #     a = 0;
# #     b = 1;
# #     while ((a < 99999) && (b ==1)){
# #         a = a +1;
# #         println(a);
# #         if (a == 5){
# #             b = 0;
# #         }
# #     }
# #     println(a);
# # }""")
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "1\n2\n3\n4\n5\n5\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_34(): # -> Ainda tá dando erro, arrumar
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{   
# #     if (-5 < 4){
# #         println(1);
# #     }
# # }""")
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "1\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_35():
# #     with open("testes/inputs/issues_in.txt", "w") as f:
# #         f.write("2\n")
# #         f.close()
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{
# #     x = readln();
# #     println(x);
# # }""")
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "2\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_36():
# #     with open("testes/inputs/issues_in.txt", "w") as f:
# #         f.write("2\n3\n")
# #         f.close()
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{
# #     x = readln();
# #     x = readln();
# #     println(x);
# # }""")
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "3\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_37():
# #     with open("testes/inputs/issues_in.txt", "w") as f:
# #         f.write("2\n")
# #         f.close()
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{
# #     x = readln();
# #     y = x*2;
# #     println(y);
# # }""")
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "4\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_38():
# #     with open("testes/inputs/issues_in.txt", "w") as f:
# #         f.write("2\n3\n")
# #         f.close()
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{
# #     x = readln();
# #     y = readln();
# #     println(x+y);
# # }""")
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c < testes/inputs/issues_in.txt", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "5\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# # def test_43():
# #     with open("testes/issues_test.c", "w") as f:
# #         f.write("""{
# #     if (0 >1)
# #         println(1);
# #     println(0);
# # }""")
# #         f.close()
# #     p = subprocess.Popen("python3 main.py testes/issues_test.c", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "0\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()