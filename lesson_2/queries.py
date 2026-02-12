from sqlalchemy import create_engine

from db_connector import DBConnector
from social_blogs_models import *

engine = create_engine(
    url="mysql+pymysql://ich1:ich1_password_ilovedbs@ich-edit.edu.itcareerhub.de:3306/social_blogs",
    future=True
)

with DBConnector(engine) as db:


    #crud
    #data = {"name": "Denys"}
    #new_role = Role(**data)
    #db.add(new_role)
    #db.commit()

    #READ
    #user = db.get(User, 11)
    #print(user.__dict__)
    #all_authors = (select(User).where(User.id == 3))
    #user = db.execute(all_authors).scalars()

    #data = { "id": user.id, "name": user.first_name, "role": user.role}
    #for author in user:
        #print(data)

    #result = db.query(User).filter(User.rating > 5).all()
    #res2 = (select(User).filter(User.rating>5))

    #result = db.execute(res2).scalars().all()
    #for r in result:
     #   print(r.__dict__)
    #res3 = select(User).where(User.last_name.like("M%"))
#
    #result = db.execute(res3).scalars()
#
    #for user in result:
    #    print(user.last_name)

    #res = select(User).where(User.rating.between(2, 5))
    #result = db.execute(res).scalars()
    #for i in result:
    #    print(i.rating)


    #res = select(User).where(and_(User.role_id==3, User.rating > 6))
    #result = db.execute(res).scalars()
    #for user in result:
    #    print(user.role_id, user.rating )
#
    #res = select(User).where(and_(User.role_id==3, User.rating > 6)).order_by(desc(User.rating), User.last_name)
    #result = db.execute(res).scalars()
    #for user in result:
       #print(user.role_id, user.rating, user.last_name)
    #res = select(User.role_id,func.avg(User.rating)).group_by(User.role_id)
    #result = db.execute(res).scalars()
#
    #for row in result:
    #    print(row)

    #us = aliased(element=User, name="us")
    #res = select(us.role_id,func.count(us.id).label("count_of_users")).group_by(us.role_id).having(func.count(us.id)>4)
    #result = db.execute(res).all()
#
    #for r in result:
    #    print( f" id_role:{r.role_id},   count:{r.count_of_users}" )

    #mean_rate_by_autor_sbq = select(func.avg(User.rating).label("user_rating")).where(User.role_id==3).scalar_subquery()
    #main_query = select(User).where(User.rating > mean_rate_by_autor_sbq)
    #result = db.execute(main_query).scalary()
    #print(result)

    mean_rate_by_author_sbq = select(
        func.avg(User.rating).label("user_rating")
    ).where(User.role_id == 3).scalar_subquery()

    # Главный зпрос
    main_query = select(User).where(User.rating > mean_rate_by_author_sbq)
    result = db.execute(main_query).scalars()
    print(result)
    for user in result:
        print(user.last_name, user.rating)

















