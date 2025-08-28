   max: 100, // limit each IP to 100 requests per windowMs
 });
 
 // Fetch redirected URL
 async function fetchRedirectedUrl(url) {
   return new Promise((resolve, reject) => {
   }
 
   let { url } = req.body;
  const allowedDomain = "www.skillrack.com";
   try {
     const parsedUrl = new URL(url);
     if (allowedDomain !== parsedUrl.hostname) {
     return res.status(400).json({ error: 'No URL provided' });
   }
 
   const data = await fetchData(url);
   if (data) {
     const logMessage = `\`${data.name} (${data.dept}'${data.year.slice(-2)})\`\n\n\`(${data.codeTutor} x 0) + (${data.codeTrack} x 2) + (${data.codeTest} x 30) + (${data.dt} x 20) + (${data.dc} x 2) = ${data.points} (${data.percentage}%)\`\n\n`;