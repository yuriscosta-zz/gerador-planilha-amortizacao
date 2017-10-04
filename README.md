# Gerador de planilhas de amortização
Software para geração de planilhas de amortização relativas a empréstimos financeiros.

## Instalação
Para que o sistema seja executado, é recomendável utilizar alguma distribuição GNU-Linux e que possuas a versão 3.5 do Python instalada. Caso esteja instalado, abra o seu terminal e siga os passos abaixo:
```bash
# Baixe a biblioteca Tkinter
apt install python3-tk

# Clone este repositório
git clone https://github.com/yuriscosta/planilha_amortizacao.git

# Entre no repositório
cd planilha_amortizacao

# Instale o virtualenv
pip install virtualenv

# Crie um ambiente virtual
virtualenv venv

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o arquivo do sistema
python main.py
```

## Como usar
![Tela inicial](http://i.imgur.com/TlvXTfE.png) <br>
Ao executar o sistema, a tela inicial do mesmo será aberta. Ela possui um formulário onde você preencherá os dados para que a sua planilha seja gerada.

![Tela inicial](http://i.imgur.com/NsTONHJ.png) <br>
Após preencher os dados corretamente, você deverá clicar no botão "gerar". Após essa ação, uma janela será aberta para que você possa escolher onde salvar a planilha.

![Tela inicial](http://i.imgur.com/gvnW8df.png) <br>
Clique em "Ok" após a seleção. Pronto! A sua planilha de amortização está pronta, basta agora ir no local onde você desejou salvar e abrir o arquivo que possui o nome escolhido no formulário.

![Tela inicial](http://i.imgur.com/vD9Zu47.png)
