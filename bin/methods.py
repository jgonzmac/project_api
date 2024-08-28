from json_reader import *

class Methods():

    def __init__(self) -> None:
        pass


    def __str__(self) -> str:
        info = '''This class defines all the methods for our API project, including operations such as adding, deleting, and updating users, retrieving user information, and creating or deleting databases.'''
        return info


    def post(self, data_base: dict) -> None:
        """
        Adds a new user into the selected Data Base.
        Args:


        Returns:
        """

        # Reading all the unique keys in the json file.
        keys = set()
        data_base = data_base.values()
        for i in data_base:
            for j in i:
                keys.update(j.keys())
        json_keys = list(keys)

        # Asking the user for the values of the new user.
        new_users_list = list()
        while True:
            new_user = dict()
            for key in json_keys:
                new_user[key] = str(input(f'Please, type the new value for {key}: ').strip())
            new_users_list.append(new_user)
            add_more_users = input('Do you want to add more users (Y/N): ')
            if add_more_users.lower() == 'y':
                continue
            else:
                break

        print(new_users_list)


        # Writing the data into the json file.




    def delete(self) -> None:
        """
        Elimina un usuario de la base de datos seleccionada.
        Args:


        Returns:
        """
        pass


    def put(self) -> None:
        """
        Actualiza la información de un usuario de la base de datos seleccionada.
        Args:


        Returns:
        """
        pass


    def get(self) -> None:
        """
        Consulta la información de un usuario de la base de datos seleccionada.
        Args:


        Returns:
        """
        pass


    def drop(self) -> None:
        """
        Elimina la base de datos seleccionada.
        Args:


        Returns:
        """
        pass


    def create(self) -> None:
        """
        Crea una nueva base de datos.
        Args:


        Returns:
        """
        pass


