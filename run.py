import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()

config_name = os.getenv('FLASK_ENV') or 'development'
app = create_app(config_name)

if __name__ == "__main__":
    app.run(
        debug=True,
        use_debugger=True,
        use_reloader=True,
        host='0.0.0.0'
    )
