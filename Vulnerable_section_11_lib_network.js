 function networkStats(ifaces, callback) {
 
   let ifacesArray = [];
  // fallback - if only callback is given
  if (util.isFunction(ifaces) && !callback) {
    callback = ifaces;
    ifacesArray = [getDefaultNetworkInterface()];
  } else {
    ifaces = ifaces || getDefaultNetworkInterface();
    ifaces = ifaces.trim().toLowerCase().replace(/,+/g, '|');
    ifacesArray = ifaces.split('|');
  }
 
   return new Promise((resolve) => {
     process.nextTick(() => {
 
       const result = [];
 
       const workload = [];