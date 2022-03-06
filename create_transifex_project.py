
import sys
def create_transifex_project():
    release_name = sys.argv[1]
    tx_token = sys.argv[2]
    print('I am the release name',release_name)
    print('How dare you print me!',tx_token)


if __name__ == "__main__":
    create_transifex_project()