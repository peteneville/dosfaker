from faker import Faker
import psycopg2
import random
from service_provider import ServiceProvider

fake = Faker('en_GB')

fake.add_provider(ServiceProvider)



conn = psycopg2.connect(dbname="pathwaysdos_dev", user="postgres",password="postgres", host="localhost")



for x in range(0, 1):
  status_id = fake.statusId()
  restrict_to_referrals = fake.restrictToReferrals()
  # open_all_hours = fake.openAllHours()
  open_all_hours = 't'
  public_phone_number = fake.phone_number()
  non_public_phone_number = fake.phone_number()
  fax = fake.phone_number()
  email = fake.email(domain='fakenhs.net')
  url = fake.url()
  created_by = fake.first_name() + fake.last_name()
  modified_by = fake.first_name() + fake.last_name()
  public_referral_instructions = fake.text(200)
  telephone_triage_referral_instructions = fake.text(200)
  uid = random.randint(100000,999999)
  name = 'todo'
  ods_code = 'todo'
  address = fake.address()
  town = fake.city_prefix() + fake.city_suffix()
  #postcode = fake.postcode()
  postcode = 'EX2 5SE'
  #easting = random.randint(400000,500000)
  #northing = random.randint(400000,500000)
  easting = 294510
  northing = 90111
  type_id = 7
  parent_id = 6
  sub_region_id = 6

  print "Status id: " + `status_id` \
    + " restrict to referrals: " + `restrict_to_referrals` \
    + " open all hours: " + `open_all_hours` \
    + " public phone: "  + `str(public_phone_number)` \
    + " non-public phone: "  + `str(non_public_phone_number)` \
    + " Fax: "  + `str(fax)` \
    + " Email: " + `str(email)` \
    + " Web: " + `str(url)` \
    + " Created by: " + `str(created_by)` \
    + " Public referral instructions: " + public_referral_instructions \
    + " Telephone triage referral instructions: " + telephone_triage_referral_instructions \
    + " UID: " + `uid` \
    + " Name: " + name \
    + " ODSCode: " + ods_code \
    + " Address: " + address \
    + " Town: " + town \
    + " Postcode: " + postcode

  cursor = conn.cursor()
  query =  "INSERT INTO pathwaysdos.services (statusid, restricttoreferrals, openallhours, publicphone, nonpublicphone, fax, email, web, createdby,  \
  publicreferralinstructions, telephonetriagereferralinstructions, name, odscode, address, town, postcode, easting, northing, typeid, uid, \
  modifiedby, subregionid, parentid) \
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
  data = (status_id, restrict_to_referrals, open_all_hours, public_phone_number, non_public_phone_number, fax, email, url, created_by, \
  public_referral_instructions, telephone_triage_referral_instructions, name, ods_code, address, town, postcode, easting, northing, type_id, uid, \
  modified_by, parent_id, sub_region_id)
  cursor.execute(query, data)

cursor.close()
conn.commit()
