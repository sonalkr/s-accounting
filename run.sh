echo running
source .venv/bin/activate
echo pwd
watchmedo shell-command --patterns="*g.py;*.sql;*code.py"  --command='python main.py' --recursive

# uvicorn tools.schema_viewer:app --reload