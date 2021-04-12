from bottle import *

posts = [
    {
        'url': 'beneficios-do-sono',
        'titulo': 'Benefícios do sono',
        'conteudo': 'Sono faz seu corpo relaxar, você consegue pensar mais facilmente nas dúvidas.'
    },
    {
        'url': 'netflix',
        'titulo': 'Netflix',
        'conteudo': 'Netflix é bom!!!'
    },
    {
        'url': 'passaros',
        'titulo': 'Pássaros',
        'conteudo': 'Pássaros são ajudados pelo Luis, voam e fazem cocô na nossa cabeça'
    }
]

@route('/')
def index():

    links_html = ''

    for post in posts:
        links_html += f'''
        <li>
            <a href="http://localhost:8080/posts/{url_post}">{post_title}</a>
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

    for post in posts:
        if post['url'] == url_post:
            post_encontrado = post
    
    return f"""
    <h1>{post_encontrado['titulo']}</h1>

    <p>{post_encontrado['conteudo']}</p>
    """

run()