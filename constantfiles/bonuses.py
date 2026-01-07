# This file stores all the constants for the program
HAMLET_POP = 0
VILLAGE_POP = 501
SETTLEMENT_POP = 1001
SMALL_TOWN_POP = 2001
LARGE_TOWN_POP = 5001
SMALL_CITY_POP = 15001
MEDIUM_CITY_POP = 40001
LARGE_CITY_POP = 100001
MEGALOPOLIS_POP = 200001

PLAYER_CLASS_BONUSES = {
        "ARTIFICER" : {
          "BONUSES" : {
            "INDEPTH" : [
              "DEFENSE",
              "SATISFACTION"
              ],
            "INATE" : []
            },
          "INATE" : {
            "SATISFACTION_LOWER_CLASS" : 0,
            "SATISFACTION_MIDDLE_CLASS" : 0,
            "SATISFACTION_UPPER_CLASS" : 0,
            "ENTERTAINMENT_PRODUCTION" : 0,
            "LUMBER_PRODUCTION" : 0,
            "LIVESTOCK_PRODUCTION" : 0,
            "CROP_PRODUCTION" : 0,
            "WATER_PRODUCTION" : 0,
            "PIETY_SPECIFIC" : 0,
            "PIETY_GENERAL" : 0,
            "DEFENSE" : 0,
            "MILITARY_TRAINING" : 0,
            "TRADE_SPEED" : 0,
            "TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            "DEFENSE" : 1,
            "SATISFACTION" : 1,
            "LUMBER_ADV" : False,
            "CROP_ADV" : False,
            "LIVESTOCK_ADV" : False,
            "MINERALS_ADV" : False,
            "WATER_ADV" : False,
            "PRODUCTION_ADV" : False
          }
        },

        "Barbarian" : {
          "BONUSES" : {
            "INDEPTH" : [
              "DEFENSE",
              "LUMBER_ADV"
              ],
            "INATE" : [
              "SATISFACTION_LOWER_CLASS"
              ]
            },
          "INATE" : {
            "SATISFACTION_LOWER_CLASS" : 4,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            "DEFENSE" : 1,
            #"SATISFACTION" : 0,
            "LUMBER_ADV" : True,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "BARD" : {
          "BONUSES" : {
            "INDEPTH" : [
              "SATISFACTION"
              ],
            "INATE" : [
              "ENTERTAINMENT_PRODUCTION"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            "ENTERTAINMENT_PRODUCTION" : .25,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            #"DEFENSE" : 0,
            "SATISFACTION" : 2,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "CLERIC" : { 
        "BONUSES" : {
          "INDEPTH" : [
            "SATISFACTION"
            ],
          "INATE" : [
            "PIETY_SPECIFIC"
            ]
          },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            "PIETY_SPECIFIC" : 2,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            #"DEFENSE" : 0,
            "SATISFACTION" : 2,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },
        
        "DRUID" : {
          "BONUSES" : {
            "INDEPTH" : [
              "LUMBER_PRODUCTION",
              "LIVESTOCK_PRODUCTION",
              "CROP_PRODUCTION",
              "WATER_PRODUCTION"
              ],
            "INATE" : [
              "LUMBER_ADV",
              "CROP_ADV"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            "LUMBER_PRODUCTION" : 0.1,
            "LIVESTOCK_PRODUCTION" : 0.1,
            "CROP_PRODUCTION" : 0.1,
            "WATER_PRODUCTION" : 0.1,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            #"DEFENSE" : 0,
            #"SATISFACTION" : 0,
            "LUMBER_ADV" : True,
            "CROP_ADV" : True,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "FIGHTER" : {
          "BONUSES" : {
            "INDEPTH" : [
              "DEFENSE"
              ],
            "INATE" : [
              "DEFENSE",
              "MILITARY_TRAINING"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            "DEFENSE" : 1,
            "MILITARY_TRAINING" : 1,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            "DEFENSE" : 3,
            #"SATISFACTION" : 0,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "MONK" : {
          "BONUSES" : {
            "INDEPTH" : [
              "DEFENSE",
              "SATISFACTION"
              ],
            "INATE" : [
              "PIETY_SPECIFIC",
              "PIETY_GENERAL"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            "PIETY_SPECIFIC" : 2,
            "PIETY_GENERAL" : 1,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            "DEFENSE" : 1,
            "SATISFACTION" : 1,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "PALADIN" : {
          "BONUSES" : {
            "INDEPTH" : [
              "DEFENSE",
              "SATISFACTION"
              ],
            "INATE" : [
              "PIETY_SPECIFIC",
              "PIETY_GENERAL"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            "PIETY_SPECIFIC" : 2,
            "PIETY_GENERAL" : 1,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            "DEFENSE" : 1,
            "SATISFACTION" : 1,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "RANGER" : {
          "BONUSES" : {
            "INDEPTH" : [
              "DEFENSE",
              "LIVESTOCK_ADV"
              ],
            "INATE" : [
              "TRADE_SPEED"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            "TRADE_SPEED" : 0.2,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            "DEFENSE" : 1,
            #"SATISFACTION" : 0,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            "LIVESTOCK_ADV" : True,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "ROGUE" : {
          "BONUSES" : {
            "INDEPTH" : [
              "SATISFACTION"
              ],
            "INATE" : [
              "TRADE_PROFIT"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            "TRADE_PROFIT" : 0.1
          },
              
          "INDEPTH" : {
            #"DEFENSE" : 0,
            "SATISFACTION" : 2,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "SORCERER" : {
          "BONUSES" : {
            "INDEPTH" : [
              "SATISFACTION"
              ],
            "INATE" : [
              "SATISFACTION_UPPER_CLASS"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            "SATISFACTION_UPPER_CLASS" : 4,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            #"DEFENSE" : 0,
            "SATISFACTION" : 1,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "WARLOCK" : {
          "BONUSES" : {
            "INDEPTH" : [
              "MINERALS_ADV",
              "WATER_ADV"
              ],
            "INATE" : [
              "SATISFACTION_MIDDLE_CLASS"
              ]
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            "SATISFACTION_MIDDLE_CLASS" : 4,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            #"DEFENSE" : 0,
            #"SATISFACTION" : 0,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            "MINERALS_ADV" : True,
            "WATER_ADV" : True,
            #"PRODUCTION_ADV" : False
          }
        },

        "WIZARD" : {
          "BONUSES" : {
            "INDEPTH" : [
              "PRODUCTION_ADV"
              ],
            "INATE" : []
            },
          "INATE" : {
            #"SATISFACTION_LOWER_CLASS" : 0,
            #"SATISFACTION_MIDDLE_CLASS" : 0,
            #"SATISFACTION_UPPER_CLASS" : 0,
            #"ENTERTAINMENT_PRODUCTION" : 0,
            #"LUMBER_PRODUCTION" : 0,
            #"LIVESTOCK_PRODUCTION" : 0,
            #"CROP_PRODUCTION" : 0,
            #"WATER_PRODUCTION" : 0,
            #"PIETY_SPECIFIC" : 0,
            #"PIETY_GENERAL" : 0,
            #"DEFENSE" : 0,
            #"MILITARY_TRAINING" : 0,
            #"TRADE_SPEED" : 0,
            #"TRADE_PROFIT" : 0
          },
              
          "INDEPTH" : {
            #"DEFENSE" : 0,
            #"SATISFACTION" : 0,
            #"LUMBER_ADV" : False,
            #"CROP_ADV" : False,
            #"LIVESTOCK_ADV" : False,
            #"MINERALS_ADV" : False,
            #"WATER_ADV" : False,
            "PRODUCTION_ADV" : 1
          }
        }
    }

SPECIES_BONUSES = {
 "HUMANSS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : [
      "PRODUCTION_ADV"
      ],
    "SECONDARY_BONUS" : [],
    "COMBAT_BONUS" : [
      "MILITARY_TRAINING_NOT_FIRST",
      "XP_REDUCTION"
      ]
    },

  "BONUS_VALUES" : {
    "PRODUCTION_ADV" : 1,
    "MILITARY_TRAINING_NOT_FIRST" : 1,
    "XP_REDUCTION" : 1
    }
  },

 "ELVES" : {
  "BONUSES" : {
      "PRIMARY_BONUS" : [
        "LIVESTOCK_PRODUCTION_PRIME", 
        "LUMBER_PRODUCTION_PRIME"
        ],
    "SECONDARY_BONUS" : [
        "LIVESTOCK_PRODUCTION_SEC", 
        "LUMBER_PRODUCTION_SEC"
        ],
    "COMBAT_BONUS" : []
    },

  "BONUS_VALUES" : {
    "LIVESTOCK_PRODCUTION_PRIME" : .1,
    "LUMER_PRODUCTION_PRIME" : .1,
    "LIVESTOCK_PRODUCTION_SEC" : .05,
    "LUMBER_PRODUCTION_SEC" : .05
    }
  },

 "DWARVES" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : [
      "MINERALS_PRODUCTION"
      ],
    "SECONDARY_BONUS" : [
      "MINERALS_ADV"
      ],
    "COMBAT_BONUS" : [
      "DEFENSE"
      ]
    },

  "BONUS_VALUES" : {
    "MINERALS_PRODUCTION" : .2,
    "MINERALS_ADV" : True,
    "DEFENSE" : 1
    }
  },

 "HALFLINGS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : [
        "ENTERTAINMENT_PRODUCTION",
        "CROP_PRODUCTION",
        "LIVESTOCK_PRODUCTION",
        "LUMBER_PRODUCTION",
        "MINERALSS_PRODUCTION",
        "WATER_PRODUCTION"
        ],
    "SECONDARY_BONUS" : [
        "ENTERTAINMENT_PRODUCTION"
        ],
    "COMBAT_BONUS" : []
    },

  "BONUS_VALUES" : {
    "ENTERTAINMENT_PRODUCTION" : .1,
    "CROP_PRODUCTION" : .05,
    "LIVESTOCK_PRODUCTION" : .05,
    "LUMBER_PRODUCTION" : .05,
    "MINERALSS_PRODUCTION" : .05,
    "WATER_PRODUCTION" : .05  
    }
  },

 "GNOMES" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : [
        "TRADE_BONUS_PRIME"
        ],
    "SECONDARY_BONUS" : [
        "TRADE_BONUS_SEC"
        ],
    "COMBAT_BONUS" : []
    },

  "BONUS_VALUES" : {
    "TRADE_BONUS_PRIME" : .1,
    "TRADE_BONUS_SEC" : .05
    }
  },

 "DRAGONBORN" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : [
        "DEFENSE_PRIME"
        ],
    "SECONDARY_BONUS" : [
        "DEFENSE_SEC"
        ],
    "COMBAT_BONUS" : [
      "ATTACK"
      ]
    },

  "BONUS_VALUES" : {
    "DEFENSE_PRIME" : 2,
    "DEFENSE_SEC" : 1,
    "ATTACK" : 1
    }
  },

 "HALF_ELVES" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : [
        "PRODUCTION_PRODUCTION_PRIME"
        ],
    "SECONDARY_BONUS" : [
        "PRODUCTION_PRODUCTION_SEC"
        ],
    "COMBAT_BONUS" : []
    },

  "BONUS_VALUES" : {
    "PRODUCTION_PRODUCTION_PRIME" : .1,
    "PRODUCTION_PRODUCTION_PRIME" : .05
    }
  },

 "TIEFLINGS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : [
        "PIETY_PRIME",
        ],
    "SECONDARY_BONUS" : [
        "PIETY_SEC"
        ],
    "COMBAT_BONUS" : [
      "ATTACK"
      ]
    },

  "BONUS_VALUES" : {
    "PIETY_PRIME" : .1,
    "PIETY_SEC" : .05,
    "ATTACK" : 1
    }
  },

 "HALF_ORC" : {
  "BONUSES" : {
      "PRIMARY_BONUS" : [
        "MINERALS_PRODUCTION_PRIME", 
        "LUMBER_PRODUCTION_PRIME"
        ],
    "SECONDARY_BONUS" : [
        "MINERALS_PRODUCTION_SEC", 
        "LUMBER_PRODUCTION_SEC"
        ],
    "COMBAT_BONUS" : [
        "CASUALTY_REDUCTION"
        ]
    },

  "BONUS_VALUES" : {
      "MINERALS_PRODUCTION_PRIME" : .1, 
      "LUMBER_PRODUCTION_PRIME" : .1,
      "MINERALS_PRODUCTION_SEC": .05,
      "LUMBER_PRODUCTION_SEC" : .05,
      "CASUALTY_REDUCTION" : .2
    }
  }
}

SPECIES_POP = {
  "HUMANS" : {
    "GROWTH_RATE" : .05,
    "REPRODUCTION_RATE" : .12,
    "DEATH_RATE" : .05
    },
  
  "ELVES" : {
    "GROWTH_RATE" : .01,
    "REPRODUCTION_RATE" : .03,
    "DEATH_RATE" : .01
    },

  "DWARVES" : {
    "GROWTH_RATE" : .04,
    "REPRODUCTION_RATE" : .06,
    "DEATH_RATE" : .03
    },

  "HALFLINGS" : {
    "GROWTH_RATE" : .05,
    "REPRODUCTION_RATE" : .08,
    "DEATH_RATE" : .04
    },

  "GNOMES" : {
    "GROWTH_RATE" : .04,
    "REPRODUCTION_RATE" : .09,
    "DEATH_RATE" : .04
    },

  "DRAGONBORN" : {
    "GROWTH_RATE" : .13,
    "REPRODUCTION_RATE" : .09,
    "DEATH_RATE" : .06
    },

  "HALF_ELVES" : {
    "GROWTH_RATE" : .04,
    "REPRODUCTION_RATE" : .06,
    "DEATH_RATE" : .03
    },

  "TIEFLINGS" : {
    "GROWTH_RATE" : .05,
    "REPRODUCTION_RATE" : .11,
    "DEATH_RATE" : .05
    },

  "HALF_ORC" : {
    "GROWTH_RATE" : .17,
    "REPRODUCTION_RATE" : .11,
    "DEATH_RATE" : .08
    }
  }

RESOURCE_TAX = {
  "CROPS" : {
    "TAX_TYPES" : {
      "WORKERS" : [
        "LOWER"
      ],
        "SALES_TAX" : True
    },

    "TAX_AMOUNT" : {
      "LOWER" : 18,
      "LOWER_AMOUNT" : 12,
      "SAlES_TAX" : 2
      }
    },
  
  "LIVESTOCK" : {
    "TAX_TYPES" : {
      "WORKERS" : [
        "LOWER"
      ],
        "SALES_TAX" : True
    },

    "TAX_AMOUNT" : {
      "LOWER" : 15,
      "LOWER_AMOUNT" : 10,
      "SAlES_TAX" : 2
      }
    },
  "LUMBER" : {
    "TAX_TYPES" : {
      "WORKERS" : [
        "LOWER",
        "MIDDLE"
      ],
        "SALES_TAX" : True
    },

    "TAX_AMOUNT" : {
      "LOWER" : 10,
      "LOWER_AMOUNT" : 6,
      "MIDLE" : 8,
      "MIDDLE_AMOUNT" : 2,
      "SAlES_TAX" : 2
      }
    },

  "MINERALS" : {
    "TAX_TYPES" : {
      "WORKERS" : [
        "LOWER"
      ],
        "SALES_TAX" : True
    },

    "TAX_AMOUNT" : {
      "LOWER" : 25,
      "LOWER_AMOUNT" : 20,
      "SAlES_TAX" : 20
      }
    },

  "WATER" : {
    "TAX_TYPES" : {
      "WORKERS" : [
        "MIDDLE"
      ],
        "SALES_TAX" : True
    },

    "TAX_AMOUNT" : {
      "LOWER" : 25,
      "MIDDLE_AMOUNT" : 8,
      "SAlES_TAX" : 5
      }
    },

  "ENTERTAINMENT" : {
    "TAX_TYPES" : {
      "WORKERS" : [
        "MIDDLE",
        "UPPER"
      ],
        "SALES_TAX" : False
    },

    "TAX_AMOUNT" : {
      "MIDDLE" : 20,
      "MIDDLE_AMOUNT" : 8,
      "UPPER" : 15,
      "UPPER_AMOUNT" : 2
      }
    }
 }

BUILDINGS = {
 "POP_HOUSING" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "LUMBER",
       "BUILD_POINTS"
       ],
     "BUILD_POINTS" : 0,
     "LUMBER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     "HAMLET" : -1,
     "VILLAGE" : -1,
     "SETTLEMENT" : -1,
     "SMALL_TOWN" : -1,
     "LARGE_TOWN" : -1,
     "SMALL_CITY" : -1,
     "MEDIUM_CITY" : -1,
     "LARGE_CITY" : -1,
     "MEGALOPOLIS" : -1
   },
   
   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "HOUSES"
       ],
     "HOUSES" : 500
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "CROPS"
      ],
      "CROPS" : 10
   }
 },

 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "WATER",
       "MINERALS"
       ],
     "BUILD_POINT" : 1,
     "WATER" : 15,
     "MINERALS" : 30
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     "HAMLET" : 1,
     "VILLAGE" : 1,
     "SETTLEMENT" : 2,
     "SMALL_TOWN" : 4,
     "LARGE_TOWN" : 4,
     "SMALL_CITY" : 6,
     "MEDIUM_CITY" : 6,
     "LARGE_CITY" : 10,
     "MEGALOPOLIS" : 10
     #"HAMLET" : 1,
     #"SETTLEMENT" : 2,
     #"SMALL_TOWN" : 4,
     #"SMALL_CITY" : 6,
     #"LARGE_CITY" : 10,
     #11 : "MAX"
   },
   
   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "PIETY_SPECIFIC"
       ],
     "PIETY_SPECIFIC" : 1
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : []
   }
 },

 "TEMPLE" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER",
       "LUMBER"
       ],
     "BUILD_POINT" : 3,
     "MINERALS" : 230,
     "WATER" : 60,
     "LUMBER" : 100
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 500,
     "SEASONS" : 12
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 1,
     "LARGE_TOWN" : 1,
     "SMALL_CITY" : 2,
     "MEDIUM_CITY" : 2,
     "LARGE_CITY" : 4,
     "MEGALOPOLIS" : 4
     #1 : SMALL_TOWN_POP,
     #2 : SMALL_CITY_POP,
     #4 : LARGE_CITY_POP,
     #5 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "PIETY_SPECIFIC",
       "SATISFACTION_MIDDLE_CLASS",
       "SATISFACTION_UPPER_CLASS",
     ],
     "PIETY_SPECIFIC" : 3,
     "SATISFACTION_MIDDLE_CLASS" : 1,
     "SATISFACTION_UPPER_CLASS" : 1
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
        "WATER",
        "LIVESTOCK"
        ],
      "WATER" : 60,
      "LIVESTOCK" : 40
      }
   },

 "MONASTERY" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "CROPS",
       "WATER",
       "LIVESTOCK"
       ],
     "BUILD_POINT" : 5,
     "MINERALS" : 600,
     "WATER" : 200,
     "LIVESTOCK" : 80
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 625,
     "SEASONS" : 16
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 0,
     "LARGE_TOWN" : 0,
     "SMALL_CITY" : 0,
     "MEDIUM_CITY" : 1,
     "LARGE_CITY" : 1,
     "MEGALOPOLIS" : 1
     #1 : MEDIUM_CITY_POP,
     #2 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "PIETY_SPECIFIC",
       "SATISFACTION_LOWER_CLASS",
       "SATISFACTION_MIDDLE_CLASS",
       "SATISFACTION_UPPER_CLASS"
     ],  
     "PIETY_SPECIFIC" : 6,
     "SATISFACTION_LOWER_CLASS" : 2,
     "SATISFACTION_MIDDLE_CLASS" : 2,
     "SATISFACTION_UPPER_CLASS" : 2
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "WATER",
      "CROPS",
      "LIVESTOCK"
      ],
    "WATER" : 120,
    "CROPS" : 60,
    "LIVESTOCK" : 60
   }
 },


 "GARRISON" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "LUMBER"
       ],
     "BUILD_POINT" : 1,
     "LUMBER" : 40
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 4
   },

   "POPULATION" : {
     "HAMLET" : 1,
     "VILLAGE" : 1,
     "SETTLEMENT" : 1,
     "SMALL_TOWN" : 2,
     "LARGE_TOWN" : 2,
     "SMALL_CITY" : 3,
     "MEDIUM_CITY" : 3,
     "LARGE_CITY" : 4,
     "MEGALOPOLIS" : 4
     #1 : HAMLET_POP,
     #2 : SMALL_TOWN_POP,
     #3 : SMALL_CITY_POP,
     #4 : LARGE_CITY_POP,
     #5 : "MAX"
   },
   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "DEFENSE"
       ],
     "DEFENSE" : 1
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : []
   }
 },

 "TOWER" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "LUMBER"
       ],
     "BUILD_POINT" : 2,
     "MINERALS" : 40,
     "LUMBER" : 90
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 8
   },

   "POPULATION" : {
     "HAMLET" : 1,
     "VILLAGE" : 1,
     "SETTLEMENT" : 1,
     "SMALL_TOWN" : 1,
     "LARGE_TOWN" : 2,
     "SMALL_CITY" : 2,
     "MEDIUM_CITY" : 3,
     "LARGE_CITY" : 3,
     "MEGALOPOLIS" : 3
     #1 : HAMLET_POP,
     #2 : SMALL_CITY_POP,
     #6 : MEDIUM_CITY_POP,
     #10 : "MAX"
   },
   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "DEFENSE"
       ], 
     "DEFENSE" : 2
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "CROPS"
      ],
    "CROPS" : 40
   }
 },

 "TRAINING_CAMP" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "CROPS",
       "WATER",
       "LUMBER"
       ],
     "BUILD_POINT" : 3,
     "CROPS" : 120,
     "WATER" : 40,
     "LUMBER" : 260
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 1,
     "LARGE_TOWN" : 1,
     "SMALL_CITY" : 1,
     "MEDIUM_CITY" : 2,
     "LARGE_CITY" : 2,
     "MEGALOPOLIS" : 2
     #1 : SMALL_TOWN_POP,
     #2 : MEDIUM_CITY_POP,
     #3 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
     "MILITARY_TRAINING"
     ],
     "MILITARY_TRAINING" : 1
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "LUMBER",
      "CROPS"
      ],
    "LUMBER" : 80,
    "CROPS" : 50
   }
 },

 "KEEP" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "LUMBER",
       "CROPS"
       ],
     "BUILD_POINT" : 4,
     "MINERALS" : 450,
     "LUMBER" : 140,
     "CROPS" : 90
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 500,
     "SEASONS" : 20
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 0,
     "LARGE_TOWN" : 1,
     "SMALL_CITY" : 1,
     "MEDIUM_CITY" : 1,
     "LARGE_CITY" : 2,
     "MEGALOPOLIS" : 2
     #1 : LARGE_TOWN_POP,
     #2 : LARGE_CITY_POP,
     #3 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "DEFENSE"
     ],  
     "DEFENSE" : 5
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
    "CROPS",
    "LIVESTOCK"
    ],
    "CROPS" : 70,
    "LIVESTOCK" : 70
   }
 },

 "CASTLE" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "LUMBER"
       ],
     "BUILD_POINT" : 5,
     "MINERALS" : 700,
     "LUMBER" : 100
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 500,
     "SEASONS" : 32
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 0,
     "LARGE_TOWN" : 0,
     "SMALL_CITY" : 1,
     "MEDIUM_CITY" : 1,
     "LARGE_CITY" : 1,
     "MEGALOPOLIS" : 1
     #1 : SMALL_CITY_POP,
     #2 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "DEFENSE",
       "SATISFACTION_LOWER_CLASS",
       "SATISFACTION_MIDDLE_CLASS",
       "SATISFACTION_UPPER_CLASS"
       ],
     "DEFENSE" : 8,
     "SATISFACTION_LOWER_CLASS" : 1,
     "SATISFACTION_MIDDLE_CLASS" : 1,
     "SATISFACTION_UPPER_CLASS" : 1
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "LUMBER",
      "LIVESTOCK",
      "CROPS"
      ],
    "LUMBER" : 80,
    "CROPS" : 100,
    "LIVESTOCK" : 50
   }
 },

 "BAR" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "LUMBER"
       ],
     "BUILD_POINT" : 1,
     "LUMBER" : 40
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     "HAMLET" : 1,
     "VILLAGE" : 1,
     "SETTLEMENT" : 1,
     "SMALL_TOWN" : 2,
     "LARGE_TOWN" : 2,
     "SMALL_CITY" : 3,
     "MEDIUM_CITY" : 3,
     "LARGE_CITY" : 4,
     "MEGALOPOLIS" : 5
     #1 : HAMLET_POP,
     #2 : SMALL_TOWN_POP,
     #3 : SMALL_CITY_POP,
     #4 : LARGE_CITY_POP,
     #5 : MEGALOPOLIS_POP,
     #6 : "MAX"
   },
   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "SATISFACTION_LOWER_CLASS",
       "SATISFACTION_MIDDLE_CLASS"
       ],  
     "SATISFACTION_LOWER_CLASS" : 1,
     "SATISFACTION_MIDDLE_CLASS" : 1
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "CROPS"
      ],
    "CROPS" : 15
   }
 },

 "PALACE" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER",
       "LUMBER"
       ],
     "BUILD_POINT" : 2,
     "MINERALS" : 40,
     "WATER" : 20,
     "LUMER" : 50
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 6
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 1,
     "SMALL_TOWN" : 1,
     "LARGE_TOWN" : 1,
     "SMALL_CITY" : 2,
     "MEDIUM_CITY" : 2,
     "LARGE_CITY" : 3,
     "MEGALOPOLIS" : 3
     #1 : SETTLEMENT_POP,
     #2 : SMALL_CITY_POP,
     #3 : LARGE_CITY_POP,
     #4 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "SATISFACTION_UPPER_CLASS",
       "DEFENSE"
       ],
     "DEFENSE" : 1,
     "SATISFACTION_UPPER_CLASS" : 2
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "WATER"
      ],
    "WATER" : 15
   }
 },

 "SHOWPLACE" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "LUMBER"
       ],
     "BUILD_POINT" : 2,
     "LUMBER" : 100
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 4
   },

   "POPULATION" : {
     "HAMLET" : 1,
     "VILLAGE" : 1,
     "SETTLMENT" : 1,
     "SMALL_TOWN" : 2,
     "LARGE_TOWN" : 2,
     "SMALL_CITY" : 3,
     "MEDIUM_CITY" : 3,
     "LARGE_CITY" : 4,
     "MEGALOPOLIS" : 3
     }
     #2 : 1001,
     #4 : 2001,
     #6 : 15001,
     #10 : "MAX"
   },
   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "SATISFACTION_LOWER_CLASS",
       "SATISFACTION_MIDDLE_CLASS",
       "SATISFACTION_UPPER_CLASS"
       ],
     "SATISFACTION_LOWER_CLASS" : 1,
     "SATISFACTION_MIDDLE_CLASS" : 1,
     "SATISFACTION_UPPER_CLASS" : 1
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "LIVESTOCK"
      ],
    "LIVESTOCK" : 25
   }
 },

 "THEATRE" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "LUMBER",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 4,
     "MINERALS" : 90,
     "WATER" : 40,
     "LUMBER" : 240
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 500,
     "SEASONS" : 16
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 0,
     "LARGE_TOWN" : 1,
     "SMALL_CITY" : 1,
     "MEDIUM_CITY" : 2,
     "LARGE_CITY" : 2,
     "MEGALOPOLIS" : 3
     #1 : LARGE_TOWN_POP,
     #2 : MEDIUM_CITY_POP,
     #3 : MEGALOPOLIS_POP,
     #4 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "SATISFACTION_LOWER_CLASS",
       "SATISFACTION_MIDDLE_CLASS",
       "SATISFACTION_UPPER_CLASS"
       ],
     "SATISFACTION_LOWER_CLASS" : 3,
     "SATISFACTION_MIDDLE_CLASS" : 3,
     "SATISFACTION_UPPER_CLASS" : 4
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "CROPS",
      "LUMBER",
      "WATER"
      ],
    "CROPS" : 50,
    "LUMBER" : 50,
    "WATER" : 20
   }
 },

 "COLOSSEUM" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER",
       "LUMBER"
       ],
     "BUILD_POINT" : 7,
     "MINERALS" : 1200,
     "WATER" : 160,
     "LUMBER" : 340
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 1250,
     "SEASONS" : 16
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 0,
     "LARGE_TOWN" : 0,
     "SMALL_CITY" : 0,
     "MEDIUM_CITY" : 0,
     "LARGE_CITY" : 1,
     "MEGALOPOLIS" : 1
     #1 : LARGE_CITY_POP,
     #2 : "MAX"
   },

   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "SATISFACTION_LOWER_CLASS",
       "SATISFACTION_MIDDLE_CLASS",
       "SATISFACTION_UPPER_CLASS",
       "MILITARY_ENTERTAINMENT"
       ],
     "SATISFACTION_LOWER_CLASS" : 6,
     "SATISFACTION_MIDDLE_CLASS" : 4,
     "SATISFACTION_UPPER_CLASS" : 4,
     "MILITARY_ENTERTAINMENT" : True
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "CROPS",
      "MINERALS",
      "LUMBER",
      "LIVESTOCK",
      "WATER"
      ],
    "WATER" : 60,
    "LIVESTOCK" : 100,
    "LUMBER" : 100,
    "MINERALS" : 150,
    "CROPS" : 100
   }
 },

 "CRADLE_OF_GODS" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 7,
     "MINERALS" : 1300,
     "WATER" : 400
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 750,
     "SEASONS" : 32
   },

   "POPULATION" : {
     "HAMLET" : 0,
     "VILLAGE" : 0,
     "SETTLEMENT" : 0,
     "SMALL_TOWN" : 0,
     "LARGE_TOWN" : 0,
     "SMALL_CITY" : 0,
     "MEDIUM_CITY" : 0,
     "LARGE_CITY" : 1,
     "MEGALOPOLIS" : 1
     #1 : LARGE_CITY_POP,
     #2 : "MAX"
   },
   "BENEFIT" : {
     "BENEFIT_LIST" : [
       "PEITY_SPECIFIC",
       "DEFENSE",
       "SATISFACTION_LOWER_CLASS",
       "SATISFACTION_MIDDLE_CLASS",
       "SATISFACTION_UPPER_CLASS"
       ],
     "PIETY_SPECIFIC" : 12,
     "DEFENSE" : 2,
     "SATISFACTION_LOWER_CLASS" : 2,
     "SATISFACTION_MIDDLE_CLASS" : 2,
     "SATISFACTION_UPPER_CLASS" : 2
   },

   "UPKEEP" : {
    "UPKEEP_REQUIRED" : [
      "MINERLAS",
      "WATER",
      "LIVESTOCK"
      ],
    "MINERLAS" : 180,
    "WATER" : 200,
    "LIVESTOCK" : 140
   }
 }

}

