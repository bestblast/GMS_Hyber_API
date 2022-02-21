MASS MESSAGES SENDING
=====================

JSON V2 protocol grants mass sending of Messages in a single request. The maximum number of Recipients in one request is 50,000.
Access details and URLs: 

.. table:: Connection parameters

+---------------------------+---------------------------------------------------------------------------------------------------------------+
| Parameters                | Value                                                                                                         |
+===========================+===============================================================================================================+
| Provider Role             | Server                                                                                                        |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
| Client Role               | Client                                                                                                        |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
| Batch-URL of the API      | https://proxy-{site}.hyber.im/{client_id}/batch      \\                                                       |
|                           | https://proxy-{site}.hyber.im/{client_id}/batch/sync                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
| Broadcast-URL of the API  | https://proxy-{site}.hyber.im/{client_id}/broadcast      \\                                                   |
|                           | https://proxy-{site}.hyber.im/{client_id}/broadcast/sync                                                      |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
| Method                    | POST                                                                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
| HTTP Authentication       | Basic                                                                                                         |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
| Mandatory header          | Content-Type: application/json                                                                                |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
| HTTP Login/Password       | TBA by GMS in technical plan                                                                                  |
+---------------------------+---------------------------------------------------------------------------------------------------------------+

Batch request contains personalized Message text across all communication channels for each User.
Broadcast request contains general text and variables that holds personalized values and can be used for all query parameters.
Examples of mass Messages requests are described in Sections 3.1-3.8.
The HTTP Status 200 OK indicates that your request has been processed successfully by server.
The platform returns a response on your request (Section 3.9).


Send batch Viber+SMS Messages request
-------------------------------------

.. code-block:: json

   {
       "messages": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "text": "Text for all channels, recipient #380961111111"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "text": "Text for all channels, recipient #380962222222"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber",
           "sms"
       ],
       "channel_options": {
           "viber": {
               "ttl": 60,
               "device": "phone",
               "img": "https://example.com/image.png",
               "caption": "Click the button",
               "action": "https://example.com",
               "ctr": false
           },
           "sms": {
               "alpha_name": "GMSU",
               "ttl": 300,
               "ctr": false
           }
       }
   }

Send batch Viber Messages request
---------------------------------

Example of template Message request:

.. code-block:: json

   {
       "messages": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "text": "Templated text for Viber, recipient #380961111111"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "text": "Templated text for Viber, recipient #380962222222"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "ttl": 60,
               "device": "phone",
               "ctr": false
           }
       }
   }

Example of non-template Message request:

.. code-block:: json

   {
       "messages": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "text": "Text for all channels, recipient #380961111111"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "text": "Text for all channels, recipient #380962222222"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "ttl": 60,
               "device": "phone",
               "img": "https://example.com/image.png",
               "caption": "Click the button",
               "action": "https://example.com",
               "ctr": false
           }
       }
   }

Example of Viber Message request with "alpha_name" parameter:

.. code-block:: json

   {
       "messages": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "text": "Text for all channels, recipient #380961111111"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "text": "Text for all channels, recipient #380962222222"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "ttl": 60,
               "device": "phone",
               "alpha_name": "GMSU",
               "img": "https://example.com/image.png",
               "caption": "Click the button",
               "action": "https://example.com",
               "ctr": false
           }
       }
   }

Send batch SMS Messages request
-------------------------------

.. code-block:: json

   {
       "messages": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "text": "Text for all channels, recipient #380961111111"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "text": "Text for all channels, recipient #380962222222"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "sms"
       ],
       "channel_options": {
           "sms": {
               "alpha_name": "GMSU",
               "ttl": 300,
               "ctr": false
           }
       }
   }

Send batch WhatsApp Messages request
------------------------------------

Example of template Message request:

.. code-block:: json

   {
       "messages": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "text": "Templated text for WhatsApp, recipient #380961111111"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "text": "Templated text for WhatsApp, recipient #380962222222"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "whatsapp"
       ],
       "channel_options": {
           "whatsapp": {
               "ttl": 604800,
               "ctr": false
           }
       }
   }

Example of non-template (Session) Message request:

.. code-block:: json

   {
       "messages": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "text": "Session text for WhatsApp, recipient #380961111111"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "text": "Session text for WhatsApp, recipient #380962222222"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "whatsapp"
       ],
       "channel_options": {
           "whatsapp": {
               "ttl": 604800,
               "img": "https://example.com/image.png",
               "img_name": "Name for image",
               "doc": "https://example.com/file.docx",
               "doc_name": "Name for document",
               "audio": "https://example.com/audio.mp3",
               "video": "https://example.com/video.mp4",
               "video_name": "Name for video",
               "latitude": "50.438820",
               "longitude": "30.498916",
               "ctr": false
           }
       }
   }

Send broadcast Viber+SMS Messages request
-----------------------------------------

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Michael",
               "greeting": "Mr. "
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Zoya",
               "greeting": "Ms. "
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber",
           "sms"
       ],
       "channel_options": {
           "viber": {
               "text": "Dear %greeting% %name%! Here is a Viber message for you",
               "ttl": 60,
               "device": "phone",
               "img": "https://example.com/image.png",
               "caption": "Click the button",
               "action": "https://example.com",
               "ctr": false
           },
           "sms": {
               "text": "Dear %greeting% %name%! Here is an SMS",
               "alpha_name": "GMSU",
               "ttl": 300,
               "ctr": false
           }
       }
   }

Send broadcast Viber Messages request
-------------------------------------

Example of template Message request:

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Michael",
               "greeting": "Mr. "
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Zoya",
               "greeting": "Ms. "
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "text": "Dear %greeting% %name%! Here is a Viber templated message for you",
               "ttl": 60,
               "device": "phone",
               "ctr": false
           }
       }
   }

