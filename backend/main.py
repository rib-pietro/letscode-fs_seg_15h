from bottle import *

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