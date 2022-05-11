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


def get_user_info(user):
    return {
        "userName": user.username,
        "userFirstName": user.first_name,
        "userLastName": user.last_name,
        "userIsActive": user.is_active,
        "userType": user.user_type,
        "userEmail": user.email,
        "userIconUrl": user.user_icon_url,
    }


def get_application_info(application):
    return {
        "applicationId": application.application_id,
        "applicationUser": application.application_user,
        "applicationImage": application.application_image,
        "applicationDate": application.application_date,
        "applicationDescription": application.application_description,
    }
