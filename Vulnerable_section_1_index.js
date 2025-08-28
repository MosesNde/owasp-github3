 const { URL } = require('url');
 const fs = require('fs');
 const path = require('path');
 
const debounceJS = fs.readFileSync(path.resolve(__dirname, './utils/debounceJS.js'), 'utf8');
const sendTextDataScript = fs.readFileSync(path.resolve(__dirname, './utils/getTextData.js'), 'utf8');
const blockNavigationScript = fs.readFileSync(path.resolve(__dirname, './utils/blockNavigation.js'), 'utf8');
const blockNavigationStyle = fs.readFileSync(path.resolve(__dirname, './utils/blockNavigation.css'), 'utf8');
 
 function createServer({
   SERVER_ROOT,
   PORT,
   CORS_OPTIONS = { origin: `${SERVER_ROOT}:3000`, credentials: true },
  COOKIE_SETTING = {}
 }) {
   console.log('createServer', SERVER_ROOT, PORT);
 
 
   const PATH = `${SERVER_ROOT}:${PORT}`;
 
  const isValidURL = (url) => {
    // eslint-disable-next-line no-useless-escape
    return /(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi.test(url);
  }

   const getHostPortSSL = (url) => {
     const {
       hostname,
     // this is the url retrieved from the input
     const url = req.query.url;
     // ****** first check for human readable URL with simple regex
    if (!isValidURL(url)) {
       res.status(400).send({ errorMessage: 'Please enter a valid URL and try again.' });
     } else {
       // ****** second check for puppeteer being able to goto url