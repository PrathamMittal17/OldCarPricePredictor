mkdir -p ~/.streamlit/

echo "[server]
headless = true
port = 0.0.0.0:PORT
enableCORS = false
" > ~/.streamlit/config.toml
