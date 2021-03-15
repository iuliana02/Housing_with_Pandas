class Haus:
    def __init__(self, longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households,median_income, median_house_value, ocean_proximity):
        self.__longitude = longitude
        self.__latitude = latitude
        self.__housing_median_age = housing_median_age
        self.__total_rooms = total_rooms
        self.__total_bedrooms = total_bedrooms
        self.__population = population
        self.__households = households
        self.__median_income = median_income
        self.__median_house_value = median_house_value
        self.__ocean_proximity = ocean_proximity

    def __str__(self):
        return self.longitude + self.latitude + self.housing_median_age + self.total_rooms + self.total_bedrooms + self.population + self.households + self.median_income + self.median_house_value + str(self.ocean_proximity)

    @property
    def longitude(self):
        return self.longitude

    @longitude.setter
    def longitude(self,long):
        self.__longitude=long

    @property
    def latitude(self):
        return self.latitude
    @latitude.setter
    def latitude(self,lat):
        self.latitude=lat

    @property
    def median_age(self):
        return self.housing_median_age
    @median_age.setter
    def median_age(self, housing_median_age):
        self.housing_median_age =housing_median_age

    @property
    def rooms(self):
        return self.total_rooms
    @rooms.setter
    def rooms(self, total_rooms):
        self.total_rooms = total_rooms

    @property
    def bedrooms(self):
        return self.total_bedrooms
    @bedrooms.setter
    def bedrooms(self, total_bedrooms):
        self.total_bedrooms = total_bedrooms

    @property
    def population(self):
        return self.population
    @population.setter
    def population(self, population):
        self.population = population

    @property
    def households(self):
        return self.households
    @households.setter
    def households(self, households):
        self.households = households

    @property
    def income(self):
        return self.median_income
    @income.setter
    def income(self, median_income):
        self.median_income = median_income

    @property
    def value(self):
        return self.median_house_value
    @value.setter
    def value(self, median_house_value):
        self.median_house_value = median_house_value

    @property
    def proximity(self):
        return self.ocean_proximity
    @proximity.setter
    def proximity(self, ocean_proximity):
        self.ocean_proximity = ocean_proximity

