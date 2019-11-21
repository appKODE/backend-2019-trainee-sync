from pitter.models.base import User


def registration():
    creation_date = '2019-11-21 09:02:13.147316'
    updating_date = '2019-11-21 09:02:13.147316'
    id = 1
    login = 'alex_login'
    password = '1234'
    profile_name = 'alex_profile_name'
    email_address = 'alex_email'

    u = User(created_at=creation_date,
             updated_at=updating_date,
             id=id,
             login=login,
             password=password,
             profile_name=profile_name,
             email_address=email_address,
             email_notifications_mode=True)
    u.save()
