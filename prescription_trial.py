from prescription_data import *


trial_patients=['Denise','Eddie','Frank','Georgia']

#removing warfarin and adding edoxban
for patient in trial_patients:
    prescription=patients[patient]
    prescription.remove(warfarin)
    prescription.add(edoxaban)