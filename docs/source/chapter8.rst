DESCRIPTION OF THE REQUEST PARAMETERS
=====================================

There are the following parameter types:

- String. Example: "text": "Text for Viber"
- Number. Example: "phone_number": 380962222222
- Boolean. Example: "ctr": false , "ctr": true

Table 8.1. Description of the request parameters

.. tabularcolumns:: |p{1cm}|p{4cm}|p{2cm}|p{10cm}|

.. table:: Description of the request parameters
  :class: longtable

== =============== ========= =======================================================================
№  Name            Mandatory Description 
== =============== ========= =======================================================================
Main
----------------------------------------------------------------------------------------------------
1  phone_number    Yes       Phone number of User. It is given in the international format without 
                             the «+» sign 
2  channels        Yes       List of Message delivery channels. Any combination without duplicates, 
                             e.g. **Viber + SMS** or **Push + Viber + SMS**
3  channel_options Yes       Have to be specified for each communication channel
4  messages        Yes       The list of phone numbers of Users and texts will be transmitted to all
                             communication channels for batch request
5  recipients      Yes       List of parameters for personalized campaign for broadcast request
6  extra_id        No        | External identifier of the Message (specified by you). 
                             | Maximum length: 64 characters
7  callback_url    No        | Message reports will be sent to this URL. 
                             | Maximum length: 256 characters 
8  start_time      No        Scheduled date of campaign start. Shall be specified in the following
                             format: "YYYY-MM-DD hh:mm:ss±hh:mm". If the difference with time
                             according to Greenwich Mean Time (in the format +03:00) is not
                             specified, then the difference according to Kyiv time is calculated
9  tag             No        | Campaign name.
                             | Maximum length: 64 characters 
10 division_code   No        | Access group code. Used to separate statistics on Messages for child
                               users of the web-interface. 
			     | Maximum length: 100 characters.
                             | Statistics are separated only by pre-generated code, which is
                               configured on the "Access groups" tab of the client web-interface.
11 ctr             No        | Counting clicks on the link. Choosing this option will
                               automatically convert your URL to a unique shortened/elongated link
                               for each separate phone number. By using this option, you are
                               solely responsible for the alteration of your link(s) and subsequent
			       results. Boolean value (true / false). true value activates counting
			       clicks on the link. The parameter must be specified separately for 
			       each of the channels of sending the Message. URL conversion and 
			       clicks counting occur in the following query parameters:
                             | "viber": ["text", "action"],
                             | "sms": ["text"],
                             | "push": ["text", "action"],
                             | "whatsapp": ["text"]
                             | If the parameter is not specified or it is false, the link is not 
			       converted and clicks are not counted
                             | Converted URL length: 28 characters
                             | The converted URL is available within three months since the start
			       of sending the Message and clicks on the link are counted for the 
			       first fourteen days.
                             | Viber channel parameters 
== =============== ========= =======================================================================

10 text            No        Viber Message text. Text requirements - up to 1000 characters (Cyrillic, Latin), including emoji codes and specific markdowns.You can format your message by adding specific markdowns(only users with Viber version 14.6 and above). Bold - asterisk markdown. String to be sent:"*Text for Viber*", Result: Text for Viber Italics - underscore markdown. String to be sent:"_Text for Viber_", Result: Text for Viber Strikethrough - tilde markdown. String to be sent:"~Text for Viber~", Result: Text for Viber Monospace - three backticks markdown. String to be sent:"```Text for Viber```", Result: Text for Viber
11 ttl             Yes       |Message lifetime in seconds: 
                             |Viber: 40..86400
                             |We recommend not setting a low TTL. This will help prevent  cases where users will receive both Viber and SMS messages.
                             |Recommended minimum for TTL is 60 seconds.
12 device          No        |Selection of devices for delivery Messages (only for Viber ID 1way).
                             |"all" - delivery to all devices 
                             |"phone" - delivery only to smartphones
                             |The template message can only be delivered to smartphone, so the device parameter is ignored.
                             |If this parameter is not specified, then the parameter takes the
                             |value from the settings on Hyber web-interface.
