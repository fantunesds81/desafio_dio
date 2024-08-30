# coding: utf-8
# author: fantunes

def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e))# instancia da exceção
        print(e.args)# argumentos as mensagem
        print(e)# __str__ mensagem
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except(TypeError, NameError):
        print("NameError ocorreu ou então, NameError")


# TypeError
erro("int+int")
# NameError
erro("a")
# ValueError
erro("int('a')")
# ZeroDivisionError
erro("5/0")