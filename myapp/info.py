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


def get_post_info(post):
    return {
        "postId": post.post_id,
        "postTitle": post.post_title,
        "postContent": post.post_content,
        "postDate": post.post_date.strftime("%Y-%m-%d %H:%M"),
        "postAuthor": post.post_user.first_name + post.post_user.last_name,
        "postCover": post.post_cover,
    }


def get_comment_info(comment):
    return {
        "commentId": comment.comment_id,
        "commentContent": comment.comment_content,
        "commentDate": comment.comment_date.strftime("%Y-%m-%d %H:%M"),
        "commentAuthor": comment.comment_user.first_name + comment.comment_user.last_name,
    }