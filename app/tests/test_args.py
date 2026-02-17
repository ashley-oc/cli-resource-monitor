from app.cli import parse_args


def test_interval_argument():
    args = parse_args(["--refresh-interval", "5"])
    assert args.refresh_interval == 5


def test_default_interval():
    args = parse_args([])
    assert args.refresh_interval == 1