ddr = ""
serveraddr = ""

usage = "Usage: %prog [options] fromaddress toaddress serveraddress"
parser = OptionParser(usage=usage)

parser.set_defaults(usetls=False)
parser.set_defaults(usessl=False)
parser.set_defaults(serverport=25)
parser.set_defaults(SMTP_USER="")
parser.set_defaults(SMTP_PASS="")
parser.set_defaults(debuglevel=0)
parser.set_defaults(verbose=False)

parser.add_option("-t", "--usetls", action="store_true", dest="usetls", default=False, help="Connect using TLS, default is false")
parser.add_option("-s", "--usessl", action="store_true", dest="usessl", default=False, help="Connect using SSL, default is false")
parser.add_option("-n", "--port", action="store", type="int", dest="serverport", help="SMTP server port", metavar="nnn")
parser.add_option("-u", "--username", action="store", type="string", dest="SMTP_USER", help="SMTP server auth username", metavar="username")
parser.add_option("-p", "--password", action="store", type="string", dest="SMTP_PASS", help="SMTP server auth password", metavar="password")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Verbose message printing")
parser.add_option("-d", "--debuglevel", type="int", dest="debuglevel", help="Set to 1 to print smtplib.send messages", metavar="n")

(options, args) = parser.parse_args()
if len(args) != 3:
	parser.print_help()
	parser.error("incorrect number of arguments")
	sys.exit(-1)

fromaddr = args[0]
toaddr = args[1]
serveraddr = args[2]	
	
now = strftime("%Y-%m-%d %H:%M:%S")

msg = "From: %s\r\nTo: %s\r\nSubject: Test Message from smtptest at %s\r\n\r\nTest message from the smtptest tool sent at %s" % (fromaddr, toaddr, now, now)

if options.verbose:
	print('usetls:', options.usetls)
	print('usessl:', options.usessl)
	print('from address:', fromaddr)
	print('to address:', toaddr)
	print('server address:', serveraddr)
	print('server port:', options.serverport)
	print('smtp username:', options.SMTP_USER)
	print('smtp password: *****')
	print('smtplib debuglevel:', options.debuglevel)
	print("-- Message body ---------------------")
	print(msg)
	print("-------------------------------------")

server = None
if options.usessl:
	server = smtplib.SMTP_SSL()
else:
	server = smtplib.SMTP()

server.set_debuglevel(options.debuglevel)
server.connect(serveraddr, options.serverport)
server.ehlo()
if options.usetls: server.starttls()
server.ehlo()
if options.SMTP_USER != "": server.login(options.SMTP_USER, options.SMTP_PASS)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
