             });
             return d.promise;
         },
        check_health: function (host) {
             var d = $q.defer();
             system_info_resource.check_health({
                host: host
             },
             function (result) {
                 d.resolve(result);