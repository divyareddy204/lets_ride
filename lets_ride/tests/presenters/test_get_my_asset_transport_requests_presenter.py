from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
import pytest

@pytest.mark.django_db
class TestPresenterImplementation():

    def test_get_my_asset_request_response_returns_details_asset_requests(self,
        asset_request_dto1,
        my_asset_request_dto,
        create_users,
        create_asset_requests,
        asset_request_dto2,
        asset_request_response,user_dtos):

        #Arrange
        presenter = PresenterImplementation()
        expected_output= asset_request_response

        #Act
        print(my_asset_request_dto)
        result = presenter.get_my_asset_requests_response(
            my_asset_request_dto=my_asset_request_dto,
            user_dtos=user_dtos)

        #Assert
        assert result == expected_output
    
    def test_get_my_asset_request_response_with_no_accepted_person_returns_empty_dict(self,
        asset_request_dto1_with_accepted_person_none,
        my_asset_request_dto_with_accepted_person_none,
        create_users,
        create_asset_requests,
        asset_request_dto2,
        asset_request_response_with_accepted_person_none,user_dtos):

        #Arrange
        presenter = PresenterImplementation()
        expected_output= asset_request_response_with_accepted_person_none

        #Act
        print(my_asset_request_dto_with_accepted_person_none)
        result = presenter.get_my_asset_requests_response(
            my_asset_request_dto=my_asset_request_dto_with_accepted_person_none,
            user_dtos=user_dtos)

        #Assert
        assert result == expected_output
    
    def test_get_my_asset_request_when_no_requests_returns_empty_list(self,
        user_dtos, my_asset_request_dto_with_no_assert_requests,
        asset_request_response_with_no_asset_requests):
            
        #Arrange
        presenter = PresenterImplementation()
        expected_output= asset_request_response_with_no_asset_requests

        #Act
        result = presenter.get_my_asset_requests_response(
            my_asset_request_dto=my_asset_request_dto_with_no_assert_requests,
            user_dtos=user_dtos)

        #Assert
        assert result == expected_output