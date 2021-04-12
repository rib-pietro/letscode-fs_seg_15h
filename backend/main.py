from bottle import *
# from bottle import run, route
# import bottle
# import bottle as bt

@route('/')
def index():
    return f"<h1>Hello, World!</h1>"

# rotas dinâmicas
@route('/<nome>/<saudacao>')
def hello(nome, saudacao):
    return f"<h1>{saudacao}, {nome}!"

run()