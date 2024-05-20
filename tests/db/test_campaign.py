import db
from assertpy import assert_that


def test_campaign_by_id(campaign_repo: db.CampaignRepository) -> None:
    cid = 2
    campaign = campaign_repo.get_by_id(cid)

    assert_that(campaign).is_not_none()
    assert_that(campaign.id).is_equal_to(cid)
    assert_that(campaign.users).is_not_empty()
