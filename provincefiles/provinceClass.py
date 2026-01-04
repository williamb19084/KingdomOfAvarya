# A file that contains the class definition for a province
#Imports the constants
import sys
sys.path.append("..")

from constantfiles import bonuses

class Province:
    
    #The population variable is a dictionary in a dictionary in a dictionary
    def __init__(self, name, population, buildings):
        self.name = name
        self.population = population
        self.buildings = buildings
        self.stats = {} #IMPLEMENT
        self.upkeep = {
                "WATER" : 0,
                "LUMBER" : 0,
                "LIVESTOCK" : 0,
                "MINERALS" : 0,
                "CROPS" : 0
                }

        self.population_total = 0
        self.population_specie = {}
        self.population_workers = {
                "LOWER_CLASS" : 0,
                "MIDDLE_CLASS" : 0,
                "UPPER_CLASS" : 0
                }

        #These variables will be changed in intilizations, but they do need to be declared and have variables assigned
        self.primary_specie = "HUMANS"
        self.secondary_specie = "HUMANS"
        self.build_points_total = 0
        self.build_points_current = 0
        
        #Calculates all sub populations
        self.updatePopulations(population)

        # Calculates what size the province is
        # Also calculates other populations totals that are useful
        #for specie in self.population:
            #self.population_specie[specie] = 0
            #for eco_status in self.population[specie]:
                #self.population_workers[eco_status] += self.population[specie][eco_status]["ADULT"]
                #for age in self.population[specie][eco_status]:
                    #self.population_total += population[specie][eco_status][age]
                    #self.population_specie[specie] += population[specie][eco_status][age]

        #for specie in self.population_specie:
            #if self.population_specie[specie] > self.population_specie[self.primary_specie]:
                
                #Moves the previous primary species down to the secondary specie
                #self.secondary_specie = self.primary_specie
                #self.primary_specie = specie
        
        #Determines what size the province is
        #for pop_req in bonuses.PROVINCE_CONSTANTS["POP_REQUIREMENTS"]:
            #if self.population_total > bonuses.PROVINCE_CONSTANTS["POP_REQUIREMENTS"][pop_req]:
                #self.size = pop_req

        #self.build_points_total = bonuses.PROVINCE_CONSTANTS["POP_BUILD_POINTS"][self.size]
        #self.build_points_current = self.build_points_total
    
    #Adds a building to the buildings dictionary
    def constructBuilding(self, building_name):
        pass

    def destroyBuilding(self):
        pass
    
    #Adds to the population of the province
    def addPopulation(self, population):
        for specie in population:
            self.population[specie]["LOWER_CLASS"]["CHILDREN"] += self.population[specie]["LOWER_CLASS"]["CHILDREN"]
            self.population[specie]["LOWER_CLASS"]["ADULT"] += population[specie]["LOWER_CLASS"]["ADULT"]
            self.population[specie]["MIDDLE_CLASS"]["CHILDREN"] += population[specie]["MIDDLE_CLASS"]["CHILDREN"]
            self.population[specie]["MIDDLE_CLASS"]["ADULT"] += population[specie]["MIDDLE_CLASS"]["ADULT"]
            self.population[specie]["UPPER_CLASS"]["CHILDREN"] += population[specie]["UPPER_CLASS"]["CHILDREN"]
            self.population[specie]["UPPER_CLASS"]["ADULT"] += population[specie]["UPPER_CLASS"]["ADULT"]
            self.updatePopulations(population)

    #Removes the population of the province 
    def subtractPopulation(self, population): 
        tmp_population = self.population

        for specie in population:
            self.population[specie]["LOWER_CLASS"]["CHILDREN"] -= population[specie]["LOWER_CLASS"]["CHILDREN"] 
            self.population[specie]["LOWER_CLASS"]["ADULT"] -= population[specie]["LOWER_CLASS"]["ADULT"]
            self.population[specie]["MIDDLE_CLASS"]["CHILDREN"] -= population[specie]["MIDDLE_CLASS"]["CHILDREN"]
            self.population[specie]["MIDDLE_CLASS"]["ADULT"] -= population[specie]["MIDDLE_CLASS"]["ADULT"]
            self.population[specie]["UPPER_CLASS"]["CHILDREN"] -= population[specie]["UPPER_CLASS"]["CHILDREN"]
            self.population[specie]["UPPER_CLASS"]["ADULT"] -= population[specie]["UPPER_CLASS"]["ADULT"]
            
            tmp_population[specie]["LOWER_CLASS"]["CHILDREN"] = self.population[specie]["LOWER_CLASS"]["CHILDREN"] * -1
            tmp_population[specie]["LOWER_CLASS"]["ADULT"] = self.population[specie]["LOWER_CLASS"]["ADULT"] * -1
            tmp_population[specie]["MIDDLE_CLASS"]["CHILDREN"] = self.population[specie]["MIDDLE_CLASS"]["CHILDREN"] * -1
            tmp_population[specie]["MIDDLE_CLASS"]["ADULT"] = self.population[specie]["MIDDLE_CLASS"]["ADULT"] * -1
            tmp_population[specie]["UPPER_CLASS"]["CHILDREN"] = self.population[specie]["UPPER_CLASS"]["CHILDREN"] * -1
            tmp_population[specie]["UPPER_CLASS"]["ADULT"] = self.population[specie]["UPPER_CLASS"]["ADULT"] * -1

        self.updatePopulations(tmp_population)

    #Updates the sub-populations based on the main population. It also updates the build points, province size, and primary and secondary populations of the population
    def updatePopulations(self, population):
        for specie in self.population:
            self.population_specie[specie] = 0
            for eco_status in self.population[specie]:
                self.population_workers[eco_status] += self.population[specie][eco_status]["ADULT"]
                for age in self.population[specie][eco_status]:
                    self.population_total += population[specie][eco_status][age]
                    self.population_specie[specie] += population[specie][eco_status][age]

        #Calculates the primary and secondary specie of the province
        for specie in self.population_specie:
            if self.population_specie[specie] > self.population_specie[self.primary_specie]:
                
                #Moves the previous primary species down to the secondary specie
                self.secondary_specie = self.primary_specie
                self.primary_specie = specie
        
        #Determines what size the province is
        for pop_req in bonuses.PROVINCE_CONSTANTS["POP_REQUIREMENTS"]:
            if self.population_total > bonuses.PROVINCE_CONSTANTS["POP_REQUIREMENTS"][pop_req]:
                self.size = pop_req
        
        used_build_points = self.build_points_total - self.build_points_current

        self.build_points_total = bonuses.PROVINCE_CONSTANTS["POP_BUILD_POINTS"][self.size]
        self.build_points_current = self.build_points_total - self.build_points_current


    #A function to check if the province has the requisuite amount of build points and population requirements to construct
    def checkBuilding(self, building_name):
        
        name_found = False
        #Checks if the building name exists
        for name in bonuses.BUILDINGS:
            if name == building_name:
                name_found = True

        if name_found == False:
            return False

        try:
            if bonuses.BUILDINGS[building_name]["MATERIALS"]["BUILD_POINT"] > self.build_points_current:
                return False
        except KeyError: # If there is no Build Point entry, this means that the Building has no build point requirement
            pass
        
        max_building = bonuses.BUILDINGS[building_name]["POPULATION"][self.size]

        cond1 = max_building == -1 # If the max_building is equal to -1, it means the building can be built an infinite amount of times
        cond2 = max_building >= self.buildings[building_name] #MIGHT NEED TO CHANGE LATER

        if cond1 or cond2:
            return True
        else:
            return False

    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Population: {self.population_total}")
        
        for specie in self.population_specie:
            print(f"{specie} {self.population_specie[specie]}")
        
        for workers in self.population_workers:
            print(f"{workers} {self.population_workers[workers]}")

        print(self.primary_specie, self.secondary_specie)
        print(self.size, self.build_points_total)
    

