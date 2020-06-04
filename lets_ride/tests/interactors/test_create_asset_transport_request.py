import pytest
from unittest.mock import create_autospec
from lets_ride.interactors.create_asset_transport_request_interactor \
    import CreateAssetTransportRequestInteractor
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.constants.enums import AssetType, SensitivityType

def test_asset_transport_request_creates_asset_transport_object():
    
    
    source = "hyderabad"
    destination = "bangloor"
    is_flexible = True
    datetime = ""
    from_datetime = "2020,5,28,20,00,00"
    to_datetime = "2020,5,29,09,00,00"
    no_of_assets = 2
    asset_type = AssetType.parcel.value
    sensitivity = SensitivityType.HighlySensitive.value
    deliver_person = "ram"
    user_id = 1

    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateAssetTransportRequestInteractor(
        storage = storage,
        presenter = presenter
        )
    #act
    interactor.create_asset_transport_request(
        source=source,
        destination=destination ,
        is_flexible=is_flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        no_of_assets=no_of_assets,
        asset_type=asset_type,
        sensitivity=sensitivity,
        deliver_person=deliver_person,
        user_id=user_id
        )

    #assert
    storage.create_asset_transport_request.assert_called_once_with(source=source,
            destination=destination ,
            is_flexible=is_flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_assets=no_of_assets,
            asset_type=asset_type,
            sensitivity=sensitivity,
            deliver_person=deliver_person,
            user_id = user_id
            )
