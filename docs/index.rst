======
faker-file
======
**Currencies done right**

.. _List of circulating currencies: https://en.wikipedia.org/wiki/List_of_circulating_currencies

In most payment systems that went international, amounts are represented in
integers, instead of decimals, as they are represented in minor currency units
(smallest units possible).

For `EUR` it is `cent <https://en.wikipedia.org/wiki/Cent_(currency)>`__,
which is 1/100 of a single `Euro <https://en.wikipedia.org/wiki/Euro>`__.
For `MRU` it is `khoums <https://en.wikipedia.org/wiki/Khoums>`__,
which is 1/5 of a single `Ouguiya <https://en.wikipedia.org/wiki/Mauritanian_ouguiya>`__.

List of currencies is generated from a single CSV dump obtained from the
`list of circulating currencies`_ Wikipedia page using the awesome
`wikitable2csv <https://github.com/gambolputty/wikitable2csv>`__.

.. image:: https://img.shields.io/pypi/v/faker-file.svg
   :target: https://pypi.python.org/pypi/faker-file
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/faker-file.svg
    :target: https://pypi.python.org/pypi/faker-file/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/faker-file/workflows/test/badge.svg
   :target: https://github.com/barseghyanartur/faker-file/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/faker-file/badge/?version=latest
    :target: http://faker-file.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/faker-file/#License
   :alt: GPL-2.0-only OR LGPL-2.1-or-later

.. image:: https://coveralls.io/repos/github/barseghyanartur/faker-file/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/barseghyanartur/faker-file?branch=master
    :alt: Coverage

Prerequisites
=============
- Core package requires Python 3.6, 3.7, 3.8 or 3.9.
- `Django integration`_ package (``faker-file.contrib.django_integration``) requires
  Django 2.2, 3.0, 3.1 or 3.2.
- `SQLAlchemy integration`_ package (``faker-file.contrib.sqlalchemy_integration``)
  has been tested with SQLAlchemy 1.4.x.

Documentation
=============
Documentation is available on `Read the Docs
<http://faker-file.readthedocs.io/>`_.

Installation
============
Latest stable version on PyPI:

.. code-block:: sh

    pip install faker-file

Or development version from GitHub:

.. code-block:: sh

    pip install https://github.com/barseghyanartur/faker-file/archive/master.tar.gz

Usage examples
==============
Pure Python
-----------
Using currency classes directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you need numbers back for further calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    import faker-file

    faker-file.EUR.convert_to_currency_units(1_000)
    # 10.0

    faker-file.UGX.convert_to_currency_units(1_000)
    # 1000.0

    faker-file.MRU.convert_to_currency_units(1_000)
    # 200.0

    faker-file.VND.convert_to_currency_units(1_000)
    # 100.0

    faker-file.TND.convert_to_currency_units(1_000)
    # 1.0

    faker-file.JPY.convert_to_currency_units(1_000)
    # 10.0

If you need to display the values and want a nice string back
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    import faker-file

    faker-file.EUR.display_in_currency_units(1_000)
    # '€10.00'

    faker-file.UGX.display_in_currency_units(1_000)
    # 'UGX1,000'

    faker-file.MRU.display_in_currency_units(1_000)
    # 'MRU200.00'

    faker-file.VND.display_in_currency_units(1_000)
    # '₫100'

    faker-file.TND.display_in_currency_units(1_000)
    # 'TND1.000'

    faker-file.JPY.display_in_currency_units(1_000)
    # '¥10'

Custom string formatting
++++++++++++++++++++++++
Based on the specifics of the given currency, displayed numbers may have or
not may have decimal points.

The ``display_in_currency_units`` method accepts optional ``format``,
``locale`` and ``decimal_quantization`` arguments. Most common values for
``format`` are listed in the ``faker-file.constants``.

format
******
**DISPLAY_FORMAT_NUMBER**

Example values: ``'10000'`` or ``'10000.00'``.

**DISPLAY_FORMAT_HUMAN_READABLE**

Displays a human readable number.

Example values: ``'10,000'`` or ``'10,000.00'``.

**DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE**

Displays a human readable number with currency code.

Example values: ``'JPY 10,000'`` or ``'EUR 10,000.00'``.

**DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL**

Displays a human readable number with currency symbol.

Example values: ``'¥ 10,000'`` or ``'€ 10,000.00'``.

A couple of examples:

