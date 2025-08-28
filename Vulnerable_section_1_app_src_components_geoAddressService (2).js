 const config = require('config');
 const axios = require('axios');

 const errorToProblem = require('./errorToProblem');

 const SERVICE = 'GeoAddressService';
 
 class GeoAddressService {
   constructor({ apiKey, bcAddressURL,queryParameters }) {
       const queryParameters = {...query, ...this.queryParameters };
 
       axios.defaults.headers['X-API-KEY'] = this.apiKey;
      const {data} = await axios.get(url, { params: { ...queryParameters } });
       return data;
     } catch (e) {
       errorToProblem(SERVICE, e);