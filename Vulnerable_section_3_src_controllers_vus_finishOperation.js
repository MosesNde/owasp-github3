 const finishOperation = async (req, res) => {
   const params = req.body;
   try {
    params.url = Constants.VUS_URLS.END_OPERATION;
     const response = await vusService.simpleOperation(params);
     await AuthRequestService.update(
       Constants.AUTHENTICATION_REQUEST.SUCCESSFUL,