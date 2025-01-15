# Today's Climate: https://todayclimate.streamlit.app/

Today's Climate é uma aplicação web interativa construída com **Python** e **Streamlit**, que permite aos usuários verificar as condições climáticas atuais de qualquer cidade ao redor do mundo. Utilizando a API OpenWeather, o aplicativo exibe informações em tempo real, como temperatura, condição climática e umidade, além de apresentar a localização no mapa.

## 📋 Funcionalidades

- **Pesquisa por Cidade:** Os usuários podem pesquisar qualquer cidade no mundo.
- **Exibição do Clima Atual:** Mostra informações como:
  - Temperatura
  - Condição climática (ex: céu limpo, nublado, etc.)
  - Umidade
- **Visualização no Mapa:** Um mapa interativo com um marcador personalizado para a localização da cidade.
- **Suporte a Unidades de Temperatura:** Escolha entre unidades métricas ou imperiais.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Streamlit:** Framework para criar aplicações web de maneira rápida e fácil.
- **Folium:** Para exibição de mapas interativos.
- **OpenWeather API:** Para obtenção dos dados climáticos.

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. **Python 3.8+** instalado.
2. Uma conta na [OpenWeather](https://openweathermap.org/) para obter sua chave API.

### Passos

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/weather-now.git
   cd weather-now
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No Mac/Linux
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave API:

   ```env
   OPENWEATHER_API_KEY=your_api_key_here
   ```

5. Execute o aplicativo:

   ```bash
   streamlit run app.py
   ```

6. Acesse no navegador:

   ```
   http://localhost:8501
   ```

## 📖 Estrutura do Projeto

```plaintext
weather-now/
├── app.py               # Arquivo principal do aplicativo
├── utils/
│   ├── __init__.py      # Inicialização do módulo
│   ├── weather_api.py   # Script para integração com a API OpenWeather
├── requirements.txt     # Dependências do projeto
├── .env                 # Arquivo para armazenar variáveis de ambiente
├── README.md            # Documentação do projeto
```

## 🌟 Recursos Futuros

- Adicionar previsão do tempo para os próximos dias.
- Suporte para múltiplos idiomas.
- Melhorar o design com mais personalizações.
- Implementar gráficos interativos para exibir tendências climáticas.

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido por Gabriel Felipe Cordeiro Da Silva.
