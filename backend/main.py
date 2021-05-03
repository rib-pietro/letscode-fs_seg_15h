from bottle import *

tarefas = [
    'Molhar as plantas',
    'Limpar o cocô'
]

posts = [
    {
        'url': 'beneficios-do-sono',
        'titulo': 'Benefícios do sono',
        'conteudo': 'Sono faz seu corpo relaxar, você consegue pensar mais facilmente nas dúvidas.',
        'views': 0,
    },
    {
        'url': 'netflix',
        'titulo': 'Netflix',
        'conteudo': 'Netflix é bom!!!',
        'views': 0,
    },
    {
        'url': 'passaros',
        'titulo': 'Pássaros',
        'conteudo': 'Pássaros são ajudados pelo Luis, voam e fazem cocô na nossa cabeça',
        'views': 0,
    },
    {
        'url': 'flamengo',
        'titulo': 'Flamengo',
        'conteudo': 'Maior da américa',
        'views': 0,
    }
]

@route('/')
def index():

    links_html = ''

    for post in posts:
        links_html += f'''
        <li>
            <a href="http://localhost:8080/posts/{post["url"]}">{post["titulo"]}</a>
        </li>
        '''

    return f"""<h1>Blog da turma de Full Stack!</h1>
    <h2> Posts: </h2>
    <ul>
        {links_html}
    </ul>
    """

@route('/posts/cadastrar')
def formulario_post():
    return """
    <form method="POST" action="/posts/cadastrar">
        <div>
            <label for="titulo">Título: </label>
            <input type="text" name="titulo" id="titulo" />
        </div>
        <div>
            <label for="url">URL: </label>
            <input type="text" name="url" id="url" />
        </div>
        <div>
            <label for="conteudo">Conteúdo: </label>
            <textarea name="conteudo" id="conteudo"></textarea>
        </div>
        <button type="submit">Cadastrar post</button>
    </form>
    """

@route('/posts/cadastrar', method='POST')
def cadastrar_post():
    info_post = request.forms
    novo_post = {}
    novo_post['url'] = info_post['url']
    novo_post['titulo'] = info_post['titulo']
    novo_post['conteudo'] = info_post['conteudo']
    novo_post['views'] = 0

    posts.append(novo_post)

    redirect('/posts/cadastrar')
    # return "Post cadastrado! <a href='/'>Voltar para Home</a>"
    

# rotas dinâmicas

@route('/posts/<url_post>')
def get_post(url_post):
    post_encontrado = None

    for i in range(len(posts)):
        if posts[i]['url'] == url_post:
            posts[i]['views'] += 1
            post_encontrado = posts[i]
    
    if post_encontrado == None:
        return "Post não encontrado!"

    return f"""
    <h1>{post_encontrado['titulo']}</h1>
    <p>Visualizações: {post_encontrado['views']}</p>
    <p>{post_encontrado['conteudo']}</p>
    """

run()