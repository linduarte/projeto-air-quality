🌍 Air Quality Analysis Dashboard
Interface de alta performance para análise de impacto ambiental e zonificação urbana.

Este projeto utiliza Python e Dear PyGui para processar e visualizar dados globais de poluição, permitindo a comparação imediata entre áreas industriais e residenciais através de renderização acelerada por GPU.

🚀 Como Executar
O projeto utiliza o gerenciador de pacotes uv para garantir máxima performance e isolamento.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/projeto-air-quality.git

# Execute instantaneamente
uv run src/main.py
```

🏎️ Alta Performance via GPU
Diferente de frameworks tradicionais (como Matplotlib ou Tkinter) que processam gráficos na CPU, este dashboard utiliza o Dear PyGui com backend em DirectX11.

Latência Zero: Manipulação de séries temporais com milhares de pontos sem perda de frames.

GPU Rendering: O processamento gráfico é delegado à placa de vídeo, liberando a CPU para auditoria de dados no utils.py.

🧪 Engenharia de Dados
O motor do sistema foi construído sobre uma arquitetura de desacoplamento entre interface e lógica:

Pandas Integration: Manipulação eficiente de DataFrames e limpeza automática de registros inconsistentes.

Time-Series Alignment: Conversão dinâmica de Timestamps (np.int64) para precisão milimétrica no eixo temporal.

Zoning Segmentation: Filtros inteligentes que separam perfis Industriais e Residenciais em tempo real.

📊 Mapeamento do Dataset
O sistema realiza a auditoria automática (utils.py) baseada no seguinte esquema de dados:

Tempo: Coluna Date (Auto-conversão para DateTime).

Variável Alvo: Coluna PM2.5 (Concentração de partículas finas).

Zonificação: Coluna Type (Segmentação por tipo de área).

🖱️ Guia de Análise Interativa
Zoom Dinâmico: Use o scroll do mouse ou selecione áreas para focar em picos de poluição.

Legendas Interativas: Clique nos nomes das séries para isolar visualmente uma zona específica.

Crosshair & Tooltips: Passe o mouse sobre as linhas para obter a leitura contextual de cada ponto de dado.

Exportação: O botão Exportar CSV Limpo consolida os dados auditados na pasta data/processed/.

📂 Estrutura do Projeto

```Plaintext
├── data/
│   ├── raw/         # Dataset original (CSV)
│   └── processed/   # Saída de dados auditados
├── src/
│   ├── main.py      # Interface e Renderização GPU
│   └── utils.py     # Motor de Auditoria e Estatística
└── pyproject.toml   # Gestão de dependências (uv)
```


