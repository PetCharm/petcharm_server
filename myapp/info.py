from datetime import timezone

from myapp.models import *


def get_pet_info(pet):
    return {
        "petId": pet.pet_id,
        "petName": pet.pet_name,
        "petType": pet.pet_type,
        "petBreed": pet.pet_breed,
        "petGender": pet.pet_gender,
        "petAge": (datetime.now(timezone.utc) - pet.pet_date_of_birth).days,
        "petDateOfBirth": pet.pet_date_of_birth,
        "petVaccinationStatus": pet.pet_vaccination_status,
        "petRegistrationNumber": pet.pet_registration_number,
        "petIconUrl": pet.pet_icon_url,
    }


def get_user_info(user):
    return {
        "userName": user.username,
        "userFirstName": user.first_name,
        "userLastName": user.last_name,
        "userIsActive": user.is_active,
        "userEmailValid": user.email_valid,
        "userType": user.user_type,
        "userEmail": user.email,
        "userIconUrl": user.user_icon_url,
    }


def get_application_info(application):
    return {
        "applicationId": application.application_id,
        "applicationType": application.application_type,
        "applicationUserName": application.application_user.username,
        "applicationUserFirstName": application.application_user.first_name,
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
        "postAuthor": post.post_user.first_name,
        "postCover": post.post_cover,
    }


def get_comment_info(comment):
    return {
        "commentId": comment.comment_id,
        "commentContent": comment.comment_content,
        "commentDate": comment.comment_date.strftime("%Y-%m-%d %H:%M"),
        "commentAuthor": comment.comment_user.first_name,
        "commentIconUrl": comment.comment_user.user_icon_url,
    }


def get_trace_path_info(trace_path, complicated=False):
    info = {
        "tracePathId": trace_path.trace_path_id,
        "tracePathStartTime": trace_path.trace_path_start_time.strftime("%Y-%m-%d %H:%M"),
        "tracePathEndTime": trace_path.trace_path_end_time.strftime("%Y-%m-%d %H:%M"),
        "tracePathNote": trace_path.trace_path_note,
    }
    if complicated:
        info["tracePathCoordinates"] = trace_path.trace_path_coordinates
    return info


def get_service_info(user, complicated=False):
    info = {
        "userId": user.id,
        "userName": user.username,
        "userFirstName": user.first_name,
        "userType": user.user_type,
        "userEmail": user.email,
        "userIconUrl": user.user_icon_url,
    }
    return info


def get_service_score(user):
    score = 0
    count = 0
    ratings = Rating.objects.filter(rating_user=user)
    for rating in ratings:
        score += rating.rating_score
        count += 1
    if count == 0:
        return 0
    return score / count
