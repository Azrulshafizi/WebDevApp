class member:
    count =0
    def __init__(self,first_name, last_name, password,date_of_birth, phone_number,):
        member.count+= 1
        self.__user_id = ""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password
        self.__date_of_birth = date_of_birth
        self.__phone_number = phone_number

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name =first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
