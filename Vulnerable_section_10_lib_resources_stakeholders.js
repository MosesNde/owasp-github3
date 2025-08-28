         },
 
         uploadStakeholderDoc(accountId, stakeholderId, params, callback) {
             return api.postFormData({
                 version: 'v2',
                 url: `${BASE_URL}/${accountId}/stakeholders/${stakeholderId}/documents`,
                formData: params
             }, callback);
         },
 