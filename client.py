# telnet program example
import socket, select, string, sys
import hashlib 
import base64
from Crypto.Cipher import AES
from Crypto import Random
#def prompt() :
#    sys.stdout.write('<You> ')
#    sys.stdout.flush()
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Start sending messages'
    #prompt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    #prompt()
             
            #user entered a message
            else :
            	print "bank_ifcs_code";
            	msg1 = sys.stdin.readline()
            	print "bank_account_number"
            	msg2 = sys.stdin.readline()
            	print "Amount"
            	msg3 = sys.stdin.readline()
            	print "merchant_transaction_ref"
            	msg4 = sys.stdin.readline()
            	print "transaction_date"
            	msg5 = sys.stdin.readline()
            	print "payment_gateway_merchant_reference"
            	msg6 = sys.stdin.readline()
            	msg = "bank_ifcs_code" + msg1+"|"+"bank_account_number"+msg2+"|"+"Amount"+msg3+"|"+"merchant_transaction_ref"+msg4+"|"+"transaction_date"+msg5+"|"+"payment_gateway_merchant_reference"+msg6
                #msg1 = sys.stdin.readline()
                hash_object = hashlib.sha1(msg)
                hex_dig = hash_object.hexdigest()
                payload_with_sha = msg+"|"+hex_dig
                #payload_to_pg = BASE64ENCODE(AES128CBC(payload_with_sha))



                s.send(payload_with_sha)
                #prompt()