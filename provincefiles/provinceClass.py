# A file that contains the class definition for a province
#Imports the constants
import sys
import random
sys.path.append("..")

from constantfiles import bonuses

class Province:
    
    #The population variable is a dictionary in a dictionary in a dictionary
    def __init__(self, name, population, buildings, terrain):
        self.counter = 0
        self.size_acres = None
        self.name = name
        self.population = population
        self.buildings = buildings
        self.terrain = terrain
        self.terrain_bonuses = bonuses.TILES_CONSTANTS[terrain]
        #self.primary_resource = primary_resource
        self.stats = {
                "DEFENSE" : 0,
                "SATISFACTION_LOWER_CLASS" : 0,
                "SATISFACTION_MIDDLE_CLASS" : 0,
                "SATISFACTION_UPPER_CLASS" : 0,
                "PIETY" : {
                    "MAKOTHA" : 0,
                    "CYNTHI" : 0,
                    "BELSOYU" : 0,
                    "BROWDEN" : 0,
                    "GILGAMESH" : 0,
                    "NYANITI" : 0,
                    "SZETH" : 0,
                    "TIAMAT" : 0
                    },
                "OVERPOPULATED" : False,
                "HOUSES" : 0,
                "MILITARY_TRAINING" : 0,
                "MILITARY_ENTERTAINMENT" : False,
                "MILITARY_PRESENT" : False,
                "PRODUCTION_ADV" : 0,
                "ENTERTAINMENT_PRODUCTION" : 0,
                "LUMBER_PRODUCTION" : 0,
                "LIVESTOCK_PRODUCTION" : 0,
                "CROP_PRODUCTION" : 0,
                "WATER_PRODUCTION" : 0,
                "LUMBER_ADV" : False,
                "CROP_ADV" : False,
                "LIVESTOCK_ADV" : False,
                "MINERALS_ADV" : False,
                "WATER_ADV" : False,
                "TRADE_SPEED" : 0,
                "TRADE_PROFIT" : 0
                } 

        self.required_materials = {
                "CONSTRUCTION_WORKERS" : 0,
                "WATER" : 0,
                "LUMBER" : 0,
                "LIVESTOCK" : 0,
                "MINERLAS" : 0,
                "CROPS" : 0
                }
    

        self.under_construction = {
                "POP_HOUSING" : 0,
                "CHAPEL" : 0,
                "TEMPLE" : 0,
                "MONASTERY" : 0,
                "GARRISON" : 0,
                "TOWER" : 0,
                "TRAINING_CAMP" : 0,
                "KEEP" : 0,
                "CASTLE" : 0,
                "BAR" : 0,
                "PALACE" : 0,
                "SHOWPLACE" : 0,
                "THEATRE" : 0,
                "COLOSSEUM" : 0,
                "CRADLE_OF_GODS" : 0
                }

        self.under_construction_list = {}
        self.upkeep = {
                "WORKERS" : 0,
                "WATER" : 0,
                "LUMBER" : 0,
                "LIVESTOCK" : 0,
                "MINERALS" : 0,
                "CROPS" : 0
                }
        self.acres = {
                "CROPS" : {
                    "ACRES" : 0,
                    "BONUS" : 0,
                    },
                "WATER" : {
                    "ACRES" : 0,
                    "BONUS" : 0,
                    },
                "LIVESTOCK" : {
                    "ACRES" : 0,
                    "BONUS" : 0,
                    },
                "ENTERTAINMENT" : {
                    "ACRES" : 0,
                    "BONUS" : 0,
                    },
                "MINERALS" : {
                    "ACRES" : 0,
                    "BONUS" : 0,
                    },
                "LUMBER" : {
                    "ACRES" : 0,
                    "BONUS" : 0,
                    }
                }
        self.population_total = 0
        self.population_specie = {}
        self.population_workers = {
                "LOWER_CLASS" : 0,
                "MIDDLE_CLASS" : 0,
                "UPPER_CLASS" : 0
                }
        self.used_workers = {
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
        
        #Calculates acreage
        self.createAcreage()

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
    
    #Adds a building to the building queue
    def constructBuilding(self, building_name, workers):
        assert self.checkBuilding(building_name) #Validates building is legal
        
        #Validates if the amount of workers can be construct the building in a whole number of seasons
        workers_per_season = (bonuses.BUILDINGS[building_name]["CONSTRUCTION"]["WORKERS"] * bonuses.BUILDINGS[building_name]["CONSTRUCTION"]["SEASONS"]) / workers
        construction_time = int(workers_per_season)
        cond1 = construction_time == workers_per_season
        cond2 = construction_time <= bonuses.BUILDINGS[building_name]["CONSTRUCTION"]["WORKERS"]
        if cond1 and cond2:
            pass
        else:
            #print(construction_time)
            raise ArithmeticError

        #self.buildings[building_name] += 1
        self.build_points_current -= bonuses.BUILDINGS[building_name]["MATERIALS"]["BUILD_POINTS"] 
        
        #Adds the building to the building queue, and adds a number to it to differentiate it from other buildings of the same type being constructed
        entry = building_name + "_" + str(self.under_construction[building_name])
        self.under_construction[building_name] += 1 #Increments the amount of this type of building being built
        self.under_construction_list[entry] = {
                "BUILDING_TYPE" : building_name,
                "WORKERS" : workers,
                "SEASONS_LEFT" : construction_time,
                "BUILDING?" : True
                }
        self.upkeep["WORKERS"] += workers

    #Any buildings that have finished constructing are added to the building list
    def addBuildings(self):
        buildings_completed = []
        for building in self.under_construction_list:
            if self.under_construction_list[building]["SEASONS_LEFT"] == 0: #Zero in SEASONS_LEFT means the building has completed construction
                building_name = self.under_construction_list[building]["BUILDING_TYPE"]
                self.buildings[building_name] += 1
                self.under_construction[building_name] -= 1
                buildings_completed.append(building)
                #self.under_construction_list.pop(building)
        
        #Removes completed buildings from the under construction list
        for completed_buildings in buildings_completed:
            self.under_construction_list.pop(completed_buildings)


    #Removes a building from the buildings already constructed
    def destroyBuilding(self, building_name):
        #Makes sure there is at least one building to destroy
        if self.buildings[building_name] == 0:
            raise ValueError
        self.buildings[building_name] -= 1
   
    #Updates the population when they grow
    def growPopulation(self):
        new_population = {} 
        #print(self.population) 
        for specie in self.population:
            new_population[specie] = {} #Need to initialize dictionaries for each level of the key
            for eco_status in self.population[specie]:
                new_population[specie][eco_status] = {}
                current_pop_adult = self.population[specie][eco_status]["ADULT"]
                current_pop_children = self.population[specie][eco_status]["CHILDREN"]
                new_kids = int(current_pop_adult * bonuses.SPECIES_POP[specie]["REPRODUCTION_RATE"]) 
                new_adults = int(current_pop_children * bonuses.SPECIES_POP[specie]["GROWTH_RATE"])
                dead_adults = int(current_pop_adult * bonuses.SPECIES_POP[specie]["DEATH_RATE"])
                new_population[specie][eco_status]["CHILDREN"] = new_kids - new_adults
                new_population[specie][eco_status]["ADULT"] = new_adults - dead_adults
        #print(new_population)
        #print(self.population)
        self.addPopulation(new_population)

    #Adds to the population of the province
    def addPopulation(self, population):
        for specie in population:
            #print(specie)
            self.population[specie]["LOWER_CLASS"]["CHILDREN"] += population[specie]["LOWER_CLASS"]["CHILDREN"]
            self.population[specie]["LOWER_CLASS"]["ADULT"] += population[specie]["LOWER_CLASS"]["ADULT"]
            self.population[specie]["MIDDLE_CLASS"]["CHILDREN"] += population[specie]["MIDDLE_CLASS"]["CHILDREN"]
            self.population[specie]["MIDDLE_CLASS"]["ADULT"] += population[specie]["MIDDLE_CLASS"]["ADULT"]
            self.population[specie]["UPPER_CLASS"]["CHILDREN"] += population[specie]["UPPER_CLASS"]["CHILDREN"]
            self.population[specie]["UPPER_CLASS"]["ADULT"] += population[specie]["UPPER_CLASS"]["ADULT"]
        
        #print(population)
        self.updatePopulations(self.population)

    #Removes the population of the province 
    def subtractPopulation(self, population): 
        #tmp_population = self.population

        for specie in population:
            #print(self.population[specie]["LOWER_CLASS"]["CHILDREN"], population[specie]["LOWER_CLASS"]["CHILDREN"])
            self.population[specie]["LOWER_CLASS"]["CHILDREN"] -= population[specie]["LOWER_CLASS"]["CHILDREN"] 
            self.population[specie]["LOWER_CLASS"]["ADULT"] -= population[specie]["LOWER_CLASS"]["ADULT"]
            self.population[specie]["MIDDLE_CLASS"]["CHILDREN"] -= population[specie]["MIDDLE_CLASS"]["CHILDREN"]
            self.population[specie]["MIDDLE_CLASS"]["ADULT"] -= population[specie]["MIDDLE_CLASS"]["ADULT"]
            self.population[specie]["UPPER_CLASS"]["CHILDREN"] -= population[specie]["UPPER_CLASS"]["CHILDREN"]
            self.population[specie]["UPPER_CLASS"]["ADULT"] -= population[specie]["UPPER_CLASS"]["ADULT"]
            #print(self.population[specie]["LOWER_CLASS"]["CHILDREN"]) 
            #tmp_population[specie]["LOWER_CLASS"]["CHILDREN"] = self.population[specie]["LOWER_CLASS"]["CHILDREN"] * -1
            #tmp_population[specie]["LOWER_CLASS"]["ADULT"] = self.population[specie]["LOWER_CLASS"]["ADULT"] * -1
            #tmp_population[specie]["MIDDLE_CLASS"]["CHILDREN"] = self.population[specie]["MIDDLE_CLASS"]["CHILDREN"] * -1
            #tmp_population[specie]["MIDDLE_CLASS"]["ADULT"] = self.population[specie]["MIDDLE_CLASS"]["ADULT"] * -1
            #tmp_population[specie]["UPPER_CLASS"]["CHILDREN"] = self.population[specie]["UPPER_CLASS"]["CHILDREN"] * -1
            #tmp_population[specie]["UPPER_CLASS"]["ADULT"] = self.population[specie]["UPPER_CLASS"]["ADULT"] * -1
        
        self.updatePopulations(self.population)
        
    #Updates the sub-populations based on the main population. It does this by recalculating all sub-populations from the main population
    #It also updates the build points, province size, and primary and secondary populations of the population
    def updatePopulations(self, population):
        #print(population["HUMANS"]["LOWER_CLASS"]["CHILDREN"])        
        #Tmp variable so if the reduction is bigger than the current population, it won't change only half the population
        #tmp_pop = {}
        tmp_pop_total = 0
        tmp_pop_specie = {}
        tmp_pop_worker = {
                "LOWER_CLASS" : 0,
                "MIDDLE_CLASS" : 0,
                "UPPER_CLASS" : 0
                }

        #Resets all the population totals
       # self.population_total = 0
        #for specie in self.population:
           # self.population_specie[specie] = 0
        #for eco_status in self.population_workers:
          #  self.population_workers[eco_status] = 0
        #print(self.population)
        #print(population) 
        for specie in population:
            tmp_pop_specie[specie] = 0
            #print(specie)
            for eco_status in population[specie]:
                #self.population_workers[eco_status] += self.population[specie][eco_status]["ADULT"]
                tmp_pop_worker[eco_status] += population[specie][eco_status]["ADULT"]
                for age in population[specie][eco_status]:
                    #print(population[specie][eco_status][age])
                    tmp_pop_total += population[specie][eco_status][age]
                    #print(tmp_pop_specie[specie])
                    tmp_pop_specie[specie] += population[specie][eco_status][age]
                    #self.population_total += population[specie][eco_status][age]
                    #self.population_specie[specie] += population[specie][eco_status][age]
                    
                    #print(specie, tmp_pop_specie)

                    #Makes sure the population will not become negative
                    cond1 = tmp_pop_total < 0
                    cond2 = tmp_pop_specie[specie] < 0
                    cond3 = tmp_pop_worker[eco_status] < 0
                    if cond1 or cond2 or cond3:
                        print(eco_status, cond1, cond2, cond3)
                        raise ArithmeticError
        
        self.population_total = tmp_pop_total
        self.population_specie = tmp_pop_specie
        self.population_workers = tmp_pop_worker

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

    #Updates the statistics of the province
    def updateStats(self):
        pass
    
    #Assigns workers to resources with validation
    def assignWorkers(self, assignment):
        pass

    #Updates the acreage of the province by keeping the acres percentage roughly the same
    def updateAcreage(self):
        if self.size != self.size_acres:
            
            acres_more_percent = random.randint(1, bonuses.ACRES_RANDOM_MAX) / 100
            new_total_acres = (bonuses.PROVINCE_CONSTANTS["ACRES_BASE"][self.size])
            new_total_acres += (bonuses.PROVINCE_CONSTANTS["ACRES_BASE"][self.size] * acres_more_percent)
            new_total_acres = int(new_total_acres)
            total_acres_left = new_total_acres            
            for resource in self.acres:
                #print(self.acres[resource])
                percent_allocated = self.acres[resource]["ACRES"] / self.total_acres
                acres_allocated = int(new_total_acres * percent_allocated)
                total_acres_left -= acres_allocated
                self.acres[resource]["ACRES"] = acres_allocated
            
            self.acres[self.terrain_bonuses["PRIMARY_RESOURCE"]]["ACRES"] += total_acres_left
            self.total_acres = new_total_acres
            self.size_acres = self.size

    #Creates acreage at initlization, with a bit of randomness
    def createAcreage(self):
        acres_more_percent = random.randint(1, bonuses.ACRES_RANDOM_MAX) / 100
        self.total_acres = (bonuses.PROVINCE_CONSTANTS["ACRES_BASE"][self.size])
        self.total_acres += (bonuses.PROVINCE_CONSTANTS["ACRES_BASE"][self.size] * acres_more_percent)
        self.total_acres = int(self.total_acres)
        total_acres_left = self.total_acres
            
        total_percent_left = 1 - bonuses.PRIMARY_RESOURCE_BONUS - bonuses.SECONDARY_RESOURCE_BONUS
        percent_allocated = {
                "CROPS" : 0,
                "MINERALS" : 0,
                "WATER" : 0,
                "LIVESTOCK" : 0,
                "LUMBER" : 0,
                "ENTERTAINMENT" : 0
                }
        percent_allocated[self.terrain_bonuses["PRIMARY_RESOURCE"]] += bonuses.PRIMARY_RESOURCE_BONUS
        percent_allocated[self.terrain_bonuses["SECONDARY_RESOURCE"]] += bonuses.SECONDARY_RESOURCE_BONUS

        #Chooses a random resource to start increasing the percent of acres allocated to those resources, then loops through the all the resources, increasing the percent of acres allocated a little bit at a time
        skiped = random.randint(0,5) #It is 0 to 5 so each resource will be skipped only one time
        while total_percent_left != 0:
           for resource in self.acres:
                if skiped != 0:
                    skiped -= 1
                    
                else:
                    percent_added = random.randint(1,2) / 100.0 #The number 2 is an arbitrary number, it could be any single digit number
                    percent_allocated[resource] += percent_added
                    total_percent_left -= percent_added
                        
                    #Checks if the total percent of acres allocated is over 100%
                    if total_percent_left < 0:
                        percent_allocated[resource] += total_percent_left
                        total_percent_left = 0

        #Allocates the acres, then determines their bonus
        for resource in self.acres:
            acres_allocated = int(self.total_acres * percent_allocated[resource])
            #print(percent_allocated[resource])
            self.acres[resource]["ACRES"] = acres_allocated
            total_acres_left -= acres_allocated

            self.acres[resource]["BONUS"] = bonuses.BASE_BONUS_RESOURCE - random.randint(1,4)

        #Adds/Subtract any leftover acres to the primary resource
        self.acres[self.terrain_bonuses["PRIMARY_RESOURCE"]]["ACRES"] += int(total_acres_left)
        
        #Sets the primary resource to a standardize bonus
        self.acres[self.terrain_bonuses["PRIMARY_RESOURCE"]]["BONUS"] = bonuses.PRIMARY_RESOURCE_BONUS_MOD
        self.acres[self.terrain_bonuses["SECONDARY_RESOURCE"]]["BONUS"] = bonuses.SECONDARY_RESOURCE_BONUS_MOD

    #A function to check if the province has the requisuite amount of build points and population requirements to construct
    def checkBuilding(self, building_name):
        
        name_found = False
        #Checks if the building name exists
        for name in bonuses.BUILDINGS:
            if name == building_name:
                name_found = True

        if name_found == False:
            raise KeyError

        #try:
        if bonuses.BUILDINGS[building_name]["MATERIALS"]["BUILD_POINTS"] > self.build_points_current:
            return False
        #except KeyError: # If there is no Build Point entry, this means that the Building has no build point requirement
            #pass
        
        max_building = bonuses.BUILDINGS[building_name]["POPULATION"][self.size]

        cond1 = max_building == -1 # If the max_building is equal to -1, it means the building can be built an infinite amount of times
        cond2 = max_building >= self.buildings[building_name] + self.under_construction[building_name] #MIGHT NEED TO CHANGE LATER

        if cond1 or cond2:
            return True
        else:
            return False
    
    #Progresses a season and returns how much money was made
    def progressSeason(self):
        
        self.growPopulation()
        self.updateAcreage()

        #Reduces the time on all currently constructing buildings by 1 season
        for construction in self.under_construction_list:
            if self.under_construction_list[construction]["BUILDING?"]:
                self.under_construction_list[construction]["SEASONS_LEFT"] -= 1

        self.addBuildings()

    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Population: {self.population_total}")
        print("--------------------------------------------")
        
        print(f"Total Acres {self.total_acres}")
        for resource in self.acres:
            print(f"{resource} {self.acres[resource]}")

        print("--------------------------------------------")
        
        for specie in self.population_specie:
            print(f"{specie} {self.population_specie[specie]}")
        
        print("--------------------------------------------")
        
        for workers in self.population_workers:
            print(f"{workers} {self.population_workers[workers]}")
        
        print("--------------------------------------------")
        print("Buildings Built:")
        for building in self.buildings:
            print(f"{building} {self.buildings[building]}")
        
        print("--------------------------------------------") 

        for constructions in self.under_construction_list:
            print(f"{constructions} {self.under_construction_list[constructions]}")

        print("--------------------------------------------")
        print("Buildings Under Construction") 
        for building in self.under_construction:
            print(f"{building} {self.under_construction[building]}")

        print("--------------------------------------------")
        print(self.primary_specie, self.secondary_specie)
        print("--------------------------------------------")
        print(self.size, self.build_points_total)
        print("--------------------------------------------")
        print("--------------------------------------------")
        

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
