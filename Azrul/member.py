class member:
    count =0
    def __init__(self, first_name,last_name, email, password, date_of_birth, phone_number, gender,image):
        member.count+= 1
        self.__user_id = member.count
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__date_of_birth = date_of_birth
        self.__phone_number = phone_number
        self.__gender = gender
        self.__image = image
        self.__postal_code = None
        self.__address = None
        self.__point = 100

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_password(self):
        return self.__password

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_phone_number(self):
        return self.__phone_number

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_point(self):
        return self.__point

    def get_image(self):
        return self.__image


    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name =first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_password(self,password):
        self.__password =password

    def set_date_of_birth(self,date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_gender(self, gender):
        self.__gender = gender

    def set_email(self, email):
        self.__email = email


    def set_point(self, point):
        self.__point = point

    def set_image(self, image):
        self.__image = image



class Address:
    def __init__(self,  country, company, address, postal_code):
        # super().__init__(first_name,last_name, email, password, date_of_birth, phone_number, gender,image)
        self.country = country
        self.company = company
        self.address = address
        # self.house = house
        self.postal_code = postal_code

    def set_country(self, country):
        self.country = country

    def set_company(self, company):
        self.company = company

    def set_address(self, address):
        self.address = address

    def set_house(self, house):
        self.house =house

    def set_postal_code(self,postal_code):
        self.postal_code = postal_code


    def get_country(self):
        return self.country

    def get_company(self):
        return self.company

    def get_address(self):
        return self.address

    def get_house(self):
        return self.house

    def get_postal_code(self):
        return self.postal_code

