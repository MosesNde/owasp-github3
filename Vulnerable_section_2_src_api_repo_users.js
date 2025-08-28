       throw new Error(`Auth Failure: No identity supplied.`);
     }
 
     // Check the cache
     const cachedUser = this.usersCache ? this.usersCache.find(x => x.id === userId) : null;
 
     return this.usersCache;
   }
 
   /**
    * Saves the user profile back to Netlify.
    * @param {*} userProfile - The Netlify user object to save.
       throw new Error(`Auth Failure: No identity supplied.`);
     }
 
     // Set up the Netlify endpoint info
     console.log(`Saving the user profile to Netlify`);
     const url = `${identity.url}/admin/users/${userId}`;