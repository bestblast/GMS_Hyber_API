USER REPLIES (2WAY)
===================

If the Viber or WhatsApp User replies to the Message, its reply can be automatically sent to your URL.

Authorization parameters and URL: 

Table 6.1 Connection parameters 

========================= =========================================
Parameters                Value
========================= =========================================
Provider Role             Client
Client Role               Server
URL for receiving Replies Provided by Client and set up on GMS side
Method                    ``POST``
HTTP Authentication       None
========================= =========================================

Viber User reply
----------------

Example of Viber User reply: 

.. code-block:: json

   {
      "phone": "+380951234567",
      "time": "2016-12-07 20:55:09",
      "channel": "viber",
      "message_id": "d5569ed4-6ff9-5078-8be3-f0b1a1f6e5fe",
      "extra_id": "1883",
      "text_to_subscriber": "text 2 viber",
      "text_from_subscriber": "Reply from viber user"
   }

Example of Viber User reply (deep link):

.. code-block:: json

   {
      "phone": "380951234567",
      "time": "2016-12-07 20:55:09",
      "channel": "viber",
      "text_from_subscriber": "Reply from viber user"
   }

Example of Viber User reply with media file:

.. code-block:: json

   {
      "phone": "380951234567",
      "time": "2016-12-07 20:55:09",
      "channel": "viber",
      "message_id": "d5569ed4-6ff9-5078-8be3-f0b1a1f6e5fe",
      "extra_id": "1883",
      "text_to_subscriber": "text 2 viber",
      "file_name": "Name_for_document.docx",
      "media": "https://example.com/file.docx"
   }

A description of the report parameters is provided in Section 8.

The links storage time of images, audios, videos, files, which were sent by Users, is 1 day.

WhatsApp User reply
-------------------

Example of WhatsApp User reply:

.. code-block:: json

   {
      "channel": "whatsapp",
      "phone": "380110000000",
      "time": "2019-11-26T08:13:39Z",
      "umid": 91dbb1a6-2410-ea11-8153-022a22cc1c71",
      "text_from_subscriber": "Test reply"
   }

User replies can be in the following combinations: 

- "text_from_subscriber"
- "image_url"
- "video_url"
- "audio_url"
- "doc_url" + "text_from_subscriber"
- "location"

A description of the report parameters is provided in Section 8.

The links storage time of images, audios, videos, files, which were sent by Users, is 1 day.

