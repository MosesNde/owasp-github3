             input.accept = "image/*";
             input.setAttribute("onchange", `picLoaded(event, "${closedBy}")`);
             input.click();
            loadingOverlayShow();
           }
         },
       });
 };
 
 const picLoaded = async (e, type) => {
   const file = e.target.files[0];
   if (file.type.indexOf("image") == -1) {
     loadingOverlayHide();