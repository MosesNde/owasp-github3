 const { v4: uuidv4 } = require("uuid");
 const { fromBuffer: fileTypeFromBuffer } = require('file-type-cjs');
 const path = require('path');
 
 /**
  * @typedef ImageFileType
                 let img_res;
                 try {
                     img_res = await axios.get(image.url, {
                         responseType: 'arraybuffer',
                         headers: {
                             'Accept': '*/*'
                         }
                     });
                 } catch(e) {
                     throw new ImageBlockError("Unable to download the image from the given URL.");
                 }
 