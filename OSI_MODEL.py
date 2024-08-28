# OSI MODULE 
import time
print(r"""
   ____  _____ ____   __  _______  ____  __  ____    ______
  / __ \/ ___//  _/  /  |/  / __ \/ __ \/ / / / /   / ____/
 / / / /\__ \ / /   / /|_/ / / / / / / / / / / /   / __/   
/ /_/ /___/ // /   / /  / / /_/ / /_/ / /_/ / /___/ /___   
\____//____/___/  /_/  /_/\____/_____/\____/_____/_____/   
                                    
                         ┌(◉ ͜ʖ◉)つ┣▇▇▇═── MADE BY : ISS """)


def loading():
    print("█▒▒▒▒▒▒▒▒▒10%")
    time.sleep(2)
    print("████▒▒▒▒▒▒30%")
    time.sleep(2)
    print("████████▒▒80%")
    time.sleep(2)
    print("██████████100%")
    time.sleep(2)

def layers_quick():
    presentation_layer()
    print("\n<----  PROCESSING DATA  ---->")
    loading()
    session_layer()
    print("\n<----  ENCAPSULATION DATA  ---->")
    loading()
    trasnport_layer()
    print("\n<----  ENCAPSULATION SEGMENTS Or DATAGRAM ---->")
    loading()
    network_layer()
    print("\n<----  ENCAPSULATION PACKETS ---->")
    loading()   
    data_link_layer()
    print("\n<----  ENCAPSULATION FRAMES ---->")
    loading()
    physical_layer()
    print("4. TRANSLATE BITS or SIGNALS -------->\n")
    print(""" 001000 111100 11000 001100 00011010""")
    print(""" 001100 110100 11010 001100 10010011\n""")


# physical layer 
def physical_layer():
    print("\n❤ --- PHYSICAL LAYER (LAYER 1) ---\n")
    print("1. TYPE OF SIGNALS (Efficient Data Transmition)-------->")
    print("Analog Signal / Digital Signals\n")
    time.sleep(4)
    print("2. TRANSMITION MODE (Wired or Wireless) -------->\n")
    time.sleep(4)
    print("3. DATA FLOW -------->\n")
    time.sleep(4)


# data link layer 
def data_link_layer():
    print("\n❤ --- DATA LINK LAYER (LAYER 2) ---\n")
    print("1. ADDRESSING (LLC and MAC ) -------->\n")
    print(r"""
+---------------------------+----------------------+
|  Destination MAC Address  |  Source MAC Address  | <-- MAC Sublayer
|  00:1A:2B:3C:4D:5E        |  01:2B:3C:4D:5E:6F   |
+---------------------------+----------------------+
| EtherType/Length (16 bits)                       | <-- MAC Sublayer
|  0x0800 (IPv4)                                   |
+---------------------------+----------------------+
|  DSAP  |  SSAP  |  Control | Payload (Data)      | <-- LLC Sublayer
|  0xAA  |  0xAA  |  0x03    | (e.g., IP packet data)
+---------------------------+----------------------+
|      Frame Check Sequence (FCS, 32 bits)         | <-- MAC Sublayer
|                 CRC value                        |
+---------------------------+----------------------+
""")
    time.sleep(4)
    print("\n2. FLOW CONTROL -------->\n")
    time.sleep(4)
    print("3. ACCESS CONTROL -------->\n")
    time.sleep(4)
    print("4. ERROR CONTROL -------->\n")
    time.sleep(4)   
    

# network layer 
def network_layer():
    print("\n❤ --- NETWORK LAYER (LAYER 3) ---\n")
    print("1. NETWORK ADDRESSING (IP Address)  -------->\n")
    print(r"""
+------------------+------------------+------------------+-----------------+
|  Version (4 bits)|  IHL (4 bits)    |      TOS (8 bits                   |
+------------------+------------------+------------------+-----------------+
|                       Total Length (16 bits)                             |
+------------------+------------------+------------------+-----------------+
|                       Identification (16 bits)                           |
+------------------+------------------+------------------+-----------------+
|  Flags (3 bits)  |   Fragment Offset (13 bits)                           |
+------------------+------------------+------------------+-----------------+
|   TTL (8 bits)   |  Protocol (8 bits)    |   Header Checksum (16 bits)   |
+------------------+------------------+------------------+-----------------+
|                   Source IP Address (32 bits)                            |
|   192           |   168           |     1            |     100           |
+------------------+------------------+------------------+-----------------+
|               Destination IP Address (32 bits)                           |  
|   192           |   168           |     1            |     101           |
+------------------+------------------+------------------+-----------------+""")
    time.sleep(4)
    print("2. PACKET ROUTING -------->\n")
    time.sleep(4)
    print("3. PACKET HANDLING -------->\n")
    time.sleep(4)
      
