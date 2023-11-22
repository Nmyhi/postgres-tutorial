from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for "Programmer" table


class Programmer(base):
    __tablename__ = "Programmer"
    Id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session( subclass defined above)
session = Session()


# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Groce",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gastes = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_burners_lee = Programmer(
    first_name="Tim",
    last_name="Burners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

mihaly_lovrencsics = Programmer(
    first_name="Mihaly",
    last_name="Lovrencsics",
    gender="M",
    nationality="Hungarian",
    famous_for="AI based programming language"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gastes)
# session.add(tim_burners_lee)
session.add(mihaly_lovrencsics)



# commit our session to the database
session.commit()

# query the database to find all Programmers
programmers= session.query(Programmer)
for programmer in programmers:
    print(
        programmer.Id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep = " | "
    )
