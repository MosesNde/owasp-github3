 const fetch = require('node-fetch');
 
 const Constants = require('../constants/Constants');
const options = require('../constants/ImageOptions');
 const Messages = require('../constants/Messages');
 
 const {
  *  Realiza un post al servicio de vuSecurity con la url interna y el body recibidos
  */
 const vuSecurityPost = async function vuSecurityPost(params) {
  const response = await fetch(params.url, {
     method: 'POST',
     headers: {
       'Content-Type': 'application/json',
       'x-access-apikey': Constants.VUS_API_KEY,
     },
     body: params.body,
    url: params.url,
   });
   if (response.status === 400) throw response.json();
   return response.json();
   if (!params.deviceName) throw missingDeviceName;
   try {
     const result = await vuSecurityPost({
      url: Constants.VUS_URLS.NEW_OPERATION,
       body: JSON.stringify({
         userName: params.userName,
         ipAddress: Constants.IP_ADDRESS,
   if (!params.side) throw missingSide;
   try {
     const response = await vuSecurityPost({
      url: options.get(params.side),
       body: JSON.stringify({
         operationId: params.operationId,
         userName: params.userName,
   if (!params.file) throw missingSelfieList;
   try {
     const response = await vuSecurityPost({
      url: Constants.VUS_URLS.ADD_SELFIE,
       body: JSON.stringify({
         operationId: params.operationId,
         userName: params.userName,
   validateCommonParams(params);
   try {
     return vuSecurityPost({
      url: params.url,
       body: JSON.stringify({
         userName: params.userName,
         operationId: params.operationId,