.. code-block:: python

    from faker-file.constants import *

    faker-file.JPY.display_in_currency_units(
        1_000_000,
        format=DISPLAY_FORMAT_HUMAN_READABLE
    )
    # '10,000'

    faker-file.JPY.display_in_currency_units(
        1_000_000,
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE
    )
    # 'JPY 10,000'

    faker-file.JPY.display_in_currency_units(
        1_000_000,
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL
    )
    # '¥ 10,000'

    faker-file.EUR.display_in_currency_units(
        1_000_000,
        format=DISPLAY_FORMAT_HUMAN_READABLE
    )
    # '10,000.00'

    faker-file.EUR.display_in_currency_units(
        1_000_000,
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE
    )
    # 'EUR 10,000.00'

    faker-file.EUR.display_in_currency_units(
        1_000_000,
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL
    )
    # '€ 10,000.00'

locale
******
.. code-block:: python

     faker-file.JPY.display_in_currency_units(1_000_000_000, locale="nl_NL")
     # 'JP¥\xa010.000.000'

     faker-file.JPY.display_in_currency_units(1_000_000_000, locale="en_US")
     # '¥10,000,000'

     faker-file.EUR.display_in_currency_units(1_000_000_000, locale="nl_NL")
     # '€\xa010.000.000,00'

    faker-file.EUR.display_in_currency_units(1_000_000_000, locale="en_US")
    #  '€10,000,000.00'

    faker-file.AMD.display_in_currency_units(1_000_000_000, locale="en_US")
    # 'AMD10,000,000.00'

    faker-file.AMD.display_in_currency_units(1_000_000_000, locale="hy_AM")
    # '10 000 000,00 ֏'

Working with string representations of the (ISO-4217) currency codes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you need numbers back for further calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from faker-file.shortcuts import convert_to_currency_units

    convert_to_currency_units("EUR", 1_000)
    # 10.0

    convert_to_currency_units("UGX", 1_000)
    # 1000.0

    convert_to_currency_units("MRU", 1_000)
    # 200.0

    convert_to_currency_units("VND", 1_000)
    # 100.0

    convert_to_currency_units("TND", 1_000)
    # 1.0

    convert_to_currency_units("JPY", 1_000)
    # 10.0

If you need to display the values and want a nice string back
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    from faker-file.shortcuts import display_in_currency_units

    display_in_currency_units("EUR", 1_000)
    # '€10.00'

    display_in_currency_units("UGX", 1_000)
    # 'UGX1,000'

    display_in_currency_units("MRU", 1_000)
    # 'MRU200.00'

    display_in_currency_units("VND", 1_000)
    # '₫100'

    display_in_currency_units("TND", 1_000)
    # 'TND1.000'

    display_in_currency_units("JPY", 1_000)
    # '¥10'

By default, exceptions arising from invalid currency codes are
suppressed (``None`` will be returned on invalid currency codes).

If you want to throw exception on invalid currency codes, set ``fail_silently``
to ``False``. The following example will throw a
``faker-file.exceptions.InvalidCurrency`` exception.

.. code-block:: python

    convert_to_currency_units("i-dont-exist", 1_000, fail_silently=False)

The ``display_in_currency_units`` shortcut function also accepts
optional ``format`` argument.

Django integration
------------------
In its basis, Django integration package is a ``CurrencyField`` representing
the ISO-4217 codes of the currencies. If bound to certain number fields
(``SmallIntegerField``, ``IntegerField``, ``BigIntegerField``) holding the
amount in minor currency units, it adds up (magic) methods to the model class
for converting field amounts to major currency units (often simply called
``currency units``).

There are also `template tags and filters`_ for when you need to render
non-model data (for instance, JSON) in templates without prior pre-processing.

Installation
~~~~~~~~~~~~
.. code-block:: sh

    pip install faker-file[django]

Model field
~~~~~~~~~~~
Model definition
^^^^^^^^^^^^^^^^
**Sample model**

*product/models.py*

.. code-block:: python

    from django.db import models
    from faker-file.contrib.django_integration.models import CurrencyField

    class Product(models.Model):

        name = models.CharField(max_length=255)
        price = models.IntegerField()  # Amount in minor currency units
        price_with_tax = models.IntegerField()  # Amount in minor currency units
        currency = CurrencyField(amount_fields=["price", "price_with_tax"])

**Sample data**

.. code-block:: python

    import faker-file
    from product.models import Product
    product = Product.objects.create(
        name="My test product",
        price=100,
        price_with_tax=120,
        currency=faker-file.AMD.uid,
    )

Converting amounts using `magic methods`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You could then refer to the `price` and `price_with_tax` as follows:

.. code-block:: python

    product.price_in_currency_units()
    # 1.0
    product.price_with_tax_in_currency_units()
    # 1.2

Note, that every field listed in the ``amount_fields`` gets a correspondent
model method with suffix ``_in_currency_units`` for converting the field
amounts to (major) currency units.

Converting amounts for display using `magic methods`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You could then refer to the `price` and `price_with_tax` as follows:

