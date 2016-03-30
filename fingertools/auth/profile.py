from fingertools.auth.models import UserProfile


def create_user_profile(user):
    profile = UserProfile()
    profile.user = user
    profile.url = ''
    profile.premium = False
    profile.save()
    return profile