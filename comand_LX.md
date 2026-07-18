# 📘 Guia Completo: Comandos Linux Essenciais para Programadores

Perfeito! Vou adicionar uma seção completa sobre os comandos Linux mais usados, já que você vai precisar deles para navegar, organizar seus projetos e trabalhar com Git.

---

## 🐧 Fundamentos: O Terminal Linux

O terminal segue uma estrutura simples:

```bash
comando [flags] [argumentos]
```

**Exemplo:**
```bash
ls -la /home/usuario/
```
- `ls` → comando (listar)
- `-la` → flags (modo detalhado + mostrar arquivos ocultos)
- `/home/usuario/` → argumento (caminho)

---

## 📂 1. Navegação entre Diretórios

```bash
pwd                     # Mostra o diretório atual (Print Working Directory)
ls                      # Lista arquivos e pastas do diretório atual
cd nome_da_pasta        # Entra na pasta especificada
cd ..                   # Volta uma pasta (diretório anterior)
cd ~                    # Vai para a pasta HOME do usuário
cd /                    # Vai para a raiz do sistema
cd -                    # Volta para o último diretório que estava
```

**Flags do `ls` (listar):**
```bash
ls -l                   # Formato detalhado (permissões, dono, tamanho, data)
ls -a                   # Mostra arquivos ocultos (começam com .)
ls -la                  # Junta os dois: detalhado + ocultos
ls -lh                  # Tamanho em formato legível (KB, MB, GB)
ls -R                   # Lista recursivamente (pastas dentro de pastas)
ls -S                   # Ordena por tamanho (maior primeiro)
ls -t                   # Ordena por data de modificação (mais recente primeiro)
```

---

## 📁 2. Manipulação de Arquivos e Pastas

### Criar

```bash
mkdir nome_da_pasta              # Cria uma pasta
mkdir -p caminho/com/pastas      # Cria pastas intermediárias se não existirem
touch arquivo.txt                # Cria arquivo vazio (ou atualiza data de modificação)
```

### Copiar

```bash
cp arquivo.txt destino/                    # Copia arquivo para pasta
cp arquivo.txt novo_nome.txt               # Copia com nome diferente
cp -r pasta/ destino/                      # Copia pasta inteira (recursivo)
cp -i arquivo.txt destino/                 # Pergunta antes de sobrescrever (interactive)
cp -v arquivo.txt destino/                 # Mostra o que está sendo copiado (verbose)
```

### Mover / Renomear

```bash
mv arquivo.txt destino/                    # Move arquivo para pasta
mv arquivo.txt novo_nome.txt               # Renomeia arquivo
mv -i arquivo.txt destino/                 # Pergunta antes de sobrescrever
mv -v arquivo.txt destino/                 # Mostra o que está sendo movido
```

### Remover ⚠️

```bash
rm arquivo.txt                             # Remove arquivo
rm -r pasta/                               # Remove pasta e TODO seu conteúdo (recursivo) ⚠️
rm -f arquivo.txt                          # Força remoção sem perguntar (force)
rm -rf pasta/                              # Remove pasta recursivamente e sem perguntar ☠️
rm -i arquivo.txt                          # Pergunta antes de remover cada arquivo (interactive)
rm -v arquivo.txt                          # Mostra o que está sendo removido (verbose)
```

> **🛑 CUIDADO COM `rm -rf`**: Esse comando não pede confirmação e apaga tudo. Já vi iniciantes apagarem projetos inteiros por acidente!

---

## 👁️ 3. Visualização de Arquivos

```bash
cat arquivo.txt              # Mostra TODO conteúdo do arquivo (útil para arquivos pequenos)
less arquivo.txt             # Mostra conteúdo paginado (espaço = próx página, q = sair)
head arquivo.txt             # Mostra as primeiras 10 linhas
head -n 20 arquivo.txt       # Mostra as primeiras 20 linhas
tail arquivo.txt             # Mostra as últimas 10 linhas
tail -n 20 arquivo.txt       # Mostra as últimas 20 linhas
tail -f arquivo.log          # Monitora o arquivo em tempo real (útil para logs)
nl arquivo.txt               # Mostra conteúdo com números de linha
```

---

## 🔧 4. Edição de Texto (no terminal)

### Nano (simples e intuitivo)

```bash
nano arquivo.txt             # Abre o editor
```

Comandos dentro do Nano:
- `Ctrl + O` → Salvar (Write Out)
- `Ctrl + X` → Sair
- `Ctrl + K` → Recortar linha
- `Ctrl + U` → Colar
- `Ctrl + W` → Buscar texto

### Vim (poderoso, mas precisa aprender)

```bash
vim arquivo.txt              # Abre o editor
```

Dentro do Vim:
- `i` → Entrar no modo de inserção (escrever)
- `Esc` → Voltar ao modo normal
- `:w` → Salvar (write)
- `:q` → Sair (quit)
- `:wq` → Salvar e sair
- `:q!` → Sair sem salvar
- `dd` → Deletar linha
- `yy` → Copiar linha
- `p` → Colar

---

## 🧰 5. Utilitários Essenciais

### Buscar arquivos e textos

```bash
find . -name "arquivo.py"                # Busca arquivo pelo nome a partir da pasta atual
find . -name "*.txt"                     # Busca todos os .txt
find . -type d -name "teste"             # Busca PASTAS chamadas "teste"

grep "palavra" arquivo.txt               # Busca palavra dentro do arquivo
grep -r "palavra" .                      # Busca recursivamente em TODOS os arquivos
grep -i "palavra" arquivo.txt            # Ignora maiúsculas/minúsculas
grep -n "palavra" arquivo.txt            # Mostra o número da linha
grep -v "palavra" arquivo.txt            # Mostra linhas que NÃO contêm a palavra
```

