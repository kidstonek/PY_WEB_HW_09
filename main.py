from sqlalchemy.orm import joinedload

from models import session, Name, Address, Email, Phone


def get_all_names():
    names = session.query(Name).options(joinedload("address")).all()
    for name in names:
        print(vars(name))
        print(f'{[f" address is {n.address_ad}" for n in name.address]}')


if __name__ == '__main__':
    get_all_names()
