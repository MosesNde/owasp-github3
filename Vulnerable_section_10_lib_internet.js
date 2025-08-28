         status: 404,
         ms: null
       };
      if (typeof url !== "string") {
         if (callback) { callback(result); }
         return resolve(result);
       }
       result.url = urlSanitized;
       try {
         if (urlSanitized && !util.isPrototypePolluted()) {
           let t = Date.now();
           if (_linux || _freebsd || _openbsd || _netbsd || _darwin || _sunos) {
             let args = ' -I --connect-timeout 5 -m 5 ' + urlSanitized + ' 2>/dev/null | head -n 1 | cut -d " " -f2';
 
   return new Promise((resolve) => {
     process.nextTick(() => {
      if (typeof host !== "string") {
         if (callback) { callback(null); }
         return resolve(null);
       }
           }
         }
       }
       let params;
       let filt;
       if (_linux || _freebsd || _openbsd || _netbsd || _darwin) {