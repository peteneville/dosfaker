from faker import Faker
import psycopg2
from service_provider import ServiceProvider

fake = Faker()

fake.add_provider(ServiceProvider)


print fake.statusId()






#conn = psycopg2.connect(dbname="pathwaysdos_dev", user="postgres",password="postgres", host="localhost")

#for x in range(0, 10):
  #print fake.name()
  #print fake.address()


  #cursor = conn.cursor()
  #query =  "INSERT INTO faker.services (name) VALUES (%s);"
  #data = (fake.name())

  #cursor.execute(query, [data])

#cursor.close()
#conn.commit()
