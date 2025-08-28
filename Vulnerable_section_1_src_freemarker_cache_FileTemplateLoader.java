                 public Object run() throws IOException {
                     File source = new File(baseDir, SEP_IS_SLASH ? name : 
                         name.replace('/', File.separatorChar));
                     if(!source.isFile()) {
                         return null;
                     }
                     }
                     return source;
                 }
             });
         }
         catch(PrivilegedActionException e)