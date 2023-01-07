from pakuri import *


evolved_pakuris = []

class Pakudex:
    # Pakudex has a list of Pakuri
    def __init__(self, capacity=20):
        self.pakuris = []
        self.capacity = capacity
        self.size = 0 #intial amount of pakuri in the pakudex

    def add_pakuri(self, species):
        # 1. Check duplicates
        # 2. When list is full
        critter = Pakuri(species)
        if species in self.pakuris:
            return False            # won't add if pakuri already exists

        else:
            self.pakuris.append(critter.species)
            self.size += 1
            return True
        # add pakuri into sel.pakuris
        # imports the species from pakuri.py

    def get_size(self):
        return self.size   # returns size

    def get_capacity(self):
        return self.capacity # returns capacity

    def get_stats(self, species):
        stats_list = []
        pak_evol = Pakuri(species)
        if species in self.pakuris:
            stats_list = [Pakuri(species).get_attack(), Pakuri(species).get_defense(), Pakuri(species).get_speed()]
            if species in evolved_pakuris:
                pak_evol.evolve()
                stats_list =[pak_evol.get_attack(), pak_evol.get_defense(), pak_evol.get_speed()]
            return stats_list
        else:
            return None


    def get_species_array(self):
        final_list = []
        for item in self.pakuris:
            sp = item
            final_list.append(sp)  # pakuri to list

        if final_list == []:    # if list is blank it returns nothing
            return None

        return final_list       # return list

    def sort_pakuri(self):
        self.pakuris.sort()
        return True

    def evolve_species(self, species):

        for pakuri in self.pakuris:
            if pakuri == species:
                evolved_pakuris.append(species)
                return True
        return False

