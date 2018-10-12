from faker.providers import BaseProvider


class ServiceProvider(BaseProvider):
    restrict_to_referrals = ('f', 't')
    open_all_hours = ('f', 't')
    status_id =(1,2,3,4,5,6,7)

    def restrictToReferrals(self):
      return self.random_element(self.restrict_to_referrals)

    def openAllHours(self):
      return self.random_element(self.open_all_hours)

    def statusId(self):
      return self.random_element(self.status_id)
