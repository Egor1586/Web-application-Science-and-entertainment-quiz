import Project

def main():
    try:
        Project.project.run(debug = True)
    except Exception as error:
        print(f'An error: {error}')

if __name__ == "__main__":
    main()