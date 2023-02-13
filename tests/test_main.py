from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_mock.plugin import MockerFixture

import services_test2


def test_entrypoint_calls_app(mocker: "MockerFixture") -> None:
    mocker.patch("services_test2.cli.app")
    from services_test2 import __main__  # noqa: F401

    services_test2.cli.app.assert_called_once_with(  # type: ignore[attr-defined]
        prog_name="services-test2",
    )