.. code-block:: python

    product.price_display_in_currency_units()
    # 'AMD1.00'
    product.price_with_tax_display_in_currency_units()
    # 'AMD1.20'

Note, that every field listed in the ``amount_fields`` gets a correspondent
model method with suffix ``_display_in_currency_units`` for converting the field
amounts to (major) currency units.

Magic methods also accept optional ``format`` argument.

.. code-block:: python

    product = Product.objects.create(
        name="My test product",
        price=100_000,
        price_with_tax=120_000,
        currency=faker-file.EUR.uid,
    )

    product.price_display_in_currency_units(
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL
    )
    # '€ 1,000.00'
    product.price_with_tax_display_in_currency_units(
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE
    )
    # 'EUR 1,200.00'

Combining ``format`` and ``locale`` arguments.

.. code-block:: python

    product.price_display_in_currency_units(
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL,
        locale="nl_NL"
    )
    # '€ 1.000,00'
    product.price_with_tax_display_in_currency_units(
        format=DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE,
        locale="nl_NL"
    )
    # 'EUR 1.200,00'

Limiting the currency choices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On the field level
++++++++++++++++++
You could limit the currency choices as follows:

.. code-block:: python

    currency = CurrencyField(
        amount_fields=["price", "price_with_tax"],
        limit_choices_to=[faker-file.AMD.uid, faker-file.EUR.uid],
    )

Globally
++++++++
You could also override the ``CurrencyField`` choices in the Django settings:

*settings.py*

.. code-block:: python

    faker-file_FIELD_LIMIT_CHOICES_TO=(
        faker-file.AMD.uid,
        faker-file.EUR.uid,
    )

Casting the converted values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you want to explicitly cast the result value to a certain type, provide a
callable ``cast_to`` for the ``CurrencyField``.

For `int` it would be
+++++++++++++++++++++

.. code-block:: python

    currency = CurrencyField(
        amount_fields=("price", "price_with_tax",),
        cast_to=int,
    )

For `float` it would be
+++++++++++++++++++++++

.. code-block:: python

    currency = CurrencyField(
        amount_fields=("price", "price_with_tax",),
        cast_to=float,
    )

For `decimal.Decimal` it would be
+++++++++++++++++++++++++++++++++

.. code-block:: python

    currency = CurrencyField(
        amount_fields=("price", "price_with_tax",),
        cast_to=lambda __v: Decimal(str(__v)),
    )

Customize the choices display format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By default, the following format is used
(``faker-file.utils.get_currency_choices_with_code``):

.. code-block:: python

        [
            ("AMD", "Armenian Dram (AMD)"),
            ("EUR", "Euro (EUR)"),
        ]

If you want to customize that, provide a callable ``get_choices_func`` along:

.. code-block:: python

    from faker-file.utils import get_currency_choices

    currency = CurrencyField(
        amount_fields=("price", "price_with_tax",),
        get_choices_func=get_currency_choices,
    )

It would then have the following format:

.. code-block:: python

        [
            ("AMD", "Armenian Dram"),
            ("EUR", "Euro"),
        ]

Take both ``faker-file.utils.get_currency_choices`` and
``faker-file.utils.get_currency_choices_with_code`` as a good example of how
to customize. You could for instance do something like this:

.. code-block:: python

    import operator
    from typing import List, Tuple, Set, Union

    from babel.numbers import get_currency_symbol
    from faker-file.base import Registry

    def get_currency_choices_with_sign(
            limit_choices_to: Union[Tuple[str, ...], List[str], Set[str]] = None,
            sort_by_key: bool = False,
    ) -> List[Tuple[str, str]]:
        """Get currency choices with code.

        List of choices in the following format::

            [
                ("AMD", "AMD - Armenian Dram"),
                ("EUR", "€ - Euro"),
                ("USD", "$ - US Dollar"),
            ]
        """
        if limit_choices_to is None:
            values = [
                (__key, f"{get_currency_symbol(__key)} - {__value.name}")
                for __key, __value in Registry.REGISTRY.items()
            ]
        else:
            values = [
                (__key, f"{get_currency_symbol(__key)} - {__value.name}")
                for __key, __value in Registry.REGISTRY.items()
                if __key in limit_choices_to
            ]
        if sort_by_key:
            values.sort(key=operator.itemgetter(0))
        else:
            values.sort(key=operator.itemgetter(1))
        return values

And then use it as follows:

.. code-block:: python

    currency = CurrencyField(
        amount_fields=("price", "price_with_tax",),
        get_choices_func=get_currency_choices_with_sign,
    )

Template tags and filters
~~~~~~~~~~~~~~~~~~~~~~~~~
Most of the cases would be covered by the `Model field`_, but it could be
that you will have non-model data (for instance, JSON) that you need to
properly render in the templates (without prior pre-processing). In that case
``faker-file_tags`` template tags/filters library might help.

