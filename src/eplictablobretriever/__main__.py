from .cli import app
from .initialize import initialize

__app_name__ = "eplictablobretriever"

def main():
    initialize()
    app(prog_name= __app_name__)

if __name__ == '__main__':
    main()
