from Drawer import Drawer

def main():
    drawer = Drawer()
    names = input("Digite os nomes separados por vírgula: ")
    team_size = input("Digite o tamanho de cada equipe: ")
    drawer.set_names(names)
    drawer.set_teams_size(team_size)
    drawer.create_teams()
    drawer.show_teams()

if __name__ == "__main__":
    main()