#!/bin/bash

./scripts/wait-for-db.sh db 5432

alembic upgrade head

printenv DB_NAME

if [ "$ENVIROMENT" == "production" ]; then 
  uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
  echo "Production mode"
elif [ "$ENVIROMENT" == "development" ]; then 
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  echo "Development mode"
fi

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload