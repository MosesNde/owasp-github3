     callback = all;
     all = false;
   }
 
   all = all || false;
   let result = [];
 // container inspect (for one container)
 
 function dockerContainerInspect(containerID, payload) {
  containerID = containerID || '';
   return new Promise((resolve) => {
     process.nextTick(() => {
      if (containerID) {
 
         if (!_docker_socket) {
           _docker_socket = new DockerSocket();
         }
 
        _docker_socket.getInspect(containerID.trim(), data => {
           try {
             resolve({
               id: payload.Id,
 function dockerContainerStats(containerIDs, callback) {
 
   let containerArray = [];
  // fallback - if only callback is given
  if (util.isFunction(containerIDs) && !callback) {
    callback = containerIDs;
    containerArray = ['*'];
  } else {
    containerIDs = containerIDs || '*';
    containerIDs = containerIDs.trim().toLowerCase().replace(/,+/g, '|');
    containerArray = containerIDs.split('|');
  }

   return new Promise((resolve) => {
     process.nextTick(() => {
 
       const result = [];
 
       const workload = [];
 // container processes (for one container)
 
 function dockerContainerProcesses(containerID, callback) {
  containerID = containerID || '';
   let result = [];
   return new Promise((resolve) => {
     process.nextTick(() => {
      if (containerID) {
 
         if (!_docker_socket) {
           _docker_socket = new DockerSocket();
         }
 
        _docker_socket.getProcesses(containerID, data => {
           /**
            * @namespace
            * @property {Array}  Titles