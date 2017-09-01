"""Classes for melon orders."""

from random import randint

from datetime import datetime


class AbstractMelonOrder(object):
    """Parent class for a melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        if qty < 100:
            self.qty = qty
        else:
            raise TooManyMelonsError(" No more than 100 many melons!")
        self.shipped = False

    def get_base_price(self):

        base_price = randint(5, 9)
        print base_price

        now_datetime = datetime.now()

        if (8 <= now_datetime.hour <= 13
            and 0 <= now_datetime.weekday() <= 4):
            base_price += 4

        if self.species == "Christmas":
            base_price *= 1.5

        print base_price

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        total = (1 + self.tax) * self.qty * self.get_base_price()

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3

        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        """ Initializes government-subsized melon orders"""

        super(GovernmentMelonOrder, self).__init__(species, qty)

        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """ Record inspection status, true or false"""

        self.passed_inspection = passed

class TooManyMelonsError(ValueError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

