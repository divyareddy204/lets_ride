from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
import pytest

@pytest.mark.django_db
class TestPresenterImplementation():

    def test_get_my_ride_request_response_returns_details_ride_requests(self,
        ride_request_dto1,
        my_ride_request_dto,
        create_users,
        create_ride_requests,
        ride_request_dto2,
        ride_request_response,user_dtos,ride_request_dtos):

        #Arrange
        presenter = PresenterImplementation()
        expected_output= ride_request_response
        #print(ride_request_response)
        #Act
        print("*"*180)
        print(my_ride_request_dto)
        result = presenter.get_my_ride_requests_response(
            my_ride_request_dto=my_ride_request_dto,
            user_dtos=user_dtos)

        #Assert
        assert result == expected_output
    
    def test_get_my_ride_request_response_when_accepted_person_is_null(self,
        ride_request_dto1_with_accepted_person_none,
        my_ride_request_dto_with_accepted_person_none,
        create_users,
        create_ride_requests_with_accepted_person_none,
        ride_request_dto2,
        ride_request_response_with_accepted_person_none,user_dtos,ride_request_dtos):
        
        presenter = PresenterImplementation()
        expected_output= ride_request_response_with_accepted_person_none
        #print(ride_request_response)
        #Act
        print("*"*180)
        print(my_ride_request_dto_with_accepted_person_none)
        result = presenter.get_my_ride_requests_response(
            my_ride_request_dto=my_ride_request_dto_with_accepted_person_none,
            user_dtos=user_dtos)

        #Assert
        assert result == expected_output
    
    def test_get_my_asset_request_when_no_requests_returns_empty_list(self,
        user_dtos, my_ride_request_dto_with_no_ride_requests,
        ride_request_response_with_no_ride_requests):
            
        #Arrange
        presenter = PresenterImplementation()
        expected_output= ride_request_response_with_no_ride_requests

        #Act
        result = presenter.get_my_asset_requests_response(
            my_asset_request_dto=my_ride_request_dto_with_no_ride_requests,
            user_dtos=user_dtos)

        #Assert
        assert result == expected_output