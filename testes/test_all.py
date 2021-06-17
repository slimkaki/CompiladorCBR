import subprocess

# def test_1():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""/*SOLVED*/
#             {println(5*5);
#             println(5/5);
#             println(0/5);
#             println(1/2);
#             println(50*50);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "25\n1\n0\n0\n2500\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_2():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{
#             x1 = 3;
#             y2 = 4;
#             z_final = x1 + y2;
#             println(z_final);
#             }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "7\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_3():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{{x1 = 3; /* bla bla $x1 = 9999998 */
#             y2 = 4;
#             z_final = x1 + y2 *33;
#             println(z_final);}}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "135\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_4():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{/*SOLVED*/
# x1 = 3;
# y2 = 4;
# z_final = (x1 + y2) *33;
# println(z_final);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "231\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_5():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""/*SOLVED*/
# { x1 = 3;
# x1 = x1 +1;
# println(x1);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "4\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_6():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""
#          {
             
             
#              x1 = 3;
# x1 = x1 +1;

#         println(x1);

#     y1 = x1 *100;
#                 println(y1);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "4\n400\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_7():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{/*SOLVED*/
#                 x1 =3;
#                 y2=4;
#                 z_final        = (x1 + y2) *33;
#                 println(z_final);
#                 }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "231\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()


# # def test_8():
# #     # Deveria dar erro
# #     with pytest.raises(KeyError) as e:
# #         p = subprocess.Popen("python3 main.py testes/teste8.c", stdout=subprocess.PIPE, shell=True)
# #         output, err = p.communicate()
# #         print(err)
# #     assert str(e.value.message) == ""

# # def test_9():
# #     # Deveria dar erro
# #     p = subprocess.Popen("python3 main.py testes/teste9.c", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "7\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# def test_10():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{/*SOLVED*/
#                 x_1x = 13;
#                 println(x_1x);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "13\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_11():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{/*SOLVED*/
# x1 = 8;
# y2 = 5;
# z_final = (x1 + y2) * ---37;
# println(z_final);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "-481\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_12():   #ARRUMAR
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{/*SOLVED*/
# x1 = 8;
# y2 = 5;



# z_final = (x1 + y2) * ---37;;;;;
# println(z_final);      }            """)
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "-481\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_13():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{x1 = 3;
# x2 = 4;
# z_final = x1 + x2 * -3;
# println(z_final);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "-9\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# # def test_14():
# #     # Deveria dar erro
# #     p = subprocess.Popen("python3 main.py testes/teste14.c", stdout=subprocess.PIPE, shell=True)
# #     output, err = p.communicate()
# #     expected = "-9\n"
# #     print("Expected output:", expected)
# #     assert output == expected.encode()

# def test_15():
#     with open("testes/inputs/actual_in.txt", "w") as f:
#         f.write("""12""")
#         f.close()
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{a = 15;
# b = 16;
# println(12+b);
# x = readln();
# println(x);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c < testes/inputs/actual_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "28\n12\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_16():
#     with open("testes/inputs/actual_in.txt", "w") as f:
#         f.write("""4
# 5""")
#         f.close()
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{x = readln();
# y = 2 + readln() + 3;
# println(x);
# println(y);
# println((x+y));}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c < testes/inputs/actual_in.txt", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "4\n10\n14\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_17():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{x = 15;
# /*Teste lesser*/
# if (x < 3) {
#     /*Não deveria printar*/
#     println(1);
# }
# if (x < 15) {
#     /*Não deveria printar*/
#     println(2);
# }
# if (x < 16) {
#     /*Deveria printar*/
#     println(3);
# }

# /*Teste greater*/
# if (x > 3) {
#     /*Deveria printar*/
#     println(4);
# }

# if (x > 15) {
#     /*Não deveria printar*/
#     println(5);
# }

# if (x > 16) {
#     /*Não deveria printar*/
#     println(6);
# }

# /*Teste equals*/
# if (x == 3) {
#     /*Não deveria printar*/
#     println(7);
# }
# if (x == 15) {
#     /*Deveria printar*/
#     println(8);
# }

# if (x == 16) {
#     /*Não deveria printar*/
#     println(9);
# }}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "3\n4\n8\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_18():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{13+4;
# println(((12)+13*---5/2));
# if (12 > 3) {
#     println(1);
#     println(2);
#     println(3);
#     println(4);
#     println(5);
#     println(6);
# }

# println(7);
# println(8);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "-20\n1\n2\n3\n4\n5\n6\n7\n8\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_19(): #ARRUMAR
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{
#     println(1); /*Deveria printar 1*/
#     if (3 == 3/1) {
#         /*Deveria printar 2*/
#         println(2);
#     } else {
#         /*Não deveria printar 3*/
#         println(3);
#     }
#     println(4); /*Deveria printar 4*/

#     if (3 == 3/2) {
#         /*Não deveria printar 5*/
#         println(5);
#     } else {
#         /*Deveria printar 6*/
#         println(6);
#     }

#     println(7); /*Deveria printar 7*/
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n2\n4\n6\n7\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_20(): #arrumar
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{
#     println(1);
#     if (3 > 5) {
#         println(2);
#     } else if (3 < 2) {
#         println(3);
#     } else {
#         println(4);
#     }
#     println(5);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n4\n5\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_21():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{i = 1;
# while(i < 5) {
#     println(i);
#     i = i + 1;
# }
# println(6);}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "1\n2\n3\n4\n6\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()


# def test_22():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{
#     x = 1;
#     y = 2;
#     println(x+y); /*Deveria printar 3*/
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "3\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_23():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{if (3 < 5){
#     if (4 == 4) {
#         println(2);
#     }
#     println(5);
# }}""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "2\n5\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_24():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{
#     x = 12+(3*76)/(4);
#     println(x);
# }""")
#         f.close()
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "60\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()

# def test_25():
#     with open("testes/actual_test.c", "w") as f:
#         f.write("""{
#     i = 5;
#     j = 0;
#     while (  i == 5) {
#         println(i);
#         if (j < 2) {
#             j = j + 1;
#         } else {
#             i = i - 1;
#         }
#     }
#     println(10);
#     println(i);
# } 
# """)
#         f.close()   
#     p = subprocess.Popen("python3 main.py testes/actual_test.c", stdout=subprocess.PIPE, shell=True)
#     output, err = p.communicate()
#     expected = "5\n5\n5\n10\n4\n"
#     print("Expected output:", expected)
#     assert output == expected.encode()