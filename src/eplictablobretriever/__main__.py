from package.cli import app
from package.initialize import initialize

__app_name__ = "eplictablobretriever"

def main():
    initialize()
    app(prog_name= __app_name__)

if __name__ == '__main__':
    main()
