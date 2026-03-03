# 🤖 Projeto de Automação Cadastral

Um sistema automático de cadastro de produtos em lote usando Python, desenvolvido para automatizar a entrada de dados de produtos em plataformas web.

## 📋 Descrição

Este projeto utiliza **automação RPA (Robotic Process Automation)** para realizar o cadastro automático de produtos a partir de um arquivo CSV. O sistema:

- ✅ Acessa um formulário web automaticamente
- ✅ Realiza login no sistema
- ✅ Preenche formulários com dados de produtos
- ✅ Processa múltiplos produtos em lote
- ✅ Valida e trata dados incompletos

**Perfeito para**: Grandes volumes de cadastros, atualização em lote, integração de dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **PyAutoGUI** - Automação de mouse e teclado
- **Pandas** - Manipulação e leitura de dados CSV
- **Navegador Opera** - Para acesso à plataforma web

## 📦 Requisitos

- Python 3.6+
- pip (gerenciador de pacotes Python)
- Navegador Opera instalado
- Arquivo CSV com dados de produtos

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/C-amorim/Projeto-de-Automacao.git
cd Projeto-de-Automacao
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install pandas pyautogui
```

## 💻 Como Usar

### 1. Prepare o arquivo CSV
O arquivo `produtos.csv` deve conter as seguintes colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| codigo | string | Código único do produto |
| marca | string | Marca do produto |
| tipo | string | Tipo/Categoria do produto |
| categoria | integer | Número da categoria |
| preco_unitario | float | Preço unitário |
| custo | float | Custo do produto |
| obs | string | Observações (opcional) |

**Exemplo:**
```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
MOLO000192,Logitech,Mouse,2,19.95,5.00,
CAHA000251,Hashtag,Camisa,1,25.00,11.00,Conferir estoque
```

### 2. Configure as credenciais
Edite o arquivo `Sistema_de_Automacao.py` e atualize:

```python
Link = "https://seu-site-aqui.com/login"  # URL do sistema

# Credenciais de login
pyautogui.write("seu_email@exemplo.com")
pyautogui.press("tab")
pyautogui.write("sua_senha_aqui")
```

### 3. Execute o sistema
```bash
python Projeto_de_Automação/Sistema_de_Automacao.py
```

**⚠️ Importante**: 
- O script abrirá o navegador automaticamente
- Não mexa no mouse/teclado durante a execução
- A velocidade padrão é 1 segundo entre ações (ajustável via `pyautogui.PAUSE`)

## 📁 Estrutura do Projeto

```
Projeto-de-Automacao/
├── Projeto_de_Automação/
│   ├── Sistema_de_Automacao.py      # Script principal de automação
│   ├── Localizar_Ponteiro.py        # Utilitário para encontrar coordenadas
│   └── produtos.csv                 # Arquivo de dados dos produtos
└── README.md
```

### Descrição dos Arquivos

- **`Sistema_de_Automacao.py`**: Script principal que automatiza todo o processo
  - Abre o navegador
  - Faz login
  - Lê dados do CSV
  - Preenche os formulários automaticamente

- **`Localizar_Ponteiro.py`**: Ferramenta auxiliar para encontrar coordenadas do mouse
  - Útil para ajustar as coordenadas `x, y` do mouse no seu sistema
  - Execute e mova o mouse para descobrir as posições exatas

- **`produtos.csv`**: Base de dados com os produtos a cadastrar

## 🎯 Funcionalidades Principais

### 1. **Automação de Login**
```python
pyautogui.click(x=726, y=448)  # Clica no campo de email
pyautogui.write("seu_email@exemplo.com")
pyautogui.press("tab")
pyautogui.write("sua_senha")
pyautogui.press("enter")
```

### 2. **Leitura de Dados em Lote**
```python
Tabela = pd.read_csv("Projeto_de_Automação/produtos.csv")
for Linha in Tabela.index:
    # Processa cada linha do CSV
```

### 3. **Preenchimento de Formulários**
Preenche automaticamente todos os campos:
- Código
- Marca
- Tipo
- Categoria
- Preço
- Custo
- Observações

### 4. **Tratamento de Campos Opcionais**
```python
obs = Tabela.loc[Linha, "obs"]
if pd.notna(obs):  # Verifica se não é vazio
    pyautogui.write(str(obs))
```

## ⚙️ Configuração Avançada

### Ajustar a Velocidade de Execução
```python
pyautogui.PAUSE = 2  # Aumenta para 2 segundos entre ações
# ou
pyautogui.PAUSE = 0.5  # Diminui para 0.5 segundos
```

### Encontrar Novas Coordenadas
Execute `Localizar_Ponteiro.py` para descobrir as coordenadas corretas:
```bash
python Projeto_de_Automação/Localizar_Ponteiro.py
```
- Aguarde 5 segundos
- Mova o mouse para a posição desejada
- As coordenadas serão exibidas no console

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| "ModuleNotFoundError: No module named 'pandas'" | Execute: `pip install pandas` |
| "ModuleNotFoundError: No module named 'pyautogui'" | Execute: `pip install pyautogui` |
| Script não clica nos lugares certos | Execute `Localizar_Ponteiro.py` e atualize as coordenadas |
| Navegador não abre | Certifique-se que Opera está instalado ou altere para Chrome/Firefox |
| CSV não encontrado | Verifique o caminho do arquivo no script |

## 📊 Exemplo de Execução

```bash
$ python Projeto_de_Automação/Sistema_de_Automacao.py

✓ Abrindo Opera...
✓ Acessando login...
✓ Preenchendo credenciais...
✓ Cadastrando produtos: 1/345
✓ Cadastrando produtos: 2/345
...
✓ Processo concluído!
```

## 🔒 Segurança

⚠️ **Importante**: 
- Nunca comita credenciais no repositório
- Use variáveis de ambiente para senhas
- Limpe senhas antes de fazer commit

**Exemplo com variáveis de ambiente:**
```python
import os
email = os.getenv("EMAIL")
senha = os.getenv("SENHA")
```

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👤 Autor

**C-amorim**

## 🤝 Contribuições

Contribuições são bem-vindas! Se encontrou um bug ou tem sugestões:

1. Abra uma issue descrevendo o problema
2. Faça um fork do projeto
3. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
4. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
5. Push para a branch (`git push origin feature/AmazingFeature`)
6. Abra um Pull Request

## 📞 Suporte

Se tiver dúvidas ou problemas:
- Abra uma [issue](https://github.com/C-amorim/Projeto-de-Automacao/issues)
- Consulte a seção [Troubleshooting](#troubleshooting)

## ✨ Melhorias Futuras

- [ ] Interface gráfica (GUI)
- [ ] Suporte a múltiplos navegadores
- [ ] Log detalhado de execução
- [ ] Tratamento de erros mais robusto
- [ ] Testes automatizados
- [ ] Suporte a banco de dados

---

**Desenvolvido com ❤️ em Python**