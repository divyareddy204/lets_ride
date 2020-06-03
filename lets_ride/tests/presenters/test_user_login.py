from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
import pytest

@pytest.mark.django_db
class TestPresenterImplementation():

    def test_user_login_returns_access_token_details(self,user_access_dto):
        
        #Arrange
        presenter = PresenterImplementation()
        expected_output= {
            'user_id': 3,
            'access_token': 'mbnZBmyNDz7KIRnTjQ3QBvnLAN7BTj',
            'refresh_token': 'qHCVVNwdm8OWw2nDH9XbsPyhI5lIQQ',
            'expires_in': '2052-02-10 20:56:09.642688'}
        #Act
        result = presenter.user_login_response(
            user_access_token_dto=user_access_dto)
            
        #Asset
        assert result == expected_output