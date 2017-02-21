import csv

class City:

    all_area = []

    def __init__(self, name, type_area, voivodeship):
        self.name = name
        self.type_area = type_area
        self.voivodeship = voivodeship

    @classmethod
    def data_reader(cls, filename):
        with open(filename, "r") as f:
            data_string = csv.reader(f, delimiter="\t")
            for line in data_string:
                if line[3].isdigit():
                    c = City(line[4], line[5], line[0])
                    cls.all_area.append(c)

        return cls.all_area

    @classmethod
    def area(cls):
        county_types={}
        for item in cls.all_area:
            county_types[item.type_area] = 0
        for key in county_types:
            i = 0
            for item2 in cls.all_area:
                if key ==item2.type_area:
                    i += 1
            county_types[key] = i
        return county_types


    @classmethod
    def longest_name_cities(cls):
        sorted_list = sorted(cls.all_area, key = lambda x: len(x.name), reverse = True)
        three_longest = [["1", sorted_list[1].name],["2", sorted_list[2].name],["3", sorted_list[3].name]]
        return three_longest


    @classmethod
    def county_name(cls):
        list_of_indicators = []
        dict ={}
        list_to_return=[]
        for citys in cls.all_area:
            if citys.type_area in ["powaiat", "miasto na prawach powiatu"]:
                list_of_indicators.append(citys.comunity_indicator)
        for types in list_of_indicators:
            i = -1
            for item in cls.all_area:
                dupa = item.comunity_indicator
                if dupa == types:
                     i= i+1
                     dict[dupa] = i
        for item in cls.all_area:
            for key in dict:
                if key == item.comunity_indicator and item.district in ["powaiat", "miasto na prawach powiatu"]:
                    list_to_return.append([str(dict[key]), item.name])
        sorted_list = sorted(list_to_return, key =lambda x: int(x[0]), reverse = True)
        return sorted_list

    @classmethod
    def lagerst_commiunty(cls):
        area_names =[]
        list_to_return=[]
        i=1
        for city in cls.all_area:
            area_names.append(city.name)
        just_one = list(set(area_names))
        for citys in just_one:
            if area_names.count(citys) > 1:
                lista=[str(i),citys]
                i+=1
                list_to_return.append(lista)
        return list_to_return


    @classmethod
    def searching_f(cls, user_input):
        searching_list=[]
        for item in cls.all_area:
            if user_input in item.name:
                searching_list.append([item.name, item.type_area])
        searching_list.sort(key=lambda x: x[0]+x[1])
        return searching_list