if __name__ == "__main__":
    #TEST POPULATION
    example_population = {
        "HUMANS" : {
            "LOWER_CLASS" : {
                "CHILDREN" : 500,
                "ADULT" : 1000
                },
            "MIDDLE_CLASS" : {
                "CHILDREN" : 300,
                "ADULT" : 600
                },
            "UPPER_CLASS" : {
                "CHILDREN" : 50,
                "ADULT" : 100
                }
            },

        "ELVES" : {
            "LOWER_CLASS" : {
                "CHILDREN" : 1000,
                "ADULT" : 2000
                },
            "MIDDLE_CLASS" : {
                "CHILDREN" : 600,
                "ADULT" : 1200
                },
            "UPPER_CLASS" : {
                "CHILDREN" : 100,
                "ADULT" : 200
                }
            },
 
        "DWARVES" : {
            "LOWER_CLASS" : {
                "CHILDREN" : 2000,
                "ADULT" : 4000
                },
            "MIDDLE_CLASS" : {
                "CHILDREN" : 1200,
                "ADULT" : 2400
                },
            "UPPER_CLASS" : {
                "CHILDREN" : 200,
                "ADULT" : 400
                }
            },

        "HALF_ELVES" : {
            "LOWER_CLASS" : {
                "CHILDREN" : 4000,
                "ADULT" : 8000
                },
            "MIDDLE_CLASS" : {
                "CHILDREN" : 2400,
                "ADULT" : 4800
                },
            "UPPER_CLASS" : {
                "CHILDREN" : 400,
                "ADULT" : 800
                }
            }
        }
    
    print(PLAYER_CLASS_BONUSES)
    test_class = Province("test", example_population)
    test_class.printInfo()
