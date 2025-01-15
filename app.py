import streamlit as st
import folium
from streamlit_folium import st_folium
from utils.weather_api import get_weather

# Configuração da página
st.set_page_config(page_title="The Weather Forecast", page_icon="🌤️", layout="centered")
st.title("🌤️ The Weather Forecast")

# Inicializando session_state para armazenar os dados
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None
if "map_data" not in st.session_state:
    st.session_state.map_data = None

# Input de cidade e unidades
city = st.text_input("Enter a city name", "Rio de Janeiro")
units = st.selectbox("Select temperature units", ["metric", "imperial"])

if st.button("Get Weather"):
    weather_data = get_weather(city, units)
    
    if "error" in weather_data:
        st.error(weather_data["error"])
    else:
        # Armazenar os dados no session_state
        st.session_state.weather_data = weather_data
        st.session_state.map_data = {
            "lat": weather_data["coord"]["lat"],
            "lon": weather_data["coord"]["lon"],
        }

# Exibir os dados do clima se disponíveis
if st.session_state.weather_data:
    weather_data = st.session_state.weather_data

    # Informações do tempo
    st.subheader(f"Weather in {weather_data['name']}")
    icon_code = weather_data["weather"][0]["icon"]
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(icon_url, width=120)
    with col2:
        st.metric(label="Temperature", value=f"{weather_data['main']['temp']}°")
        st.write(f"**Condition:** {weather_data['weather'][0]['description'].capitalize()}")
        st.write(f"**Humidity:** {weather_data['main']['humidity']}%")
    
    # Coordenadas da cidade
    lat, lon = st.session_state.map_data["lat"], st.session_state.map_data["lon"]
    
    # Criar o mapa com folium
    map_ = folium.Map(location=[lat, lon], zoom_start=10)
    
    # Ícone personalizado para o pin
    popup_content = f"""
    <strong>{weather_data['name']}</strong><br>
    🌡️ {weather_data['main']['temp']}°C<br>
    🌤️ {weather_data['weather'][0]['description'].capitalize()}<br>
    💧 {weather_data['main']['humidity']}% Humidity
    """
    folium.Marker(
        [lat, lon],
        popup=folium.Popup(popup_content, max_width=300),
        icon=folium.Icon(color="blue", icon="cloud", prefix="fa")  # Usando FontAwesome
    ).add_to(map_)
    
    # Exibir o mapa no Streamlit
    st_folium(map_, width=700, height=500)
