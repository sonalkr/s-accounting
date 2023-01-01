## Genrate code
watchmedo shell-command --patterns="*g.py;*.sql;*.code.*"  --command='python main.py' --recursive

## Run server
uvicorn server_fastapi.server:server --reload
