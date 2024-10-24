#!/bin/sh
export AUTH0_DOMAIN="dev-free-test.us.auth0.com"
export ALGORITHMS="RS256"
export API_AUDIENCE="capstone"

export FLASK_APP=app.py
export FLASK_DEBUG=True
export FLASK_ENVIRONMENT=debug
export DATABASE_URL="postgresql://postgres:taokopit105@localhost:2912/capstone"

flask run --reload