# reansport layer 
def trasnport_layer():
    print("\n❤ --- TRANSPORT LAYER (LAYER 4) ---\n")
    print("1. PROCESS TO PROCESS DELIVERY-------->")
    print("- appiles a 16-bit port address identify sender destination application correctly. -\n")
    time.sleep(4)
    print("2. MULTIPLEXING and DEMULTIPLEXING  -------->\n")
    time.sleep(4)
    print("3. SELECT Method TCP OR UDP -------->\n")
    time.sleep(4)
    print("4. FLOW CONTROL -------->\n")
    time.sleep(4)
    print("5. ERROR CONTROL -------->\n")
    time.sleep(4)

# session layer 
def session_layer():
    print("\n❤ --- SESSION LAYER (LAYER 5) ---\n")
    print("1. Searching Protocols -->\n")
    time.sleep(3)
    print("""
USED Protocols -->
* RTCP - Real Time Transfer Protocol
* PPTP - Point To Point Transfer Protocol
* PAP  - Password Authentication Protocol
\n""")
    print("2. SYNCHRONIZATION -------->\n")
    time.sleep(4)
    print("3. SESSION ESTABLISHMENT  -------->")
    print("- between systems -- mapping connection with transport connection (1:1 , 1:M , M:N) - \n")
    time.sleep(4)
    print("4. DIALOG MANAGMENT -------->\n")
    time.sleep(4)
    print("5. DATA TRANSFER Method Choose (Half Duplex , Full Duplex) -------->\n")
    time.sleep(4)
    


def presentation_layer():
    print("\n❤ --- PRESENTATION LAYER (LAYER 6) ---\n")
    print("1. USED Protocol --> NDR (Network data Representation)\n")
    time.sleep(3)
    print("2. DATA CONVERSION (Translation) -------->")
    print("content (text, attachments) is encoded into a standardized format.\n")
    time.sleep(4)
    print("3. DATA COMPRESSED  -------->\n")
    time.sleep(4)
    print("4. DATA ENCRYPTION -------->\n")
    time.sleep(4)
    

# email broweser 
def email_browser():
    print("\n❤ --- APPLICATION LAYER (LAYER 7) ---")
    print(r"""
+-------------------------------------------------+
|               Email USER INTERFACE              |
+-------------------------------------------------+
| Inbox      | Sent       | Drafts     | Trash    |
+-------------------------------------------------+
| From: contact@example.com                       |
| Subject: Welcome to our service!                |
+-------------------------------------------------+
| Hello,                                          |
|                                                 |
| Thank you for signing up for our service.       |
| We are excited to have you on board.            |
|                                                 |
| Best regards,                                   |
| The Team                                        |
+-------------------------------------------------+
| Reply        Forward        Delete              |
+-------------------------------------------------+""")
    print("\nSeaching Protocol .........")
    time.sleep(4)
    print("\nProtocol USED --> SMTP (Simple Mail Transfer Protocol)")
    print("\n<----  PROCESSING EMAIL  ---->")
    loading()
    layers_quick()

# web browser 
def web_browser():
    print("\n❤ --- APPLICATION LAYER (LAYER 7) ---\n")
    print(r"""
+------------------------------------------------------+
| File  Edit  View  History  Bookmarks  Tools  Help    |
+------------------------------------------------------+
| [🔍 Search or enter address...                     ] |
+------------------------------------------------------+
| ⟵ ⟶ ⟳  | Home | Bookmark | Tabs | Profile | Settings |
+------------------------------------------------------+
|          Welcome to Your Web Browser!                |
|                                                      |
|This is a simple web page displaying a sample content.|
|                                                      |
|Here's a link to your favorite website: [Example.com] |
|                                                      |
|  Enjoy browsing the web!                             |
|                                                      |
|                                                      |
+------------------------------------------------------+
|  Status: Loading...                                  |
+------------------------------------------------------+""")
    print("Seaching Protocol .........")
    time.sleep(4)
    print("\nProtocol USED --> HTTP (Hyper Text Transfer Protocol)")
    print("\n<----  LOADING WEBSITE  ---->")
    loading()
    layers_quick()

