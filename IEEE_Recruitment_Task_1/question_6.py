# Dictionaries to store the cutoffs.


cutoff_ls =[                                                                  #storing the data in a list of tuples

    # Pilani
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Msc Eco", 271),
    ("Pilani", "Msc Bio", 236),

    # Goa
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Msc Eco", 263),
    ("Goa", "Msc Bio", 234),

    # Hyderabad
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Msc Eco", 261),
    ("Hyderabad", "Msc Bio", 234),
]

cutoff_dict={                                                                      # converting tuple to dictionary

    "Pilani" : {"CS" : 327, "Chemical" : 275, "Msc Eco" : 271, "Msc Bio" : 236  },
    "Goa" : {"CS" : 301, "Chemical" : 239, "Msc Eco" : 263, "Msc Bio" : 234},
    "Hyderabad" : {"CS" : 298, "Chemical" : 238, "Msc Eco" : 261, "Msc Bio" : 234}, 
}

print(cutoff_dict["Pilani"]["Msc Bio"])                                               # Accessing the cutoff for CS in Pilani

print(cutoff_dict["Goa"])                                               # Accessing the cutoff for Chemical in Goa
