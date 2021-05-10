<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> <!-- Define o conjunto de caractes -->
    <title>TO-DO List</title>
</head>
<body>
    <form action="/tarefas/cadastrar" method="POST">
        <div>
            <label for="tarefa">Nova tarefa: </label>
            <input type="text" id="tarefa" name="tarefa" />
        </div>
        <button type="submit">Adicionar</button>
    </form>
    <ul>
        % for tarefa in tarefas:
        <li>{{ tarefa }}</li>
        % end
    </ul>
</body>
</html>