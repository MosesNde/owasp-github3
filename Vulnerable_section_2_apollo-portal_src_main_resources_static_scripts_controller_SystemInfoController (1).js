         });
     }
 
    function check(host) {
        SystemInfoService.check_health(host).then(function (result) {
             var status = result.status.code;
            if (status == 'UP') {
                 toastr.success(host + ' is healthy!');
             } else {
                 toastr.error(host + ' is not healthy, please check ' + host + '/health for more information!');