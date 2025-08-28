 See LICENSE file in root for details.
 
 *******************************************************************************/

 const { readFileSync } = require('fs');
 const path = require('path');
 
 const isObject = (item) =>
   typeof item === 'object' && !Array.isArray(item) && item !== null;
 
 /** Maps the old options to the new config structure
  * @export utils
  * @param oldOptions {any} Options to be mapped
   expBackoff,
   fixType,
   handleResources,
  isObject,
   isCorrectJSON,
   mapToNewConfig,
   mergeConfigOptions,
   optionsStringify,