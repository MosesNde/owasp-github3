         return log_text
 
     def _log_task(self, log_f, subject, text, text_prefix=None):
         with open(log_f, 'a+') as the_file:
             text_to_write = \
                 '\n<b>' + subject + '</b> ...\n%s\n' % \