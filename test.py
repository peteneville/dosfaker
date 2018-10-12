from faker import Faker
import psycopg2
from service_provider import ServiceProvider

fake = Faker('en_GB')

fake.add_provider(ServiceProvider)



conn = psycopg2.connect(dbname="pathwaysdos_dev", user="postgres",password="postgres", host="localhost")



for x in range(0, 10):
  status_id = fake.statusId()
  restrict_to_referrals = fake.restrictToReferrals()
  open_all_hours = fake.openAllHours()
  public_phone_number = fake.phone_number()
  non_public_phone_number = fake.phone_number()
  fax = fake.phone_number()
  email = fake.email(domain='fakenhs.net')
  url = fake.url()
  created_by = fake.first_name() + fake.last_name()

  print "Status id: " + `status_id` \
    + " restrict to referrals: " + `restrict_to_referrals` \
    + " open all hours: " + `open_all_hours` \
    + " public phone: "  + `str(public_phone_number)` \
    + " non-public phone: "  + `str(non_public_phone_number)` \
    + " Fax: "  + `str(fax)` \
    + " Email: " + `str(email)` \
    + " Web: " + `str(url)` \
    + " Created by: " + `str(created_by)`

  cursor = conn.cursor()
  query =  "INSERT INTO faker.services (statusid, restricttoreferrals, openallhours, publicphone, nonpublicphone, fax, email, web, createdby) \
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
  data = (status_id, restrict_to_referrals, open_all_hours, public_phone_number, non_public_phone_number, fax, email, url, created_by)
  cursor.execute(query, data)

cursor.close()
conn.commit()
