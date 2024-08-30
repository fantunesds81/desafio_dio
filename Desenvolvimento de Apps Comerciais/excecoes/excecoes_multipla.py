# coding: utf-8
# author: fantunes

def erro(x):
    try:
        eval(x)
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionErro")


# TypeError
erro("int+int")
# NameError
erro("a")
# ValueError
erro("int('a')")
# ZeroDivisionError
erro("5/0")