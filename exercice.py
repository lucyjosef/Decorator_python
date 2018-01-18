#!/home/apprenant/PycharmProject/Decorateur/venv/bin/python

from functools import wraps

# to please th teacher
import this
print(this)


def simple_decorator(func):
    """
    simple_decorator content in here
    """
    def sdeco(*args):
        print("\n")
        print("I'm a simple decorator !")
        try:
            args
        except NameError as err:
            print("Erreur : ", err)
        func(*args)
        print("I'm also from single decorator but a execute myself after function")
    return sdeco


@simple_decorator
def say_hello():
    print("hello")


@simple_decorator
def say_something(something):
    print(something)


def argument_decorator(*expected_args):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args):
            print("\n")
            print("omg je suis argument decoration !")
            print(expected_args)
            return func(*args)
        return wrapper
    return my_decorator


@argument_decorator("Je suis en arg", "Moi aussi !", "copieurs...", "a l'infini", "tp torché à 14:40", "je vais avoir le temps", "de mettre autant d'arg", "que je veux", "et meme des int ! ", "regarde :", 1255, "lol", "ouais ouais ouais", "titatitatou..", True)
def say_blah():
    print("blah")


@argument_decorator("Bah moi je suis arg 2 ;)")
def say_blah_and_something():
    print("BLAH and something")


say_hello()
say_something("GLOUBI")
say_blah()
say_blah_and_something()

