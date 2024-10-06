class ListHelper:
    @staticmethod
    def doubles(list):
        return len([x for x in set(list) if list.count(x) > 1])

    @staticmethod
    def greatest_frequency(list):
        return max([(x,list.count(x)) for x in list], key = lambda y: y[1])[0]