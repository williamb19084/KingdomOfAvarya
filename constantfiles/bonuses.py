# This file stores all the constants for the program

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
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },
 "CHAPEL" : {
   "MATERIALS" : {
     "MATERIALS_REQUIRED" : [
       "BUILD_POINT",
       "MINERALS",
       "WATER"
       ],
     "BUILD_POINT" : 1,
     "MINERALS" : 30,
     "WATER" : 15
     },
    
   "CONSTRUCTION" : {
     "WORKERS" : 250,
     "SEASONS" : 2
   },

   "POPULATION" : {
     1 : 0,
     2 : 1001,
     4 : 2001,
     6 : 15001,
     10 : "MAX"
   },





























