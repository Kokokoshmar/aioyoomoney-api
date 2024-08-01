API Yoomoney (async) - unofficial python library
==================================================
`This repository <https://github.com/AlekseyKorshuk/yoomoney-api>`_ was taken as a basis.

This is an unofficial `YooMoney <https://yoomoney.ru>`_ API python library.

==========
Summary
==========

- `Introduction`_

- `Features`_

- `Installation`_

- `Quick start`_

  #. `Access token`_

  #. `Account information`_

  #. `Operation history`_

  #. `Operation details`_

  #. `Quickpay forms`_

============
Introduction
============

This repository is based on the official documentation of `YooMoney <https://yoomoney.ru/docs/wallet>`__.

========
Features
========

Implemented methods:

- `Access token`_ - Getting an access token
- `Account information`_ - Getting information about the status of the user account.
- `Operation history`_ - This method allows viewing the full or partial history of operations in page mode. History records are displayed in reverse chronological order (from most recent to oldest).
- `Operation details`_ - Provides detailed information about a particular operation from the history.
- `Quickpay forms`_ - The YooMoney form is a set of fields with information about a transfer. You can embed payment form into your interface (for instance, a website or blog). When the sender pushes the button, the details from the form are sent to YooMoney and an order for a transfer to your wallet is initiated.

============
Installation
============

You can install with:

.. code:: shell

    pip install aioyoomoney-api


You can install from source with:

.. code:: shell

    git clone https://github.com/Kokokoshmar/aioyoomoney-api
    cd aioyoomoney-api
    pip install .

===========
Quick start
===========

Access token
************

First of all we need to receive an access token.

1. Log in to your YooMoney wallet with your username. If you do not have a wallet, `create it <https://yoomoney.ru/reg>`_.
2. Go to the `App registration <https://yoomoney.ru/myservices/new>`_ page.
3. Set the application parameters. Save CLIENT_ID and YOUR_REDIRECT_URI for net steps
4. Click the Confirm button.
5. Paste CLIENT_ID, REDIRECT_URI and CLIENT_SECRET insted of YOUR_CLIENT_ID, YOUR_REDIRECT_URI and YOUR_CLIENT_SECRET. Choose scopes and run code.
6. Follow all steps from the program.

.. code:: python

    from aioyoomoney import authorize

    token = authorize(
        client_id=CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        client_secret=CLIENT_SECRET,
        scope=[
            "account-info",
            "operation-history",
            "operation-details",
            "incoming-transfers",
            "payment-p2p",
        ]
    )

    print(token)

You are done with the most difficult part!

Account information
*******************

Paste YOUR_TOKEN and run this code:

.. code:: python

    import asyncio

    from aioyoomoney import Client


    async def client_info():
        client = Client(YOUR_TOKEN)

        account = await client.account_info()

        print(f"Account: {account.id}")
        print(f"Balance: {account.balance}")
        print(f"Currency: {account.currency}")
        print(f"Account Status: {account.account_status}")
        print(f"Account Type: {account.account_type}")
        print(f"Balance Details: {account.balance_details}")
        print(f"Cards Linked: {account.cards_linked}")


    asyncio.run(client_info())


Operation history
*****************

Paste YOUR_TOKEN and run this code:

.. code:: python

    import asyncio

    from aioyoomoney import Client
    from dataclasses import fields


    async def get_operation_history():
        client = Client(YOUR_TOKEN)

        history = await client.operation_history()
        print("Next record:", history.next_record)
        for operation in history.operations:
            for field in fields(operation):
                if field.name != "kwargs":
                    print(field.name, '->', operation[field.name])

            for key, value in operation.kwargs.items():
                print(key, '->', value)

            print("================================")


    asyncio.run(get_operation_history())


Operation details
*****************

Paste YOUR_TOKEN with an OPERATION_ID (example: 670244335488002312):

.. code:: python
    import asyncio

    from aioyoomoney import Client
    from dataclasses import fields


    async def get_operation_details():
        client = Client(YOUR_TOKEN)

        operation = await client.operation_details(OPERATION_ID)
        for field in fields(operation):
            if field.name != "kwargs":
                print(field.name, '->', operation[field.name])

        for key, value in operation.kwargs.items():
            print(key, '->', value)


    asyncio.run(get_operation_details())


Quickpay forms
**************

Run this code:

.. code:: python
    import asyncio

    from aioyoomoney import Quickpay


    async def quickpay():
        async with Quickpay(
            receiver="899999999999999",
            quickpay_form="shop",
            targets="Sponsor this project",
            payment_type="SB",
            sum=10,
            form_comment='test',
            label="label"
        ) as quickpay:
            print(quickpay.redirected_url)
            print(quickpay.base_url)
            print(quickpay.payload)


    asyncio.run(quickpay())