13 alpha_name      No        Value of field alpha_name specifies Viber service. Link of "alpha_name" to Viber service is set on GMS side.  
14 img             No        URL of an image on the Internet. Maximum length:256characters 
15 caption         No        Name of caption. Maximum length:30characters
16 action          No        |URL inside the button. Maximum length:256characters. 
                             |You can utilize this if you wish to direct a User to the following:
                             |Direct a User to the webpage or a link to a file: http://example.com
                             |Start Viber call. Opens the Viber keypad with the phone number that you entered in the request: "viber://keypad?number=380961111111"
                             |Start a call. Opens the phone number, that you entered in the request: tel:+380961111111
                             |Open a 1on1 chat - Opens a 1on1 chat with the sender (the sender needs to have a 2way account): "viber://chat?service=3016"
                             |Open Viber QR scanner. Opens a QR scanner through Viber. Tapping the button will open the camera to capture a QR code: "viber://more/qr"
17 file_name       No        Name of file. Maximum length:25characters.
The name must contain a file extension.
The following extensions are allowed for the following file types:
 Documents: .doc, .docx, .rtf, .dot, .dotx, .odt ,odf, .fodt, .txt, .info. Example: "File_name.docx"
 PDF: .pdf, .xps, .pdax, .eps. Example: "File_name.pdf"
 Spreadsheets: .xls, .xlsx, .ods, .fods, .csv, .xlsm, .xltx. Example: "File_name.xlsx"
Maximum file size: 200Mb.
SMS channel parameters  
18 text  Yes  SMS Message text.
 Text requirements - Cyrillic characters (up to 335 characters), Latin characters (up to 765 characters) 
19 ttl  Yes  Message lifetime in seconds:
 SMS:300..259200 
20 alpha_name  Yes  Alphanumeric name. 
 Maximum length is 11 characters, may begin with a number
 Alphanumeric name may consist of GSM7 bitdefault alphabet table characters only
WhatsApp channel parameters 
21 text  No  WhatsApp Message text. 
Text requirements - up to 1000 characters (Cyrillic, Latin), including emoji codes and specific markdowns.
You can format your message by adding specific markdowns.
 Bold - asterisk markdown. String to be sent:
"*Session text for WhatsApp*", Result: Session text for WhatsApp
 Italics - underscore markdown. String to be sent:
"_Session text for WhatsApp_", Result: Session text for WhatsApp
 Strikethrough - tilde markdown. String to be sent:
"~Session text for WhatsApp~", Result: Session text for WhatsApp
 Monospace - three backticks markdown. String to be sent:
"```Session text for WhatsApp```", Result: Session text for WhatsApp
22 ttl  Yes  Message lifetime in seconds: 
 WhatsApp: 604800 
23 img  No  URL of an image on the Internet. 
 Maximum length:256characters 
24 img_name  No  Text under the image. 
 Maximum length: 1000 characters
25 doc  No  URL of a file on the Internet. 
 Maximum length:256characters 
26 doc_name  No  Text under the file. 
 Maximum length: 1000 characters 
27 audio  No  URL of an audio on the Internet. 
 Maximum length:256characters 
28 video  No  URL of a video on the Internet. 
 Maximum length:256characters  
29 video_name  No  Text under the video. 
 Maximum length: 1000 characters 
30 latitude No  Latitude coordinates. 
 Numeric value from -90 to 90 
31 longitude No  Longitude coordinates. 
 Numeric value from -180 to 180 
Push channel parameters  
32 text  Yes  Push Message text. 
 Text requirements – up to 1000 characters (Cyrillic and Latin) 
33 ttl  Yes  Message lifetime in seconds: Push: 30..86400 
34 title  Yes  Title of Message. 
 Maximum length:20characters 
35 img  No  URL of an image on the Internet. Maximum length:256characters 
36 caption  No  Name of caption. Maximum length: 30characters
37 action  No  URL inside the button. Maximum length: 256characters 