# file transfer 
def file_transfer():
    print("\n❤ --- APPLICATION LAYER (LAYER 7) ---\n")
    print(r"""
    +------------------------------------------------+
    |                  File Transfer                 |
    +------------------------------------------------+
    | Source Folder: [ C:\Users\Documents\Source\  ] |
    | Destination Folder: [ D:\Backup\Destination\ ] |
    +------------------------------------------------+
    | Files to Transfer:                             |
    | [X] file1.txt  [ ] file2.jpg  [ ] file3.pdf    |
    | [ ] file4.doc  [X] file5.png  [X] file6.mp4    |
    +------------------------------------------------+
    | Transfer Progress:                             |
    | [███████████---------]  57% Complete           |
    | Time Remaining: 2 mins                         |
    +------------------------------------------------+
    | [ Start ]   [ Pause ]   [ Cancel ]   [ Close ] |
    +------------------------------------------------+""")
    print("\nSeaching Protocol .........")
    time.sleep(4)
    print("\nProtocol USED --> FTP (File Transfer Protocol)")
    print("\n<----  PROGRESS FILES  ---->")
    loading()
    layers_quick()

    
# sender application layer    
def s_application_layer():
    print("""
CHOOSE USER APPLICATION:
          1)  Email Browser
          2)  Web Browser
          3)  File Transfer
""")
    application = input("Enter Number (ex: 3) -> ")
    if application == "1":
        email_browser()
    elif application == "2":
        web_browser()
    elif application == "3":
        file_transfer()
    else:
        print("Somthing Wrong!")

# osi layers representation 
def osi_layers():
    print(r"""
❤ The open systems interconnection (OSI) model is a conceptual model 
  created by the International Organization for Standardization 
    which enables diverse communication systems to communicate 
                  using standard protocols.
          
+-------------------------+
| 7. Application Layer    |
+-------------------------+
| 6. Presentation Layer   |
+-------------------------+
| 5. Session Layer        |
+-------------------------+
| 4. Transport Layer      |
+-------------------------+
| 3. Network Layer        |
+-------------------------+
| 2. Data Link Layer      |
+-------------------------+
| 1. Physical Layer       |
+-------------------------+
""")

def sender():
    s_application_layer()

def receiver():
    print("\n--- CONNECTION SUCCESS ---\n")
    print("COMING BITS ...............\n")
    time.sleep(4)
    print(r"""
00100 001011 001111 0011000 11010101 00101010 001011
00110 001011 001101 0011001 11010101 00101010 001011
01100 001011 000111 0011010 11010101 00101010 001000
00101 001011 001001 0011000 11010111 00101010 001001""")
    time.sleep(4)
    print("\n❤ --- PHYSICAL LAYER (LAYER 1) ---\n")
    time.sleep(2)
    print("1. DATA FLOW -------->\n")
    time.sleep(4)
    print("\n<----  TRANSLATE BITS  ---->")
    loading()
    data_link_layer()
    print("\n<----  DE-CAPSULATION FRAMES  ---->")
    loading()
    network_layer()
    print("\n<----  DE-CAPSULATION PACKETS  ---->")
    loading()
    print("\n❤ --- TRANSPORT LAYER (LAYER 4) ---\n")
    print("1. FLOW CONTROL -------->\n")
    time.sleep(4)
    print("2. ERROR CONTROL -------->\n")
    time.sleep(4)    
    print("\n<----  DE-CAPSULATION SEGMENTS or DATAGRAM  ---->")
    loading()
    session_layer()
    print("\n<----  DE-CAPSULATION MSG/DATA  ---->")
    loading()
    print("\n❤ --- PRESENTATION LAYER (LAYER 6) ---\n")
    print("1. USED Protocol --> NDR (Network data Representation)\n")
    time.sleep(3)
    print("2. DATA CONVERSION (Translation) -------->")
    time.sleep(4)
    print("3. DATA DECOMPRESSED  -------->\n")
    time.sleep(4)
    print("4. DATA DECRYPTION -------->\n")
    time.sleep(4)
    print("\n<----  TRANSLATE MSG  ---->")
    loading()
    print("\n❤ --- APPLICATION LAYER (LAYER 7) ---\n")
    print("""\n
        +-------------------------------------------------+
        |          MESSAGE :    GOOD BYEE                 |
        +-------------------------------------------------+\n""")
# main menu 
print("""
Methods : 
      1) Sender
      2) Receiver
      3) OSI Layers
""")
method = input("CHOOSE Your Method (ex:2) -> ")
if method == "1":
    sender()
elif method == "2":
    receiver()
elif method == "3":
    osi_layers()
else:
    print("Somthing Wrong ! Try Again (ㆆ _ ㆆ) \n")
