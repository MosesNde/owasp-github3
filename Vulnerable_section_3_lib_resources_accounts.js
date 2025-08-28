         },
 
         uploadAccountDoc(accountId, params, callback) {
             return api.postFormData({
                 version: 'v2',
                 url: `${BASE_URL}/${accountId}/documents`,
                formData: params
             }, callback);
         },
        