Template tags prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you want to use templatetags library, you need to add
``faker-file.contrib.django_integration`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        "faker-file.contrib.django_integration",
        # ...
    )

If you want to make use of pre-defined rendering formats, it might be
useful to add ``faker-file.contrib.django_integration.context_processors.constants``
to the ``context_processors``.

.. code-block:: python

    TEMPLATES = [{
        # ...
        "OPTIONS": {
            # ...
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "faker-file.contrib.django_integration.context_processors.constants",
            ],
            # ...
        },
        # ...
    }]

Sample data
^^^^^^^^^^^
.. code-block:: python

    instance = {
        "price": 1_000,
        "price_with_tax": 1_200,
        "currency_code": "EUR",
    }

Without formatting
^^^^^^^^^^^^^^^^^^

Sample template filters template
++++++++++++++++++++++++++++++++
*template_filter_price_in_currency_units.html*

.. code-block:: html

    {% load faker-file_tags %}

    {{ instance.price|convert_to_currency_units:instance.currency_code }}

Sample template filters renderer
++++++++++++++++++++++++++++++++
.. code-block:: python

    from django.template.loader import render_to_string

    render_to_string(
        "template_filter_price_in_currency_units.html", {"instance": instance}
    )

Sample template tags template
+++++++++++++++++++++++++++++
*template_tag_price_in_currency_units.html*

.. code-block:: html

    {% load faker-file_tags %}

    {% convert_to_currency_units instance.price instance.currency_code %}

Sample template tags renderer
+++++++++++++++++++++++++++++
.. code-block:: python

    from django.template.loader import render_to_string

    render_to_string(
        "template_tag_price_in_currency_units.html", {"instance": instance}
    )

With formatting
^^^^^^^^^^^^^^^

Sample template filters template
++++++++++++++++++++++++++++++++
*template_filter_price_display_in_currency_units.html*

.. code-block:: html

    {% load faker-file_tags %}

    {{ instance.price|display_in_currency_units:instance.currency_code }}

Sample template filters renderer
++++++++++++++++++++++++++++++++
.. code-block:: python

    from django.template.loader import render_to_string

    render_to_string(
        "template_filter_price_display_in_currency_units.html", {"instance": instance}
    )

Sample template tags template
+++++++++++++++++++++++++++++
*template_tag_price_display_in_currency_units.html*

.. code-block:: html

    {% load faker-file_tags %}

    {% display_in_currency_units instance.price instance.currency_code %}

You can also display units in specific format (including the currency symbol).
Most common use-cases are pre-defined in ``faker-file.constants`` and if you have
included the correspondent context processor as instructed above, you could
use it as follows:

.. code-block:: html

    {% load faker-file_tags %}

    {% display_in_currency_units instance.price instance.currency_code DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE %}

For the full list of options, see `Custom string formatting`_.

Sample template tags renderer
+++++++++++++++++++++++++++++
.. code-block:: python

    from django.template.loader import render_to_string

    render_to_string(
        "template_tag_price_display_in_currency_units.html", {"instance": instance}
    )

SQLAlchemy integration
----------------------
Similarly to Django integration package, the SQLAlchemy integration package is
a simple ``CurrencyType`` representing the ISO-4217 codes of the currencies.

No magic methods are implemented yet (although planned to). What you get
is a simple SQLAlchemy type for storing the data. For the rest you will have
to make use of the ``faker-file.shortcuts``.

See `examples/sqlalchemy_example/faker-file_admin/models.py <https://github.com/barseghyanartur/faker-file/blob/master/examples/sqlalchemy_example/faker-file_admin/models.py#L50>`_
as a good example.

Installation
~~~~~~~~~~~~
.. code-block:: sh

    pip install faker-file[sqlalchemy]

Model definition
~~~~~~~~~~~~~~~~
**Sample model**

*product/models.py*

.. code-block:: python

    from faker-file.contrib.sqlalchemy_integration.types import CurrencyType
    from . import db  # Standard SQLAlchemy way

    class Product(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Unicode(64), unique=True)
        price = db.Column(db.Integer())
        price_with_tax = db.Column(db.Integer())
        currency = db.Column(CurrencyType())

**Sample data**

.. code-block:: python

    import faker-file
    from product.models import Product
    product = Product(
        name="My test product",
        price=100,
        price_with_tax=120,
        currency=faker-file.AMD.uid,
    )

Supported currencies
====================
Currencies marked with `(*)` are custom (added manually). The rest is obtained
from the already mentioned `list of circulating currencies`_.

