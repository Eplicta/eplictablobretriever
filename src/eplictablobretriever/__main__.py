import cli
from initialize import initialize

__app_name__ = "blobretriever"

def main():
    initialize()
    cli.app(prog_name= __app_name__)

if __name__ == '__main__':
    main()
