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
            "MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
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
            #"MINERAL_ADV" : False,
            #"WATER_ADV" : False,
            #"PRODUCTION_ADV" : False
          }
        },

        "WARLOCK" : {
          "BONUSES" : {
            "INDEPTH" : [
              "MINERAL_ADV",
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
            "MINERAL_ADV" : True,
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
            #"MINERAL_ADV" : False,
            #"WATER_ADV" : False,
            "PRODUCTION_ADV" : 1
          }
        }
    }

SPECIES_BONUSES = {
 "HUMANS" : {
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
      "MINERAL_PRODUCTION"
      ],
    "SECONDARY_BONUS" : [
      "MINERAL_ADV"
      ],
    "COMBAT_BONUS" : [
      "DEFENSE"
      ]
    },

  "BONUS_VALUES" : {
    "MINERAL_PRODUCTION" : .2,
    "MINERAL_ADV" : True,
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
        "MINERALS_PRODUCTION",
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
    "MINERALS_PRODUCTION" : .05,
    "WATER_PRODUCTION" : .05  
    }
  },

 "HUMANS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : "PRODUCTION_ADV",
    "SECONDARY_BONUS" : None,
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

 "HUMANS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : "PRODUCTION_ADV",
    "SECONDARY_BONUS" : None,
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

 "HUMANS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : "PRODUCTION_ADV",
    "SECONDARY_BONUS" : None,
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

 "HUMANS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : "PRODUCTION_ADV",
    "SECONDARY_BONUS" : None,
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

 "HUMANS" : {
  "BONUSES" : {
    "PRIMARY_BONUS" : "PRODUCTION_ADV",
    "SECONDARY_BONUS" : None,
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
  }
}
