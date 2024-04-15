SMS ENCODING
------------

+-----------------------------------------+-------------------------------------------------------------+----------------------------------------------------------+-----------+
| Encoding scheme                         | Text length of a short SMS Message in the Message segment   | Text length of a long SMS Message in the Message segment | Supported |
+=========================================+=============================================================+==========================================================+===========+
| GSM 7-bit default alphabet (GSM 03.38)* | 160 characters                                              | 153 characters                                           | Yes       |
+-----------------------------------------+-------------------------------------------------------------+----------------------------------------------------------+-----------+
| UCS2 (ISO/IEC-10646) 16-bit             | 70 characters                                               | 67 characters                                            | Yes       |
+-----------------------------------------+-------------------------------------------------------------+----------------------------------------------------------+-----------+

*length of Message segments is given based on usage of characters of GSM 7-bit default alphabet table. In this case, it should be noted that if the characters of GSM 7-bit default alphabet extended table are used, the length of Message segments will decrease, since each character of the extended table is transmitted as two octets, and is counted as two characters  

The extended table of GSM 7-bit default alphabet characters:

======  ======  =========================== ==========
Hex     Dec 	  Character name              Character 
======  ======  =========================== ==========
0x1B0A 	27 10 	FORM FEED (PAGE BREAK)      
0x1B14 	27 20 	CIRCUMFLEX ACCENT           ^
0x1B28 	27 40 	LEFT CURLY BRACKET 	        {
0x1B29 	27 41 	RIGHT CURLY BRACKET         }
0x1B2F 	27 47 	REVERSE SOLIDUS (BACKSLASH) \
0x1B3C 	27 60 	LEFT SQUARE BRACKET-        [
0x1B3D 	27 61 	TILDE                       ~
0x1B3E 	27 62 	RIGHT SQUARE BRACKET        ]
0x1B40 	27 64 	VERTICAL BAR                |
0x1B65 	27 101 	EURO SIGN 	                €
0x1B1B 	27 27 	RESERVED                    
======  ======  =========================== ==========

Table of country codes and their prefixes are provided upon request.

