       let preferUrl = query.bcGeoAddressURL;
       delete query.bcGeoAddressURL;
 
      const url = !preferUrl || (preferUrl===this.apiUrl)?this.apiUrl:preferUrl;
       const queryParameters = {...query, ...this.queryParameters };
 
       axios.defaults.headers['X-API-KEY'] = this.apiKey;
 
      const parsedUrl = new URL(url);
 
      const {data} = await axios.get(parsedUrl.href, { params: { ...queryParameters } });
 
       return data;
 