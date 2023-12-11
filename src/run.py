from app import app
import os, sys
if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    app.run()