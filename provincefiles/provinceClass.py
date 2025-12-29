# A file that contains the class definition for a province

#import bonuses

class Province:
    
    #The population variable is a dictionary in a dictionary in a dictionary

    def __init__(self, name, population):
        self.name = name
        self.population = population

        self.population_total = 0
        self.population_specie = {}
        self.population_workers = {
                "LOWER_CLASS" : 0,
                "MIDDLE_CLASS" : 0,
                "UPPER_CLASS" : 0
                }

        # Calculates what size the province is
        # Also calculates other populations totals that are useful
        for specie in self.population:
            self.population_specie[specie] = 0
            for eco_status in self.population[specie]:
                self.population_workers[eco_status] += self.population[specie][eco_status]["ADULT"]
                for age in self.population[specie][eco_status]:
                    self.population_total += population[specie][eco_status][age]
                    self.population_specie[specie] += population[specie][eco_status][age]
        
        

        #Calculates the primary and secondary specie of the province
        self.primary_specie = "HUMANS"
        self.secondary_specie = "HUMANS"

        for specie in self.population_specie:
            if self.population_specie[specie] > self.population_specie[self.primary_specie]:
                
                #Moves the previous primary species down to the secondary specie
                self.secondary_specie = self.primary_specie
                self.primary_specie = specie

    def constructBuilding():
        pass
    
    def destroyBuilding():
        pass

    def addPopulation(population):
        pass

    def subtractPopulation():
        pass
    
    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Population: {self.population_total}")
        
        for specie in self.population_specie:
            print(f"{specie} {self.population_specie[specie]}")
        
        for workers in self.population_workers:
            print(f"{workers} {self.population_workers[workers]}")

        print(self.primary_specie, self.secondary_specie)
    

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

    test_class = Province("test", example_population)
    test_class.printInfo()
