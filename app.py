import os
from api.index import app

if __name__ == "__main__":
    debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5005))
    try:
        app.run(host='0.0.0.0', port=port, debug=debug_mode)
    except Exception as e:
        import logging
        logging.critical(f"Failed to start wrapper server: {e}")
        raise