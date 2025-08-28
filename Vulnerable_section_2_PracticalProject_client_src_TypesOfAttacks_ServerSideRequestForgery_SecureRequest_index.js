 
     return (
         <>
            <p>{`This problem may occur when the api is too permisive with the imputs.`}</p>
            <p>{`For example if the API reads a text file, if the API receives the file name,
            an attacker can modify it and get access to other sensitive data.`}</p>
            <p>{`The input below takes in resource name (this kind of input may not exist but can be replicated with programs such as Postman).
             The text1 resource is intended to be presented, but text2 is not.`}</p>
             <input type="text" defaultValue={"text1"} onChange={(event) => setFileName(event.target.value)} />
             <input type="button" value="Get resource" onClick={() => { ServerSideRequestForgeryLevel2(setData, fileName) }} />
 