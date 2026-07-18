# 📘 Guia Completo: Enviando seu Projeto para o GitHub pela Primeira Vez

---

## 📦 Primeiro Envio: Do Zero ao GitHub

### 1️⃣ Criar o repositório no GitHub
Vá até [github.com](https://github.com) → clique no **+** (canto superior direito) → **New repository**

Preencha:
- **Repository name**: `jogo-adivinhacao` (ou o nome do seu projeto)
- **Description**: opcional
- Marque **Public** ou **Private**
- **NÃO marque** "Initialize this repository with a README" (vamos criar localmente)
- Clique em **Create repository**

### 2️⃣ Configurar o Git no seu computador (primeira vez apenas)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --global init.defaultBranch main
```

### 3️⃣ Preparar o projeto localmente

Navegue até a pasta do seu projeto:

```bash
cd ~/Documentos/projetos_python/jogo_adivinhacao/
```

Crie o arquivo `.gitignore` (para não enviar arquivos desnecessários):

```bash
# Cria um arquivo .gitignore básico para Python
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
venv/
.env
*.egg-info/
dist/
build/
.idea/
.vscode/
*.swp
*.swo
*~
.DS_Store
EOF
```

### 4️⃣ Inicializar o Git e fazer o primeiro commit

```bash
# Inicializar o repositório Git
git init

# Verificar o que vai ser enviado
git status

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Primeiro commit - Jogo de Adivinhação"
```

### 5️⃣ Conectar ao GitHub

```bash
# Adicionar o repositório remoto (use a URL do seu repositório)
git remote add origin https://github.com/seu-usuario/jogo-adivinhacao.git

# Verificar se a conexão funcionou
git remote -v
```

### 6️⃣ Enviar para o GitHub

```bash
# Primeiro push (precisa da flag -u para definir a branch upstream)
git push -u origin main
```

> ⚠️ **Importante**: Na primeira vez que fizer `git push`, o GitHub pode pedir autenticação. Veja a seção abaixo.

---

## 🔑 Autenticação no GitHub

### Opção 1: Token (recomendada - mais segura)

1. Vá em GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Clique em **Generate new token (classic)**
3. Dê um nome, marque `repo` e `workflow`
4. Copie o token gerado (só aparece uma vez!)
5. Quando o terminal pedir **username**: digite seu usuário do GitHub
6. Quando pedir **password**: **cole o token** (não a senha do GitHub)

### Opção 2: GitHub CLI (mais fácil)

```bash
# Instalar o GitHub CLI
# No Linux: sudo apt install gh
# No Mac: brew install gh
# No Windows: baixar do site

# Autenticar
gh auth login

# Seguir os passos no terminal (login pelo navegador)
```

### Opção 3: SSH (avançado, mas prático depois)

```bash
# Gerar chave SSH
ssh-keygen -t ed25519 -C "seu@email.com"

# Copiar a chave pública
cat ~/.ssh/id_ed25519.pub

# Adicionar no GitHub: Settings → SSH and GPG keys → New SSH key

# Depois usar a URL SSH em vez de HTTPS
git remote add origin git@github.com:seu-usuario/jogo-adivinhacao.git
```

---

## 🔄 Fluxo de Trabalho Diário (após o primeiro envio)

```bash
# 1. Verificar o status
git status

# 2. Adicionar mudanças
git add .
# ou git add nome_do_arquivo.py

# 3. Commitar
git commit -m "Descrição clara do que mudou"

# 4. Enviar para o GitHub
git push

# 5. Se houver mudanças no GitHub (trabalho em equipe)
git pull
```

---

## 🎯 Exemplo Prático: Seu Projeto Jogo de Adivinhação

Vou simular o processo completo com seu código:

```bash
# 1. Criar a pasta do projeto
mkdir ~/Documentos/projetos_python/jogo_adivinhacao
cd ~/Documentos/projetos_python/jogo_adivinhacao

# 2. Criar o arquivo do jogo
# (coloque seu código no arquivo jogo.py)

# 3. Criar .gitignore
cat > .gitignore << EOF
__pycache__/
*.pyc
.env
venv/
.DS_Store
EOF

# 4. Inicializar e commitar
git init
git add .
git commit -m "Primeiro commit - Jogo de Adivinhação com validação de entrada"

# 5. Criar repositório no GitHub (pelo site)
# Nome: jogo-adivinhacao
# Não inicializar com README

# 6. Conectar e enviar
git remote add origin https://github.com/seu-usuario/jogo-adivinhacao.git
git push -u origin main
```

---

## 📊 Comandos Essenciais que Estavam Faltando

### Ver histórico e diferenças

```bash
# Ver logs de forma mais legível
git log --oneline --graph --all

# Ver o que mudou entre commits
git diff
git diff --staged  # mudanças que estão no stage

# Ver detalhes de um commit específico
git show hash_do_commit
```

### Desfazer coisas

```bash
# Desfazer último commit mantendo alterações
git reset --soft HEAD~1

# Desfazer último commit PERDENDO alterações (cuidado!)
git reset --hard HEAD~1

# Remover arquivo do stage (útil se add algo errado)
git restore --staged arquivo.py

# Descartar mudanças em um arquivo
git restore arquivo.py
```

### Trabalhar com branches

```bash
# Criar branch para testar uma feature
git checkout -b teste-nova-feature

# Fazer alterações e commitar na branch
git add .
git commit -m "Testando nova funcionalidade"

# Voltar para main e mesclar
git checkout main
git merge teste-nova-feature

# Deletar branch que não precisa mais
git branch -d teste-nova-feature
```

---

## 🚨 Problemas Comuns e Soluções

### "failed to push some refs"
```bash
# Seu repositório local está desatualizado
git pull origin main --rebase
git push
```

### "Authentication failed"
```bash
# Seu token expirou ou está incorreto
# Gere um novo token no GitHub
git remote set-url origin https://novo-token@github.com/usuario/repo.git
```

### Esqueceu de fazer .gitignore antes do commit
```bash
# Se já commitou arquivos que deveriam estar no .gitignore
git rm --cached -r pasta_ou_arquivo
# Adicione a pasta/arquivo no .gitignore
# Depois faça um novo commit
```

---

## 📁 Estrutura Recomendada para seus Projetos

```
projetos_python/
├── .gitignore (global com regras comuns)
├── jogo_adivinhacao/
│   ├── .gitignore
│   ├── jogo.py
│   └── README.md
├── calculadora/
│   ├── .gitignore
│   ├── calculadora.py
│   └── README.md
└── outros_projetos/
```

---

## 🎯 Resumo para seu Próximo Projeto

Depois de fazer o primeiro projeto com sucesso (Jogo de Adivinhação), para o **segundo** projeto (Calculadora Dinâmica), os passos serão apenas:

```bash
# NOVO projeto
mkdir calculadora_dinamica && cd calculadora_dinamica
# criar o arquivo .gitignore e o código
git init
git add .
git commit -m "Calculadora com funções"
# criar repositório no GitHub
git remote add origin https://github.com/seu-usuario/calculadora-dinamica.git
git push -u origin main
```

---

