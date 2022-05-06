from datetime import timezone

from myapp.models import *


def get_pet_info(pet):
    return {
        "petName": pet.pet_name,
        "petType": pet.pet_type,
        "petBreed": pet.pet_breed,
        "petGender": pet.pet_gender,
        "petAge": (datetime.now() - pet.pet_date_of_birth).days,
        "petRegistrationNumber": pet.pet_registration_number,
    }
