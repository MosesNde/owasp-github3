 case 18:
 #line 428 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 13: goto tr26;
 		case 32: goto tr27;
 	}
	goto tr25;
 tr25:
 #line 46 "ext/puma_http11/http11_parser.rl"
 	{ MARK(mark, p); }
 	if ( ++p == pe )
 		goto _test_eof19;
 case 19:
#line 442 "ext/puma_http11/http11_parser.c"
	if ( (*p) == 13 )
		goto tr29;
	goto st19;
 tr9:
 #line 53 "ext/puma_http11/http11_parser.rl"
 	{
 	if ( ++p == pe )
 		goto _test_eof20;
 case 20:
#line 488 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 32: goto tr31;
 		case 60: goto st0;
 	if ( ++p == pe )
 		goto _test_eof21;
 case 21:
#line 509 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 32: goto tr33;
 		case 60: goto st0;
 	if ( ++p == pe )
 		goto _test_eof22;
 case 22:
#line 530 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 43: goto st22;
 		case 58: goto st23;
 	if ( ++p == pe )
 		goto _test_eof23;
 case 23:
#line 555 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 32: goto tr8;
 		case 34: goto st0;
 	if ( ++p == pe )
 		goto _test_eof24;
 case 24:
#line 575 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 32: goto tr37;
 		case 34: goto st0;
 	if ( ++p == pe )
 		goto _test_eof25;
 case 25:
#line 598 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 32: goto tr41;
 		case 34: goto st0;
 	if ( ++p == pe )
 		goto _test_eof26;
 case 26:
#line 618 "ext/puma_http11/http11_parser.c"
 	switch( (*p) ) {
 		case 32: goto tr44;
 		case 34: goto st0;