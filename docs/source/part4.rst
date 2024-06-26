RECEIVE MESSAGE DELIVERY REPORT
===============================

Receive single delivery report
------------------------------

As soon as the status is updated in GMS system, the delivery report is sent to your URL in JSON format.

The report contains the final status of the Message. The only exception is the "seen" status 
for Viber and WhatsApp channels. 

There are two ways to receive "seen" statuses:
- Automatic sending to your URL. To activate this functionality, you need to send a request to your manager.
- The request using GET method (Section 5).

Example of report:

.. code-block:: json

   {
      "number": 380961111111,
      "time": 1477417294667,
      "status": 2,
      "substatus": 23,
      "hyber_status": 23011,
      "message_id": "9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
      "extra_id": AD-6640-7006",
      "sent_via": "sms",
      "total_sms_parts": 1,
      "delivered_sms_parts": 1
   }

A description of the report parameters is provided in Section 8.

Receive batched delivery report
-------------------------------

As soon as the status is updated in GMS system, Message delivery reports are stored in the batch. The batch is sent to your URL in JSON-format (via http or https). The number of reports in the batch and the period of its sending are configured on GMS side.

Example of report:

.. code-block:: json

   [
      {
         "number": "380961111111",
         "time": 1477417294667,
         "status": 2,
         "substatus": 23,
         "hyber_status": 23011,
         "message_id": "9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
         "extra_id": "AD-6640-7006",
         "sent_via": "sms"
      },
      {
         "number": "380962222222",
         "time": 1477417299000,
         "status": 3,
         "substatus": 35,
         "hyber_status": 35015,
         "message_id": "e5ea7286-6849-52d7-9e1b-8719b736283e",
         "extra_id": "AD-6640-7007",
         "sent_via": "sms"
      },
      {
         "number": "380963333333",
         "time": 1477417299050,
         "status": 2,
         "substatus": 23,
         "hyber_status": 23033,
         "message_id": "8a3ff6c5-a1fb-4849-a54b-3c488753cb8b",
         "extra_id": "AD-6640-7008",
         "sent_via": "viber"
      }
   ]

A description of the report parameters is provided in Section 8.

Receive delivery report of template Viber Message
-------------------------------------------------

As soon as the status is updated in GMS system, the delivery report is sent to your URL in JSON format.

If the sent Message matches the template, you receive the template ID in the "matching_template_id" field:

.. code-block:: json

   {
      "number": "380961111111",
      "time": 1477417294667,
      "status": 2,
      "substatus": 23,
      "hyber_status": 23043,
      "message_id": "9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
      "extra_id": "AD-6640-7006",
      "sent_via": "viber",
      "matching_template_id": 6349599
   }

If the Message does not match the template, you receive the value 0 in the field "matching_template_id": 

.. code-block:: json

   {
      "number": "380961111111",
      "time": 1477417294667,
      "status": 2,
      "substatus": 23,
      "hyber_status": 23043,
      "message_id": "9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
      "extra_id": "AD-6640-7006",
      "sent_via": "viber",
      "matching_template_id": 0
   }
   
A description of the report parameters is provided in Section 8.
