from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='test', password='secret', email='teste@test')
        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'test'))
        session.add(user)

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test',
        'password': 'secret',
        'created_at': time,
    }
