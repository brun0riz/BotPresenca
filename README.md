# BotPresenca

## Descrição
O **BotPresenca** é um bot desenvolvido para o Discord, com o objetivo de gerenciar a lista de presenças de um canal específico. Ele permite registrar os nomes dos participantes e registrar a data e hora de entrada, facilitando o controle de presença em reuniões, aulas ou eventos.

## Funcionalidades
- **Registro de presença**: Capta automaticamente os nomes dos participantes que enviam uma mensagem no canal especificado.
- **Limite de tempo**: Permite a configuração de um tempo limite de 15 minutos para que os usuários registrem presença.
- **Armazenamento em planilha**: Salva a lista de presença em uma planilha Excel, com o nome do usuário, data e hora de entrada.

## Pré-requisitos
- Python 3.x
- Biblioteca `discord.py`
- Biblioteca `openpyxl` (para manipulação de planilhas Excel)

## Como Usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/BotPresenca.git
   cd BotPresenca
2. Instale as dependencias:
   ```bash
   pip install -r requirements.txt
3. Atualizações das informações no código:
   - **ID do canal**: Vá no canal que deseja que as presenças sejam registradas e siga os seguintes passos: 'Botão direito do mouse em cima do canal -> Copiar ID do canal'
        - **Caso essa opção não apareça, verifique se o modo de desenvolvedor do Discord está ativado, indo em 'Configurações -> Avançado -> Modo desenvolvedor'
# 
### Desenvolvido por Bruno Trevizan Rizzatto
