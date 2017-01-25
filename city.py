class City:

    city_list = []

    def __init__(self, voivodeship, county, community, rgmi ,name, typ):
        self.voivodeship = voivodeship
        self.county = county
        self.community = community
        self.rgmi = rgmi
        self.name = name
        self.typ = typ

    @classmethod
     def creat_obj(cls, filename = "malopolska.csv"):
          with (filename, "r") as f:
              for line in f:
                  line = line.replace("\n", "").split(" ")
                  cls.city_list.append(City(line[0],line[1],line[2],line[3],line[4],line[5]))


    #
     @classmethod
     def display_all(cls):
         return cls.city_list
    #
    #
    # @classmethod
    # def display_all(cls):
    #     return cls.city_list