.. code-block:: text

    ┌───────────┬──────────────────────────────────────────┐
    │ ISO code  │ Currency                                 │
    ├───────────┼──────────────────────────────────────────┤
    │ AED       │ United Arab Emirates Dirham              │
    ├───────────┼──────────────────────────────────────────┤
    │ AFN       │ Afghan Afghani                           │
    ├───────────┼──────────────────────────────────────────┤
    │ ALL       │ Albanian Lek                             │
    ├───────────┼──────────────────────────────────────────┤
    │ AMD       │ Armenian Dram                            │
    ├───────────┼──────────────────────────────────────────┤
    │ ANG       │ Netherlands Antillean Guilder            │
    ├───────────┼──────────────────────────────────────────┤
    │ AOA       │ Angolan Kwanza                           │
    ├───────────┼──────────────────────────────────────────┤
    │ ARS       │ Argentine Peso                           │
    ├───────────┼──────────────────────────────────────────┤
    │ AUD       │ Australian Dollar                        │
    ├───────────┼──────────────────────────────────────────┤
    │ AWG       │ Aruban Florin                            │
    ├───────────┼──────────────────────────────────────────┤
    │ AZN       │ Azerbaijani Manat                        │
    ├───────────┼──────────────────────────────────────────┤
    │ BAM       │ Bosnia-Herzegovina Convertible Mark      │
    ├───────────┼──────────────────────────────────────────┤
    │ BBD       │ Barbadian Dollar                         │
    ├───────────┼──────────────────────────────────────────┤
    │ BDT       │ Bangladeshi Taka                         │
    ├───────────┼──────────────────────────────────────────┤
    │ BGN       │ Bulgarian Lev                            │
    ├───────────┼──────────────────────────────────────────┤
    │ BHD       │ Bahraini Dinar                           │
    ├───────────┼──────────────────────────────────────────┤
    │ BIF       │ Burundian Franc                          │
    ├───────────┼──────────────────────────────────────────┤
    │ BMD       │ Bermudan Dollar                          │
    ├───────────┼──────────────────────────────────────────┤
    │ BND       │ Brunei Dollar                            │
    ├───────────┼──────────────────────────────────────────┤
    │ BOB       │ Bolivian Boliviano                       │
    ├───────────┼──────────────────────────────────────────┤
    │ BRL       │ Brazilian Real                           │
    ├───────────┼──────────────────────────────────────────┤
    │ BSD       │ Bahamian Dollar                          │
    ├───────────┼──────────────────────────────────────────┤
    │ BTC       │ Bitcoin (*)                              │
    ├───────────┼──────────────────────────────────────────┤
    │ BTN       │ Bhutanese Ngultrum                       │
    ├───────────┼──────────────────────────────────────────┤
    │ BWP       │ Botswanan Pula                           │
    ├───────────┼──────────────────────────────────────────┤
    │ BYN       │ Belarusian Ruble                         │
    ├───────────┼──────────────────────────────────────────┤
    │ BZD       │ Belize Dollar                            │
    ├───────────┼──────────────────────────────────────────┤
    │ CAD       │ Canadian Dollar                          │
    ├───────────┼──────────────────────────────────────────┤
    │ CDF       │ Congolese Franc                          │
    ├───────────┼──────────────────────────────────────────┤
    │ CHF       │ Swiss Franc                              │
    ├───────────┼──────────────────────────────────────────┤
    │ CKD       │ CKD                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ CLP       │ Chilean Peso                             │
    ├───────────┼──────────────────────────────────────────┤
    │ CNY       │ Chinese Yuan                             │
    ├───────────┼──────────────────────────────────────────┤
    │ COP       │ Colombian Peso                           │
    ├───────────┼──────────────────────────────────────────┤
    │ CRC       │ Costa Rican Colón                        │
    ├───────────┼──────────────────────────────────────────┤
    │ CUP       │ Cuban Peso                               │
    ├───────────┼──────────────────────────────────────────┤
    │ CVE       │ Cape Verdean Escudo                      │
    ├───────────┼──────────────────────────────────────────┤
    │ CZK       │ Czech Koruna                             │
    ├───────────┼──────────────────────────────────────────┤
    │ DJF       │ Djiboutian Franc                         │
    ├───────────┼──────────────────────────────────────────┤
    │ DKK       │ Danish Krone                             │
    ├───────────┼──────────────────────────────────────────┤
    │ DOP       │ Dominican Peso                           │
    ├───────────┼──────────────────────────────────────────┤
    │ DZD       │ Algerian Dinar                           │
    ├───────────┼──────────────────────────────────────────┤
    │ EGP       │ Egyptian Pound                           │
    ├───────────┼──────────────────────────────────────────┤
    │ ERN       │ Eritrean Nakfa                           │
    ├───────────┼──────────────────────────────────────────┤
    │ ETB       │ Ethiopian Birr                           │
    ├───────────┼──────────────────────────────────────────┤
    │ EUR       │ Euro                                     │
    ├───────────┼──────────────────────────────────────────┤
    │ FJD       │ Fijian Dollar                            │
    ├───────────┼──────────────────────────────────────────┤
    │ FKP       │ Falkland Islands Pound                   │
    ├───────────┼──────────────────────────────────────────┤
    │ FOK       │ FOK                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ GBP       │ British Pound                            │
    ├───────────┼──────────────────────────────────────────┤
    │ GEL       │ Georgian Lari                            │
    ├───────────┼──────────────────────────────────────────┤
    │ GGP       │ GGP                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ GHS       │ Ghanaian Cedi                            │
    ├───────────┼──────────────────────────────────────────┤
    │ GIP       │ Gibraltar Pound                          │
    ├───────────┼──────────────────────────────────────────┤
    │ GMD       │ Gambian Dalasi                           │
    ├───────────┼──────────────────────────────────────────┤
    │ GNF       │ Guinean Franc                            │
    ├───────────┼──────────────────────────────────────────┤
    │ GTQ       │ Guatemalan Quetzal                       │
    ├───────────┼──────────────────────────────────────────┤
    │ GYD       │ Guyanaese Dollar                         │
    ├───────────┼──────────────────────────────────────────┤
    │ HKD       │ Hong Kong Dollar                         │
    ├───────────┼──────────────────────────────────────────┤
    │ HNL       │ Honduran Lempira                         │
    ├───────────┼──────────────────────────────────────────┤
    │ HRK       │ Croatian Kuna                            │
    ├───────────┼──────────────────────────────────────────┤
    │ HTG       │ Haitian Gourde                           │
    ├───────────┼──────────────────────────────────────────┤
    │ HUF       │ Hungarian Forint                         │
    ├───────────┼──────────────────────────────────────────┤
    │ IDR       │ Indonesian Rupiah                        │
    ├───────────┼──────────────────────────────────────────┤
    │ ILS       │ Israeli New Shekel                       │
    ├───────────┼──────────────────────────────────────────┤
    │ IMP       │ IMP                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ INR       │ Indian Rupee                             │
    ├───────────┼──────────────────────────────────────────┤
    │ IQD       │ Iraqi Dinar                              │
    ├───────────┼──────────────────────────────────────────┤
    │ IRR       │ Iranian Rial                             │
    ├───────────┼──────────────────────────────────────────┤
    │ ISK       │ Icelandic Króna                          │
    ├───────────┼──────────────────────────────────────────┤
    │ JEP       │ JEP                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ JMD       │ Jamaican Dollar                          │
    ├───────────┼──────────────────────────────────────────┤
    │ JOD       │ Jordanian Dinar                          │
    ├───────────┼──────────────────────────────────────────┤
    │ JPY       │ Japanese Yen                             │
    ├───────────┼──────────────────────────────────────────┤
    │ KES       │ Kenyan Shilling                          │
    ├───────────┼──────────────────────────────────────────┤
    │ KGS       │ Kyrgystani Som                           │
    ├───────────┼──────────────────────────────────────────┤
    │ KHR       │ Cambodian Riel                           │
    ├───────────┼──────────────────────────────────────────┤
    │ KID       │ KID                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ KMF       │ Comorian Franc                           │
    ├───────────┼──────────────────────────────────────────┤
    │ KPW       │ North Korean Won                         │
    ├───────────┼──────────────────────────────────────────┤
    │ KRW       │ South Korean Won                         │
    ├───────────┼──────────────────────────────────────────┤
    │ KWD       │ Kuwaiti Dinar                            │
    ├───────────┼──────────────────────────────────────────┤
    │ KYD       │ Cayman Islands Dollar                    │
    ├───────────┼──────────────────────────────────────────┤
    │ KZT       │ Kazakhstani Tenge                        │
    ├───────────┼──────────────────────────────────────────┤
    │ LAK       │ Laotian Kip                              │
    ├───────────┼──────────────────────────────────────────┤
    │ LBP       │ Lebanese Pound                           │
    ├───────────┼──────────────────────────────────────────┤
    │ LKR       │ Sri Lankan Rupee                         │
    ├───────────┼──────────────────────────────────────────┤
    │ LRD       │ Liberian Dollar                          │
    ├───────────┼──────────────────────────────────────────┤
    │ LSL       │ Lesotho Loti                             │
    ├───────────┼──────────────────────────────────────────┤
    │ LYD       │ Libyan Dinar                             │
    ├───────────┼──────────────────────────────────────────┤
    │ MAD       │ Moroccan Dirham                          │
    ├───────────┼──────────────────────────────────────────┤
    │ MDL       │ Moldovan Leu                             │
    ├───────────┼──────────────────────────────────────────┤
    │ MGA       │ Malagasy Ariary                          │
    ├───────────┼──────────────────────────────────────────┤
    │ MKD       │ Macedonian Denar                         │
    ├───────────┼──────────────────────────────────────────┤
    │ MMK       │ Myanmar Kyat                             │
    ├───────────┼──────────────────────────────────────────┤
    │ MNT       │ Mongolian Tugrik                         │
    ├───────────┼──────────────────────────────────────────┤
    │ MOP       │ Macanese Pataca                          │
    ├───────────┼──────────────────────────────────────────┤
    │ MRU       │ Mauritanian Ouguiya                      │
    ├───────────┼──────────────────────────────────────────┤
    │ MUR       │ Mauritian Rupee                          │
    ├───────────┼──────────────────────────────────────────┤
    │ MVR       │ Maldivian Rufiyaa                        │
    ├───────────┼──────────────────────────────────────────┤
    │ MWK       │ Malawian Kwacha                          │
    ├───────────┼──────────────────────────────────────────┤
    │ MXN       │ Mexican Peso                             │
    ├───────────┼──────────────────────────────────────────┤
    │ MYR       │ Malaysian Ringgit                        │
    ├───────────┼──────────────────────────────────────────┤
    │ MZN       │ Mozambican Metical                       │
    ├───────────┼──────────────────────────────────────────┤
    │ NAD       │ Namibian Dollar                          │
    ├───────────┼──────────────────────────────────────────┤
    │ NGN       │ Nigerian Naira                           │
    ├───────────┼──────────────────────────────────────────┤
    │ NIO       │ Nicaraguan Córdoba                       │
    ├───────────┼──────────────────────────────────────────┤
    │ NOK       │ Norwegian Krone                          │
    ├───────────┼──────────────────────────────────────────┤
    │ NPR       │ Nepalese Rupee                           │
    ├───────────┼──────────────────────────────────────────┤
    │ NZD       │ New Zealand Dollar                       │
    ├───────────┼──────────────────────────────────────────┤
    │ OMR       │ Omani Rial                               │
    ├───────────┼──────────────────────────────────────────┤
    │ PAB       │ Panamanian Balboa                        │
    ├───────────┼──────────────────────────────────────────┤
    │ PEN       │ Peruvian Sol                             │
    ├───────────┼──────────────────────────────────────────┤
    │ PGK       │ Papua New Guinean Kina                   │
    ├───────────┼──────────────────────────────────────────┤
    │ PHP       │ Philippine Piso                          │
    ├───────────┼──────────────────────────────────────────┤
    │ PKR       │ Pakistani Rupee                          │
    ├───────────┼──────────────────────────────────────────┤
    │ PLN       │ Polish Zloty                             │
    ├───────────┼──────────────────────────────────────────┤
    │ PND       │ PND                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ PRB       │ PRB                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ PYG       │ Paraguayan Guarani                       │
    ├───────────┼──────────────────────────────────────────┤
    │ QAR       │ Qatari Rial                              │
    ├───────────┼──────────────────────────────────────────┤
    │ RON       │ Romanian Leu                             │
    ├───────────┼──────────────────────────────────────────┤
    │ RSD       │ Serbian Dinar                            │
    ├───────────┼──────────────────────────────────────────┤
    │ RUB       │ Russian Ruble                            │
    ├───────────┼──────────────────────────────────────────┤
    │ RWF       │ Rwandan Franc                            │
    ├───────────┼──────────────────────────────────────────┤
    │ SAR       │ Saudi Riyal                              │
    ├───────────┼──────────────────────────────────────────┤
    │ SBD       │ Solomon Islands Dollar                   │
    ├───────────┼──────────────────────────────────────────┤
    │ SCR       │ Seychellois Rupee                        │
    ├───────────┼──────────────────────────────────────────┤
    │ SDG       │ Sudanese Pound                           │
    ├───────────┼──────────────────────────────────────────┤
    │ SEK       │ Swedish Krona                            │
    ├───────────┼──────────────────────────────────────────┤
    │ SGD       │ Singapore Dollar                         │
    ├───────────┼──────────────────────────────────────────┤
    │ SHP       │ St. Helena Pound                         │
    ├───────────┼──────────────────────────────────────────┤
    │ SLL       │ Sierra Leonean Leone                     │
    ├───────────┼──────────────────────────────────────────┤
    │ SLS       │ SLS                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ SOS       │ Somali Shilling                          │
    ├───────────┼──────────────────────────────────────────┤
    │ SRD       │ Surinamese Dollar                        │
    ├───────────┼──────────────────────────────────────────┤
    │ SSP       │ South Sudanese Pound                     │
    ├───────────┼──────────────────────────────────────────┤
    │ STN       │ São Tomé & Príncipe Dobra                │
    ├───────────┼──────────────────────────────────────────┤
    │ SYP       │ Syrian Pound                             │
    ├───────────┼──────────────────────────────────────────┤
    │ SZL       │ Swazi Lilangeni                          │
    ├───────────┼──────────────────────────────────────────┤
    │ THB       │ Thai Baht                                │
    ├───────────┼──────────────────────────────────────────┤
    │ TJS       │ Tajikistani Somoni                       │
    ├───────────┼──────────────────────────────────────────┤
    │ TMT       │ Turkmenistani Manat                      │
    ├───────────┼──────────────────────────────────────────┤
    │ TND       │ Tunisian Dinar                           │
    ├───────────┼──────────────────────────────────────────┤
    │ TOP       │ Tongan Paʻanga                           │
    ├───────────┼──────────────────────────────────────────┤
    │ TRY       │ Turkish Lira                             │
    ├───────────┼──────────────────────────────────────────┤
    │ TTD       │ Trinidad & Tobago Dollar                 │
    ├───────────┼──────────────────────────────────────────┤
    │ TVD       │ TVD                                      │
    ├───────────┼──────────────────────────────────────────┤
    │ TWD       │ New Taiwan Dollar                        │
    ├───────────┼──────────────────────────────────────────┤
    │ TZS       │ Tanzanian Shilling                       │
    ├───────────┼──────────────────────────────────────────┤
    │ UAH       │ Ukrainian Hryvnia                        │
    ├───────────┼──────────────────────────────────────────┤
    │ UGX       │ Ugandan Shilling                         │
    ├───────────┼──────────────────────────────────────────┤
    │ USD       │ US Dollar                                │
    ├───────────┼──────────────────────────────────────────┤
    │ UYU       │ Uruguayan Peso                           │
    ├───────────┼──────────────────────────────────────────┤
    │ UZS       │ Uzbekistani Som                          │
    ├───────────┼──────────────────────────────────────────┤
    │ VES       │ Venezuelan Bolívar                       │
    ├───────────┼──────────────────────────────────────────┤
    │ VND       │ Vietnamese Dong                          │
    ├───────────┼──────────────────────────────────────────┤
    │ VUV       │ Vanuatu Vatu                             │
    ├───────────┼──────────────────────────────────────────┤
    │ WST       │ Samoan Tala                              │
    ├───────────┼──────────────────────────────────────────┤
    │ XAF       │ Central African CFA Franc                │
    ├───────────┼──────────────────────────────────────────┤
    │ XCD       │ East Caribbean Dollar                    │
    ├───────────┼──────────────────────────────────────────┤
    │ XOF       │ West African CFA Franc                   │
    ├───────────┼──────────────────────────────────────────┤
    │ XPF       │ CFP Franc                                │
    ├───────────┼──────────────────────────────────────────┤
    │ YER       │ Yemeni Rial                              │
    ├───────────┼──────────────────────────────────────────┤
    │ ZAR       │ South African Rand                       │
    ├───────────┼──────────────────────────────────────────┤
    │ ZMW       │ Zambian Kwacha                           │
    ├───────────┼──────────────────────────────────────────┤
    │ ZWB       │ ZWB                                      │
    └───────────┴──────────────────────────────────────────┘

