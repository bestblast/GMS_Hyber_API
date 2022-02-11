SINGLE MESSAGES SENDING
=======================

JSON V2 protocol allows you to use multiple communication channels with your audience simultaneously: PUSH, messenger apps, and SMS. If the Message is delivered by any channel, further sending of the Message to other channels is stopped. 
Access details and URLs: 

Table 2.1. Connection parameters
Parameters	Value
Provider Role	Server
Client Role	Client
URL of the API	https://api-v2-{site}.hyber.im/{client_id}

Method	POST
HTTP Authentication	Basic
Mandatory header	Content-Type: application/json
HTTP Login/Password	TBA by GMS in technical plan

Query parameters are divided into two types: mandatory and optional. If at least one mandatory parameter is missing, the request is not accepted by platform. Each of the Message communication channels has its own unique parameters. A description of all request parameters is provided in Section 8. 
Examples of single Messages requests are described in Sections 2.1-2.5.
The HTTP Status 200 OK indicates that your request has been processed successfully by server.
The platform returns a response on your request (Section 2.6).

Send Push+Viber+SMS Message request 
-----------------------------------

.. code-block:: json

   {
      "phone_number":380961111111,
      "extra_id":"AD-6640-7006",
      "callback_url":"https://send-dr-here.com",
      "start_time":"2020-12-12 10:10:10+03:00",
      "tag":"Campaign name",
      "division_code":"Division code",
      "channels":[
         "push",
         "viber",
         "sms"
      ],
      "channel_options":{
         "push":{
            "text":"Text for Push",
            "ttl":60,
            "title":"Title for Push",
            "img":"https://example.com/image.png",
            "caption":"Click the button",
            "action":"https://example.com",
            "ctr":false
         },
         "viber":{
            "text":"Text for Viber",
            "ttl":60,
            "device":"phone",
            "img":"https://example.com/image.png",
            "caption":"Click the button",
            "action":"https://example.com",
            "ctr":false
         },
         "sms":{
            "text":"Text for SMS",
            "alpha_name":"GMSU",
            "ttl":300,
            "ctr":false
         }
      }
   }
Send Viber+SMS Message request 
------------------------------

.. code-block:: json

   {
       "phone_number": 380961111111,
       "extra_id": "AD-6640-7006",
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
               "text": "Text for Viber",
               "ttl": 60,
               "device": "phone",
               "img": "https://example.com/image.png",
               "caption": "Click the button",
               "action": "https://example.com",
               "ctr": false
           },
           "sms": {
               "text": "Text for SMS",
               "alpha_name": "GMSU",
               "ttl": 300,
               "ctr": false
           }
       }
   }

Send Viber Message request
-------------------------- 

Example of template Message request (only text is specified):

.. code-block:: json

   {
      "phone_number":380961111111,
      "extra_id":"AD-6640-7006",
      "callback_url":"https://send-dr-here.com",
      "start_time":"2020-12-12 10:10:10+03:00",
      "tag":"Campaign name",
      "division_code":"Division code",
      "channels":[
         "viber"
      ],
      "channel_options":{
         "viber":{
            "text":"Templated text for Viber",
            "ttl":60,
            "ctr":false
         }
      }
   }

Example of non-template Message request:

.. code-block:: json

   {
       "phone_number": 380961111111,
       "extra_id": "AD-6640-7006",
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "text": "Text for Viber",
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
       "phone_number": 380961111111,
       "extra_id": "AD-6640-7006",
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "viber"
       ],
       "channel_options": {
           "viber": {
               "text": "Text for Viber",
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
       "phone_number": 380961111111,
       "extra_id": "AD-6640-7006",
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
               "file_name": "Name_for_document.docx",
               "action": "https://example.com/file.docx",
               "ctr": false
           }
       }
   }

Send SMS Message request
------------------------

.. code-block:: json

   {
       "phone_number": 380961111111,
       "extra_id": "AD-6640-7006",
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "sms"
       ],
       "channel_options": {
           "sms": {
               "text": "Text for SMS",
               "alpha_name": "GMSU",
               "ttl": 300,
               "ctr": false
           }
       }
   }

Send WhatsApp Message request
----------------------------- 

Example of template Message request:

.. code-block:: json

   {
       "phone_number": 380961111111,
       "extra_id": "AD-6640-7006",
       "callback_url": "https://send-dr-here.com",
       "start_time": "2020-12-12 10:10:10+03:00",
       "tag": "Campaign name",
       "division_code": "Division code",
       "channels": [
           "whatsapp"
       ],
       "channel_options": {
           "whatsapp": {
               "text": "Templated text for WhatsApp",
               "ttl": 604800,
               "ctr": false
           }
       }
   }

Example of non-template (Session) Message request:

.. code-block:: json

   {
      "phone_number":380961111111,
      "extra_id":"AD-6640-7006",
      "callback_url":"https://send-dr-here.com",
      "start_time":"2020-12-12 10:10:10+03:00",
      "tag":"Campaign name",
      "division_code":"Division code",
      "channels":[
         "whatsapp"
      ],
      "channel_options":{
         "whatsapp":{
            "text":"Session text for WhatsApp",
            "img":"https://example.com/image.png",
            "img_name":"Name for image",
            "doc":"https://example.com/file.docx",
            "doc_name":"Name for document",
            "audio":"https://example.com/audio.mp3",
            "video":"https://example.com/video.mp4",
            "video_name":"Name for video",
            "latitude":"50.438820",
            "longitude":"30.498916",
            "ttl":604800,
            "ctr":false
         }
      }
   }

Response to a single Message request  
------------------------------------

If the request is correct, you receive the following response to your request: 

.. code-block:: json

   {"message_id":"9f60ac8f-e721-5027-b838-e6fcb95fcd7a"}

If the request contains an error or inconsistency with the connection settings, you receive the following response:

.. code-block:: json
   {"error_code":36024,"error_text":"Phone number incorrect"}

A description of the response parameters is provided in Section 9. 


