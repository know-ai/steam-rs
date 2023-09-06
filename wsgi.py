from app import CreateApp
from app.helpers import init_logging

init_logging()
application = CreateApp()

# Serve App
app = application()

# Import variables defined when CreateApp
from app import port


if __name__=="__main__":
    
    app.run(host="0.0.0.0", port=port)