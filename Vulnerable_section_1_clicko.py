     parser.add_argument("-t", type=int, default=90, help="use this option to set sleep time between clicks")
     args = parser.parse_args()
 
     try:
         with open("conf.pkl", "rb") as f:
             pos = pickle.load(f)
 
     except FileNotFoundError:
        if args.set:
            pos = getPosition()
            with open("conf.pkl", "wb") as f:
                pickle.dump(pos, f)
        else:
            print("you have to set position first!, use --set option")
            sys.exit(-1)
 
     print("button position set to: ", pos)
 
     clicks = 0
     secs = args.t
     while True:
         print(f"sleeping for {secs} seconds")
        time.sleep(secs-1)
         pa.moveTo(pos, duration=1)
         pa.click(pos)
         clicks += 1
         print(f"mouse clicked at position {pos}, total clicks: {clicks}")
