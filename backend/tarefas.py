from bottle import *

tarefas = [] # lista de strings

@route('/tarefas/cadastrar') # MÉTODO 'GET'
def formulario_tarefa():

    return template('formulario_tarefa', tarefas=tarefas)

    # return f"""
    # <form action="/tarefas/cadastrar" method="POST">
    #     <div>
    #         <label for="tarefa">Nova tarefa: </label>
    #         <input type="text" id="tarefa" name="tarefa" />
    #     </div>
    #     <button type="submit">Adicionar</button>
    # </form>
    # {', '.join(tarefas)}
    # """

@route('/tarefas/cadastrar', method='POST')
def cadastrar_tarefa():
    infos = request.forms
    nova_tarefa = infos['tarefa']
    tarefas.append(nova_tarefa)

    redirect('/tarefas/cadastrar')

run()