### Compactar e descompactar

```bash
# ZIP
zip -r projeto.zip pasta/                # Compacta pasta em .zip
unzip projeto.zip                        # Descompacta .zip

# TAR.GZ (mais comum no Linux)
tar -czvf projeto.tar.gz pasta/          # Compacta pasta
tar -xzvf projeto.tar.gz                 # Descompacta

# Flags do tar:
# -c = create (criar)
# -x = extract (extrair)
# -z = gzip (compactar/descompactar)
# -v = verbose (mostrar processo)
# -f = file (nome do arquivo)
```

---

## 👤 6. Permissões e Usuários

```bash
whoami                    # Mostra seu nome de usuário
id                        # Mostra seu ID e grupos

chmod +x script.sh        # Torna o arquivo executável
chmod 755 script.sh       # Define permissões específicas (dono=rwx, grupo=rx, outros=rx)

chown usuario:grupo arquivo.txt   # Muda dono e grupo do arquivo (precisa de sudo)
```

**Entendendo permissões do `ls -l`:**
```bash
-rw-r--r-- 1 usuario grupo 1024 Jan 15 10:00 arquivo.txt
drwxr-xr-x 2 usuario grupo 4096 Jan 15 10:00 pasta/
  ^^^^
  ||||
  |||+-- outros (r-- = leitura)
  ||+--- grupo (r-- = leitura)
  |+---- dono (rw- = leitura e escrita)
  +----- tipo (- = arquivo, d = diretório)
```

---

## 🌐 7. Rede e Internet

```bash
ping google.com              # Testa conexão com a internet
curl https://api.github.com  # Faz requisição HTTP (útil para APIs)
wget https://site.com/arquivo.zip   # Baixa arquivo da internet
ifconfig                     # Mostra informações de rede (IP, etc.)
ip a                         # Alternativa moderna ao ifconfig
```

---

## 🔄 8. Redirecionamento e Pipe

```bash
# >  = Redireciona SAÍDA para um arquivo (sobrescreve)
echo "texto" > arquivo.txt

# >> = Redireciona SAÍDA para um arquivo (adiciona ao final)
echo "mais texto" >> arquivo.txt

# <  = Redireciona ENTRADA a partir de um arquivo
sort < arquivo.txt

# |  = Pipe: envia saída de um comando como entrada de outro
ls -la | grep ".py"          # Lista apenas arquivos .py
cat arquivo.txt | head -5    # Mostra primeiras 5 linhas
history | grep git           # Busca comandos git no histórico

# 2> = Redireciona ERROS para um arquivo
comando_inexistente 2> erro.log

# &> = Redireciona TUDO (saída + erros) para um arquivo
comando &> tudo.log
```

---

## 🎯 9. Exemplos Práticos Combinados

### Para seus projetos Python:

```bash
# 1. Criar estrutura de projeto
mkdir -p projetos/jogo_adivinhacao
cd projetos/jogo_adivinhacao

# 2. Criar arquivo .gitignore
cat > .gitignore << EOF
__pycache__/
*.pyc
.env
venv/
EOF

# 3. Criar e editar código
touch jogo.py
nano jogo.py

# 4. Testar o programa
python3 jogo.py

# 5. Verificar tamanho dos arquivos
ls -lh

# 6. Buscar por erros no código
grep -n "def " *.py          # Procura todas as funções definidas
grep -rn "TODO" .            # Procura todos os "TODO" no projeto

# 7. Compactar para backup
cd ..
tar -czvf jogo_backup.tar.gz jogo_adivinhacao/
```

---

## 📋 10. Atalhos do Terminal

```bash
Ctrl + C          # Interrompe comando atual (mata processo)
Ctrl + D          # Finaliza entrada (ou sai do terminal)
Ctrl + Z          # Pausa o processo (volta com fg)

Ctrl + A          # Vai para o início da linha
Ctrl + E          # Vai para o final da linha
Ctrl + U          # Apaga tudo antes do cursor
Ctrl + K          # Apaga tudo depois do cursor
Ctrl + W          # Apaga palavra anterior

Ctrl + L          # Limpa a tela (igual comando clear)
Ctrl + R          # Busca comando digitado anteriormente (reverse search)

Seta ↑ / ↓        # Navega pelo histórico de comandos
Tab               # Auto-completar nomes de arquivos/pastas
Tab + Tab         # Mostra sugestões de auto-completar
```

---

## 🚀 Comandos Mais Perigosos (NUNCA Execute sem Saber)

```bash
rm -rf /              # ☠️ Apaga TODO o sistema (formatar o PC)
rm -rf ~              # ☠️ Apaga sua pasta HOME (todos seus arquivos)
:(){ :|:& };:         # ☠️ "Fork bomb" - trava o computador
dd if=/dev/zero of=/dev/sda  # ☠️ Sobrescreve o disco rígido
chmod -R 777 /        # ☠️ Dá permissão total a TODO sistema
```

---

## 💡 Aprendendo na Prática

O melhor jeito de aprender Linux é **usar**. Aqui vai um mini-desafio:

```bash
# Desafio: Criar e organizar seu primeiro projeto
mkdir -p ~/projetos_python/jogo_adivinhacao
cd ~/projetos_python/jogo_adivinhacao
# (copie seu código do jogo para cá)
ls -la
cat jogo.py
```

Amanhã quando você acordar, tente lembrar desses comandos sem consultar o guia. Depois confira o que errou. Repetição é a chave!

Precisa que eu detalhe algum comando específico ou quer continuar com o **Projeto 2 (Calculadora Dinâmica)**? 🚀