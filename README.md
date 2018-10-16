# DoS Faker
This project makes use of the Python Faker library (see https://github.com/joke2k/faker for further info).

The purpose of this project is to generate a large amount of fake test data suitable for loading into the DoS postgres database.
This project started as a hackday idea and will hopefully be worked on to completion.



## Current state

The initial aim was to populate the services table such that the various web pages are able to operate with the fake data. Currently, service records are being created, but only viewable in the service admin page. This is due to the code not currently creating the associated records in the join tables.

## Summary of what's needed to progress further

- Populate associated join tables
- Update the provider (and use of) to generate a unique (across all the service records generated) ODS code
- Further work on provider so that combinations data for a service record make sense. For example, the name, type etc should be related
- Generate postcodes with eastings and northings for the postcode. Whilst this data exists in the DoS, it is paid for. We can either generate the data from the existing dataset (and not publish in the open) or try and identify an alternative open source postcode with points (northing/eastings or lat/long) dataset.
