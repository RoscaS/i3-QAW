
class Helpers(object):

    @classmethod
    def check_cash(cls):
        with open('cash_launcher', 'r') as f:
            lines = f.readlines()
            return [i.strip('\n') for i in lines]

    @classmethod
    def cash_append(cls, app_name):
        with open('cashed_apps_with_launcher', 'a') as f:
            f.write(app_name.lower())
