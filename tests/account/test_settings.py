import pytest
from ymdantic import YMClient
from ymdantic.models.account import SetAccountSettingsParams


@pytest.mark.anyio
async def test_set_account_settings_direct(client: YMClient) -> None:
    old_settings = await client.get_account_settings()

    settings = await client.set_account_settings_request(
        SetAccountSettingsParams(
            auto_play_radio=not old_settings.auto_play_radio,
        ),
    )
    assert settings.result.auto_play_radio != old_settings.auto_play_radio


@pytest.mark.anyio
async def test_set_account_settings(client: YMClient) -> None:
    old_settings = await client.get_account_settings()

    settings = await client.set_account_settings(
        auto_play_radio=not old_settings.auto_play_radio,
    )
    assert settings.auto_play_radio != old_settings.auto_play_radio