PROVINCE_CONSTANTS = {
  "POP_REQUIREMENTS" : {
      "HAMLET" : HAMLET_POP,
      "VILLAGE" : VILLAGE_POP,
      "SETTLEMENT" : SETTLEMENT_POP,
      "SMALL_TOWN" : SMALL_TOWN_POP,
      "LARGE_TOWN" : LARGE_TOWN_POP,
      "SMALL_CITY" : SMALL_CITY_POP,
      "MEDIUM_CITY" : MEDIUM_CITY_POP,
      "LARGE_CITY" : LARGE_CITY_POP,
      "MEGALOPOLIS" : MEGALOPOLIS_POP
  },

  "POP_BUILD_POINTS" : {
      "HAMLET" : 1,
      "VILLAGE" : 2,
      "SETTLEMNET" : 3,
      "SMALL_TOWN" : 5,
      "LARGE_TOWN" : 8,
      "SMALL_CITY" : 12,
      "MEDIUM_CITY" : 20,
      "LARGE_CITY" : 30,
      "MEGALOPOLIS" : 50
  }
}

GODS = {
        "MAKOTHA" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .75
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_ADDITION" : -.01
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_INCREASE" : -.3,
                    "ADULT_GAIN_INCREASE" : .1
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "CASUALTY_INCREASE" : -.05
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_ADDITION" : -.1
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_INCREASE" : -.5
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "CASUALTY_INCREASE" : .01
                    },
                "ANGERED" : {
                    "NATURAL_DEATH_INCREASE" : .05
                    },
                "ENRAGED" : {
                    "NATURAL_DEATH_ADDITION" : .01
                    }
                },
            "RIVAL" : "TIAMAT"
            },

        "CYNTHI" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "ADULT_GAIN_ADDITION" : .01
                    },
                "MAJOR" : {
                    "CHILD_GAIN_ADDITION" : .01
                    },
                "EXALTED" : {
                    "ADULT_GAIN_INCREASE" : .25,
                    "CHILD_GAIN_INCREASE" : .25
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "ADULT_GAIN_INCREASE" : .15
                    },
                "MAJOR" : {
                    "CHILD_GAIN_INCREASE" : .15
                    },
                "EXALTED" : {
                    "ADULT_GAIN_ADDITION" : .01,
                    "CHILD_GAIN_ADDITION" : .01
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "ADULT_GAIN_INCREASE" : -.1
                    },
                "ANGERED" : {
                    "CHILD_GAIN_INCREASE" : -.1
                    },
                "ENRAGED" : {
                    "CHILD_GAIN_INCREASE" : -.1
                    }
                },
            "RIVAL" : "SZETH"
            },

        "BELSOYU" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "COMPANY_UPGRADE_INCREASE" : -.1
                    },
                "MAJOR" : {
                    "TRADE_SPEED" : .15
                    },
                "EXALTED" : {
                    "TRADE_PROFIT" : .2
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "TRADE_PROFIT" : .05
                    },
                "MAJOR" : {
                    "LOGISTICS_CAPACITY_INCREASE" : 75
                    },
                "EXALTED" : {
                    "TRADE_SPEED" : .15
                    "CONSTRUCTION_TAX" : True
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "TRADE_PROFIT" : -.1
                    },
                "ANGERED" : {
                    "TRADE_SPEED" : -.2
                    },
                "ENRAGED" : {
                    "LOGISTICS_CAPACITY_INCREASE" : -25
                    }
                },
            "RIVAL" : "NYANITI"
            },

        "MAKOTHA" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .75
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .01
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .3,
                    "ADULT_GAIN_INCREASE" : .1
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .05
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .1
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .5
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "CASUALTY_INCREASE" : .1
                    },
                "ANGERED" : {
                    "NATURAL_DEATH_INCREASE" : .05
                    },
                "ENRAGED" : {
                    "NATURAL_DEATH_ADDITION" : .01
                    }
                }
            },

        "MAKOTHA" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .75
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .01
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .3,
                    "ADULT_GAIN_INCREASE" : .1
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .05
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .1
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .5
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "CASUALTY_INCREASE" : .1
                    },
                "ANGERED" : {
                    "NATURAL_DEATH_INCREASE" : .05
                    },
                "ENRAGED" : {
                    "NATURAL_DEATH_ADDITION" : .01
                    }
                }
            },

        "MAKOTHA" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .75
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .01
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .3,
                    "ADULT_GAIN_INCREASE" : .1
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .05
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .1
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .5
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "CASUALTY_INCREASE" : .1
                    },
                "ANGERED" : {
                    "NATURAL_DEATH_INCREASE" : .05
                    },
                "ENRAGED" : {
                    "NATURAL_DEATH_ADDITION" : .01
                    }
                }
            },

        "MAKOTHA" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .75
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .01
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .3,
                    "ADULT_GAIN_INCREASE" : .1
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .05
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .1
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .5
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "CASUALTY_INCREASE" : .1
                    },
                "ANGERED" : {
                    "NATURAL_DEATH_INCREASE" : .05
                    },
                "ENRAGED" : {
                    "NATURAL_DEATH_ADDITION" : .01
                    }
                }
            },

        "MAKOTHA" : {
            "SETTLEMENT" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .75
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .01
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .3,
                    "ADULT_GAIN_INCREASE" : .1
                    }
                },
            "STATE" : {
                "MINOR" : {
                    "CASUALTY_REDUCTION" : .05
                    },
                "MAJOR" : {
                    "NATURAL_DEATH_SUBTRACTION" : .1
                    },
                "EXALTED" : {
                    "NATURAL_DEATH_REDUCTION" : .5
                    }
                },
            "DETRIMENT" : {
                "IRATE" : {
                    "CASUALTY_INCREASE" : .1
                    },
                "ANGERED" : {
                    "NATURAL_DEATH_INCREASE" : .05
                    },
                "ENRAGED" : {
                    "NATURAL_DEATH_ADDITION" : .01
                    }
                }
            }
        }




