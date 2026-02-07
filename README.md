## 🧪 Engenharia de Dados
- **Pandas Integration:** Utilizado para manipulação de DataFrames e limpeza de outliers.
- **Time-Series Alignment:** Conversão dinâmica de Timestamps para garantir precisão no eixo temporal dos gráficos.
- **Zoning Segmentation:** Filtros inteligentes para comparação imediata entre perfis Industriais e Residenciais.

## 📊 Guia de Análise
Ao rodar o dashboard:
1. **Zoom Dinâmico:** Use o mouse para focar em picos de poluição específicos.
2. **Legendas Interativas:** Clique na legenda (Industrial/Residencial) para ocultar/exibir uma das séries.
3. **Exportação:** O botão 'Exportar CSV Limpo' salva os dados processados pelo `utils.py` na pasta `data/processed/` para uso em modelos de Machine Learning.

## 📊 Mapeamento do Dataset
O sistema foi configurado para processar o cabeçalho padrão:
- **Tempo:** Coluna `Date`
- **Variável Alvo:** Coluna `PM2.5`
- **Zonificação:** Coluna `Type` (Industrial/Residential)

### 🏎️ Alta Performance via GPU
Diferente de frameworks tradicionais baseados em CPU, este dashboard utiliza o **Dear PyGui** para renderização acelerada por hardware (DirectX11). 
- **Latência Zero:** Manipulação de séries temporais com milhares de pontos sem perda de frames.
- **GPU Rendering:** O processamento gráfico é delegado à placa de vídeo, liberando a CPU para as tarefas de auditoria e limpeza de dados no `utils.py`.