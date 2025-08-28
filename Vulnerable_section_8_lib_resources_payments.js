 'use strict'
 
const Promise = require("promise");

 const { normalizeDate } = require('../utils/razorpay-utils')
 
 const ID_REQUIRED_MSG = '`payment_id` is mandatory',