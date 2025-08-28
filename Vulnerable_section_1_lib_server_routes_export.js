   clearText,
   fixType,
   isCorrectJSON,
   mergeConfigOptions,
   optionsStringify
 } = require('./../../utils.js');
     requestId: uniqueId
   };
 
   // Start the export process
   chart.startExport(options, (info, error) => {
     // If the connection was closed, do nothing