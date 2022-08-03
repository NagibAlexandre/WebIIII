from flask import Flask, render_template, request


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('God of War', 'Ação', 'Playstation')
jogo2 = Jogo('CS:GO', 'Tiro', 'Computador')
jogo3 = Jogo('Minecraft', 'Construção', 'Computador')

lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def ola():
    return render_template('lista.html', titulo=' -/- Meus Jogos -/-', jogos=lista)

@app.route('/teste')
def pag1():
    return render_template('teste.html')

@app.route('/novo')
def pag2():
    return render_template('novo.html')

@app.route('/criar', methods=["post",])
def pag3():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome,categoria,console)
  lista.append(jogo)
  return render_template('lista.html', titulo = 'Jogos', jogos = lista)
# Esse código é para quando for rodar no Replit
#app.run(host='0.0.0.0', debug=True)

# Esse código é para quando for rodar em sua máquina
app.run(debug=True)
