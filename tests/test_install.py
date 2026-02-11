def test_import():
    import novatron

    assert hasattr(novatron, "__version__")


def test_cli_app():
    from novatron.cli import app

    assert app is not None
