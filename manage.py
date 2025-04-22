import Project

from sign_up.confirmation import confirmation_email

def main():
    try:
        Project.load_env()
        # confirmation_email("egorgrockij1@gmail.com")
        Project.project.run(debug = True)
    except Exception as error:
        print(f'An error: {error}')

if __name__ == "__main__":
    main()