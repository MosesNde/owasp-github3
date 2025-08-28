         })
 
         rzpInstance.disputes.all({count:10, skip: 0}).then((response) => {
            console.log(response.__JUST_FOR_TESTS__)
             assert.equal(
                 response.__JUST_FOR_TESTS__.url,
                 `/v1/disputes?count=10&skip=0`,