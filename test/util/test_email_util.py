from app.util.email_util import deliver_email


def test_email_util():
    deliver_email('shubhipun@gmail.com', 4412)
