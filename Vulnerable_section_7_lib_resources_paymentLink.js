  * DOCS: https://razorpay.com/docs/payment-links/
  */
 
const Promise = require("promise"),
      { normalizeDate, normalizeNotes } = require('../utils/razorpay-utils');
 
 module.exports = function paymentLinkApi (api) {
 