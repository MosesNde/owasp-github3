 import axios from 'axios';
 import OAuth  from 'oauth-1.0a'
 import CryptoJS from 'crypto-js'
 
 const oauth = OAuth({
     consumer: {
 
 export const getFullUrl = (path) => {
 
     let url = `${process.env.NEXT_PUBLIC_WORDPRESS_URL}/wp-json/wc/v3/${path}`;
 
     // url += `?consumer_key=${process.env.WC_CONSUMER_KEY}`;