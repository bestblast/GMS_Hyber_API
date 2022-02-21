GET SINGLE MESSAGE DELIVERY REPORT
==================================

The delivery report includes the final status of the Message (including "seen" statuses for Viber and WhatsApp channels).
To GET Message status report, use the following authorization options and URL:

Table 5.1 Connection parameters

===================== ===============================================================================
Parameters            Value
===================== ===============================================================================
Provider Role         Server
Client Role           Client
Get Detailed DR URLs  | https://dr-v2-{site}.hyber.im/{client_id}/api/dr/{message_id}/advanced
                      | https://dr-v2-{site}.hyber.im/{client_id}/api/dr/external/{extra_id}/advanced
Get Simple DR URLs    | https://dr-v2-{site}.hyber.im/{client_id}/api/dr/{message_id}/simple
                      | https://dr-v2-{site}.hyber.im/{client_id}/api/dr/external/{extra_id}/simple
Method                GET
HTTP Authentication   Basic
HTTP Login/Password   TBA by GMS in technical plan
===================== ===============================================================================

GET simple delivery report
--------------------------

Simple Message delivery report may be requested by the Message identifier (received via API in the course of Messages creation: "message_id") or by the additional identifier (set by you in JSON request: "extra_id" parameter). 

To GET the report using Message identifier, use the following URL:

https://dr-v2-{site}.hyber.im/{client_id}/api/dr/{message_id}/simple

To GET the report using the additional identifier, use the following URL:

https://dr-v2-{site}.hyber.im/{client_id}/api/dr/external/{extra_id}/simple

An example of simplified delivery report: 

.. code-block:: json

   {
      "phone_number":"380961111111",
      "last_partner":"sms",
      "message_id":"9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
      "extra_id":"AD-6640-7006",
      "time":1477417294667,
      "status":2,
      "substatus":23,
      "hyber_status":23011,
      "total_sms_parts":1,
      "delivered_sms_parts":1,
      "clicks":2
   }

The HTTP Status 200 OK indicates that your request has been processed successfully by server.
A description of the report parameters is provided in Section 8.

GET detailed delivery report
----------------------------
A detailed Message delivery report may be requested by the Message identifier (received via API in the course of Messages creation: "message_id") or by the additional identifier (set by you in JSON request: "extra_id" parameter). 

To GET the report using Message identifier, use the following URL:

https://dr-v2-{site}.hyber.im/{client_id}/api/dr/{message_id}/advanced

To GET the report using the additional identifier, use the following URL:

https://dr-v2-{site}.hyber.im/{client_id}/api/dr/external/{extra_id}/advanced

An example of detailed delivery report:

.. code-block:: json

   {
      "reports":[
         {
            "phone_number":"380961111111",
            "message_id":"9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
            "extra_id":"AD-6640-7006",
            "time":1477417294667,
            "last_partner":"viber",
            "status":3,
            "substatus":35,
            "hyber_status":35015
         },
         {
            "phone_number":"380961111111",
            "message_id":"9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
            "extra_id":"AD-6640-7006",
            "time":1477417294667,
            "last_partner":"sms",
            "status":2,
            "substatus":23,
            "hyber_status":23011,
            "total_sms_parts":1,
            "delivered_sms_parts":1
         }
      ],
      "started":true,
      "processing":false,
      "delivered_via":"sms",
      "clicks":2,
      "channels":[
         {
            "channel":"viber",
            "ttl":60
         },
         {
            "channel":"sms",
            "ttl":300
         }
      ]
   }

If the Message is not sent to any of the communication channels or has no final delivery status yet, the status of the Message is -1.
The HTTP Status 200 OK indicates that your request has been processed successfully by server.
A description of the report parameters is provided in Section 8.

GET simple and detailed delivery report of template Viber Message
-----------------------------------------------------------------

An example of simplified delivery report: 

.. code-block:: json

   {
      "phone_number":"380961111111",
      "last_partner":"viber",
      "message_id":"9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
      "extra_id":"AD-6640-7006",
      "time":1477417294667,
      "status":2,
      "substatus":23,
      "hyber_status":23043,
      "matching_template_id":6349599,
      "clicks":2
   }

An example of detailed delivery report: 

.. code-block:: json

   {
      "started":true,
      "reports":[
         {
            "time":1477417294667,
            "substatus":23,
            "status":2,
            "phone_number":"380961111111",
            "message_id":"9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
            "matching_template_id":6349599,
            "last_partner":"viber",
            "hyber_status":23043,
            "extra_id":"AD-6640-7006"
         }
      ],
      "processing":false,
      "delivered_via":"viber",
      "clicks":2,
      "channels":[
         {
            "ttl":60,
            "channel":"viber"
         }
      ]
   }

The HTTP Status 200 OK indicates that your request has been processed successfully by server.
A description of the report parameters is provided in Section 8.
