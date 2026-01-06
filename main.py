from provincefiles import provinceClass
 
def testPop():
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
            }
        }

    #TEST BUILDING
    example_building = {
            "POP_HOUSING" : 0,
            "CHAPEL" : 0,
            "TEMPLE" : 7,
            "MONASTERY" : 0,
            "GARRISON" : 0,
            "TOWER" : 0,
            "TRAINING CAMP" : 0,
            "KEEP" : 0,
            "CASTLE" : 0,
            "BAR" : 0,
            "PALACE" : 0,
            "SHOWPLACE" : 0,
            "THEATRE" : 0,
            "COLOSSEUM" : 0,
            "CRADLE_OF_GODS" : 0
            }
    
    pop = {
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
            }
        }

    test_class = provinceClass.Province("test", example_population, example_building)
    test_class.constructBuilding("POP_HOUSING", 250)
    test_class.printInfo()
    test_class.progressSeason()
    test_class.printInfo()

if __name__ == "__main__":
    testPop()
