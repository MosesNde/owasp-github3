 
   return new Promise((resolve) => {
     process.nextTick(() => {
      if (typeof srv !== "string") {
         if (callback) { callback([]); }
         return resolve([]);
       }
   return new Promise((resolve) => {
     process.nextTick(() => {
 
       let processesString = '';
       processesString.__proto__.toLowerCase = util.stringToLower;
       processesString.__proto__.replace = util.stringReplace;