Run the following command in terminal to list all available currencies:

.. code-block:: shell

    faker-file-list-currencies

Custom currencies
=================
To register a new custom currency, do as follows:

.. code-block:: python

    from faker-file.base import BaseCurrency

    class XYZ(BaseCurrency):
        """XYZ - The XYZ currency."""

        uid: str = "XYZ"
        rate: int = 100_000_000

Generating currencies from a CSV dump
=====================================
If `list of circulating currencies`_ is ever updated, grab it the same way,
save as `list_of_circulating_currencies.csv` in the source and run the
following command:

.. code-block:: shell

    faker-file-generate-currencies --skip-first-line

Testing
=======
Simply type:

.. code-block:: sh

    pytest -vvv

Or use tox:

.. code-block:: sh

    tox

Or use tox to check specific env:

.. code-block:: sh

    tox -e py39-django32

Writing documentation
=====================

Keep the following hierarchy.

.. code-block:: text

    =====
    title
    =====

    header
    ======

    sub-header
    ----------

    sub-sub-header
    ~~~~~~~~~~~~~~

    sub-sub-sub-header
    ^^^^^^^^^^^^^^^^^^

    sub-sub-sub-sub-header
    ++++++++++++++++++++++

    sub-sub-sub-sub-sub-header
    **************************

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>

Project documentation
=====================
Contents:

.. contents:: Table of Contents

.. toctree::
   :maxdepth: 20

   index
   changelog
   faker-file

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
