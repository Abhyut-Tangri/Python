
"""
farm_animals={'cow','sheep','hen','horse','goat'}
wild_animal={'lion','elephant','tiger','goat','panther','horse'}
all_animals=farm_animals.union(wild_animal)
print(all_animals)"""

from prescription_data import adverse_interactions
meds_to_watch=set()

#for interaction in adverse_interactions:
    #meds_to_watch=meds_to_watch.union(interaction)
    #meds_to_watch.update(interaction)
    
meds_to_watch.update(*adverse_interactions)

print(sorted(meds_to_watch))
 