Example of non-template Message request:

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Michael",
               "greeting": "Mr. "
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Zoya",
               "greeting": "Ms. "
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "text": "Dear %greeting% %name%! Here is a Viber message for you",
               "ttl": 60,
               "device": "phone",
               "img": "https://example.com/image.png",
               "caption": "Click the button",
               "action": "https://example.com",
               "ctr": false
           }
       }
   }

Example of Viber Message request with "alpha_name" parameter:

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Michael",
               "greeting": "Mr. "
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Zoya",
               "greeting": "Ms. "
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "text": "Dear %greeting% %name%! Here is a Viber message for you",
               "ttl": 60,
               "device": "phone",
               "alpha_name": "GMSU",
               "img": "https://example.com/image.png",
               "caption": "Click the button",
               "action": "https://example.com",
               "ctr": false
           }
       }
   }

Example of Viber Message request with "File Only" type:

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Name_for_document1.docx",
               "url": "https://example.com/file1.docx"
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Name_for_document2.docx",
               "url": "https://example.com/file2.docx"
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "ttl": 60,
               "device": "phone",
               "file_name": "%name%",
               "action": "%url%",
               "ctr": false
           }
       }
   }

Send broadcast SMS Messages request
-----------------------------------

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Michael",
               "greeting": "Mr. "
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Zoya",
               "greeting": "Ms. "
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "sms"
       ],
       "channel_options": {
           "sms": {
               "text": "Dear %greeting% %name%! Here is an SMS",
               "alpha_name": "GMSU",
               "ttl": 300,
               "ctr": false
           }
       }
   }

Send broadcast WhatsApp Messages request
----------------------------------------

Example of template Message request:

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Michael",
               "greeting": "Mr. "
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Zoya",
               "greeting": "Ms. "
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "whatsapp"
       ],
       "channel_options": {
           "whatsapp": {
               "text": "Dear %greeting% %name%! Here is a WhatsApp templated message for you",
               "ttl": 604800,
               "ctr": false    
           }
       }
   }

Example of non-template (Session) Message request:

.. code-block:: json

   {
       "recipients": [{
               "phone_number": 380961111111,
               "extra_id": "AD-6640-7006",
               "name": "Michael",
               "greeting": "Mr. "
           },
           {
               "phone_number": 380962222222,
               "extra_id": "AD-6640-7007",
               "name": "Zoya",
               "greeting": "Ms. "
           }
       ],
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "whatsapp"
       ],
       "channel_options": {
           "whatsapp": {
               "text": "Dear %greeting% %name%! Here is a WhatsApp session message for you",
               "ttl": 604800,
               "img": "https://example.com/image.png",
               "img_name": "Name for image",
               "doc": "https://example.com/file.docx",
               "doc_name": "Name for document",
               "audio": "https://example.com/audio.mp3",
               "video": "https://example.com/video.mp4",
               "video_name": "Name for video",
               "latitude": "50.438820",
               "longitude": "30.498916",
               "ctr": false    
           }
       }
   }

Response to a Mass Messages request 
-----------------------------------

If the request was sent to the URL https://proxy-{site}.hyber.im/{client_id}/batch or https://proxy-{site}.hyber.im/{client_id}/broadcast you will receive a campaign ID in response as: 

{"job_id": "66591729-cb47-5ef9-964b-949dc6aff84f"}

If the request is sent to the URL https://proxy-{site}.hyber.im/{client_id}/batch/sync or https://proxy-{site}.hyber.im/{client_id}/broadcast/sync you receive details on each Message with their "message_id":

.. code-block:: json
   {
       "messages": [
          {
               "processed": true,
               "phone_number": "380961111111",
               "message_id": "9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
               "extra_id": "AD-6640-7006",
               "accepted": true
           },
           {
               "processed": true,
               "phone_number": "380962222222",
               "message_id": "e5ea7286-6849-52d7-9e1b-8719b736283e",
               "extra_id": "AD-6640-7007",
               "accepted": true
           }
       ]
   }

A description of the response parameters is provided in Section 9.


GET campaign status report
--------------------------

The campaign status request allows you to get information about the processing status of your campaign.
To get campaign status, use the following authorization options and URL:

Table 3.2. Connection parameters  
Parameters	Value
Provider Role	Server
Client Role	Client
Get Job status URL	https://proxy-{site}.hyber.im/{client_id}/status/{job_id}
Method	GET
HTTP Authentication	Basic
HTTP Login/Password	TBA by GMS in technical plan

Example of campaign status:

.. code-block:: json

   {
       "messages": [{
               "time": 1477417299000,
               "phone_number": "380962222222",
               "message_id": "e5ea7286-6849-52d7-9e1b-8719b736283e",
               "extra_id": "AD-6640-7007",
               "processed": false,
               "accepted": true,
               "total_sms_parts": 1,
               "error_text": "SMS expired",
               "error_code": 35015,
               "clicks": 0
           },
           {
               "time": 1477417294667,
               "phone_number": "380961111111",
               "message_id": "9f60ac8f-e721-5027-b838-e6fcb95fcd7a",
               "extra_id": "AD-6640-7006",
               "processed": false,
               "accepted": true,
               "total_sms_parts": 1,
               "delivered_sms_parts": 1,
               "status_text": "SMS delivered",
               "status": 2,
               "substatus": 23,
               "hyber_status": 23011,
               "clicks": 2
           }]
   }

The HTTP Status 200 OK indicates that your request has been processed successfully by server.
A description of the report parameters is provided in Section 8.









