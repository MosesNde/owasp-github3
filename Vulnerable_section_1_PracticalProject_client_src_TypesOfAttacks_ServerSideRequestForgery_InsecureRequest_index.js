 
     return (
         <>
            <p>{`To fix the problem, a check on the imput can be used.`}</p>
             <input type="text" defaultValue={"text1"} onChange={(event) => setFileName(event.target.value)} />
             <input type="button" value="Get resource" onClick={() => { ServerSideRequestForgeryLevel1(setData, fileName) }} />
 