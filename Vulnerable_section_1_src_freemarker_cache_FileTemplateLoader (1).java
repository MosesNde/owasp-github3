 import java.security.PrivilegedExceptionAction;
 
 import freemarker.template.utility.SecurityUtilities;
 
 /**
  * A {@link TemplateLoader} that uses files in a specified directory as the
         try {
             return AccessController.doPrivileged(new PrivilegedExceptionAction() {
                 public Object run() throws IOException {
                     File source = new File(baseDir, SEP_IS_SLASH ? name : 
                         name.replace('/', File.separatorChar));
                     
                    if(!isParent(baseDir, source) ) { 
                        throw new SecurityException("File " + name + " is not in base directiry");
                    }
                    
                     if(!source.isFile()) {
                         return null;
                     }
                     return source;
                 }
                 
                private boolean isParent(File parent, File file) {
                    File f;
                    try {
                        parent = parent.getCanonicalFile();
                        f = file.getCanonicalFile();
                    } catch (IOException e) {
                        return false;
                    }
                    while (f != null) {
                        if (parent.equals(f)) {
                            return true;
                        }
                        f = f.getParentFile();
                    }
                    return false;
                }               
             });
         }
         catch(PrivilegedActionException e)