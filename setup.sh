mkdir -p ~/.streamlit/

echo "[server]
headless = true
serverAddress = "0.0.0.0"
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
