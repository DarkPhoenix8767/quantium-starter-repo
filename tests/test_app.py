import pytest
from app import app


@pytest.fixture
def dash_app():
    return app


def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    dash_duo.wait_for_element("#header", timeout=20)

    assert dash_duo.find_element("#header") is not None


def test_visualisation_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    dash_duo.wait_for_element("#sales-line-chart", timeout=20)

    assert dash_duo.find_element("#sales-line-chart") is not None


def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    dash_duo.wait_for_element("#region-filter", timeout=20)

    assert dash_duo.find_element("#region-filter") is not None