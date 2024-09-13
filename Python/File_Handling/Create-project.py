def project():
    project_num = int(input('number of project: '))
    suffix = input('purpose of project: ')
    try:
        file = open(f'project {project_num} ({suffix}).py', 'x')
        file.close()
    except FileExistsError:
        return False


while True:
    if project() is None:
        break
    print('\nfile already exists\n', '-'*72)
    print()