Table 8.2. Description of the response parameters
№  Name Description
1 message_id Message identifier.
 Set in UUID format
2 phone_number User`s phone number. 
 It is given in the international format without the «+» sign
3 extra_id External identifier of the Message (specified by you) 
4 job_id Campaign identifier.
 Set in UUID format 
5 error_code  Error code.
 The list of codes is provided in Section 9

6 error_text Short description of the error code
7 processed Boolean value (true/false).
 It is true only if the Message is being processed
 It is false if processing of the Message has not been started 
8 accepted Boolean value (true/false).
 It is true only if the Message is accepted by platform 
 It is false if the Message is rejected by platform 

Table 8.3. Description of Message delivery report parameters 
№ Name  Description 
1 number 
phone_number User`s phone number.
 It is given in the international format without the «+» sign
2 time Unix time stamp for the last action of a communication channel
3 message_id Message identifier
4 extra_id External identifier of the Message (specified by you)
5 status Simplified status of the Message.
 The list of statuses is provided in Section 9

6 substatus Extended Message status.
 The list of statuses is provided in Section 9

7 hyber_status Detailed Message status. 
 The list of statuses is provided in Section 9 

8 sent_via The last channel of Message delivery.
 If Message is blocked by the Platform – the value of the field is "hyber"
9 total_sms_parts The total number of parts of the SMS-Message
10 delivered_sms_parts Number of delivered parts of SMS-Message.
 If there is no Message sent to SMS channel, this parameter is missing
11 matching_template_id Matching Template ID, which specifies the Viber template number.  
 If the Message does not match any template - the value in this field is 0
12 status_text Short description of the status of the Message
13 error_text Short description of the error
14 error_code Error code.
 The list of codes is provided in Section 9  

15 processed Boolean value (true/false).
 It is true only if the Message is being processed  
 It is false if processing of the Message has not been started
16 accepted Boolean value (true/false).
 It is true only if the Message is accepted by platform 
 It is false if the Message is rejected by platform 
17 last_partner The last channel of Message delivery. 
 If the Message is accepted but has not got final status or it is blocked by the Platform – the value of the field is "hyber" 
 For a detailed report (advanced), this parameter is specified for each communication channel
18 delivered_via The last channel of Message delivery.
 If the Message is accepted but has not got final status or it is blocked by the Platform – the value of the field is "hyber"
19 started Boolean value (true/false). 
 It is false if processing of the Message either has not started or started with delay
20 processing Boolean value (true/false).
 It is true only if the Message is being processed
 It is false if processing of the Message either has not been started or already ended
21 channel Message sending channel
22 ttl Message lifetime in seconds for each of channels
23 clicks Number of clicks on links.
 If the "ctr" parameter is not specified in the request or is false, the "clicks" parameter will be missing

Table 8.4. Description of User reply parameters 
№ Name  Description 
1 phone User`s phone number. 
 It is given in the international format without the «+» sign
2 time User’s reply date and time.
 According to Kyiv local time for Viber User replies 
 UTC+0 for WhatsApp User replies
3 channel The communication channel  
4 message_id The Message identifier to which the User replies.
 Set in UUID format 
5 extra_id External identifier of the Message to which the User replies
6 text_to_subscriber Text of Message, to which the User replies. This value can be null if the User has previously sent the following Message type: Image Only or File Only
7 text_from_subscriber User`s text reply
8 file_name Name of file
9 media Link of shared image.
 For example: "https://example.com/file.docx"
10 umid Transport ID of the sent Message, to which the User replies.
 Set in UUID format 
11 image_url Link of shared image.
 For example: "https://example.com/image.png"
12 video_url Link of shared video.
 For example: "https://example.com/video.mp4"
13 audio_url Link of shared audio.
 For example: "https://example.com/audio.mp3"
14 doc_url Link of shared file.
 For example: "https://example.com/file.docx"
15 location Link of shared location.
 For example:"50.450248718262,30.523889541626"

 
