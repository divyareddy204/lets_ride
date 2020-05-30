from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetUserProfileInteractor():
    
    def __init__(self, storage: PostStorageInterface,
                 presenter: PresenterInterface):
                     self.storage =storage
                     self.presenter = presenter
    
    def get_user_profile(self)