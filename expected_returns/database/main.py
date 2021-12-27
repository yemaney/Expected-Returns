from sqlmodel import Session

from database import create_db_and_tables, engine
from models import GlobalCape, NationalCape


def create_capes():  #

    global_cape_1 = GlobalCape(cape=3.839, date="6/30/2021")  #
    global_cape_2 = GlobalCape(cape=4.032, date="3/31/202")
    global_cape_3 = GlobalCape(cape=4.188, date="12/31/2020")

    national_cape_1 = NationalCape(cape=3.923, date="6/30/2021", nation="Canada")  #
    national_cape_2 = NationalCape(cape=4.383, date="12/31/2020", nation="Canada")
    national_cape_3 = NationalCape(cape=4.615, date="6/30/2020", nation="Canada")

    with Session(engine) as session:  #
        session.add(global_cape_1)  #
        session.add(global_cape_2)
        session.add(global_cape_3)

        session.add(national_cape_1)
        session.add(national_cape_2)
        session.add(national_cape_3)

        session.commit()


if __name__ == "__main__":
    create_db_and_tables()
    create_capes()
