from app import hello_world


def test_hello_world() -> None:
    # Given
    returned_expected = 'Hello, World!'

    # When
    value_returned = hello_world()

    # Then
    assert value_returned == returned_expected
