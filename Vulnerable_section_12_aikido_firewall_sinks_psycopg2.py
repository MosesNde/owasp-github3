 import importhook
 from aikido_firewall.vulnerabilities.sql_injection.dialects import Postgres
 from aikido_firewall.background_process.packages import add_wrapped_package
from aikido_firewall.vulnerabilities import run_vulnerability_scan
 
 
 def wrap_cursor_factory(cursor_factory):
     class AikidoWrappedCursor(ext.cursor):
         def execute(self, *args, **kwargs):
             """Aikido's wrapped execute function"""
            run_vulnerability_scan(
                 kind="sql_injection",
                 op="psycopg2.Connection.Cursor.execute",
                 args=(args[0], Postgres()),  #  args[0] : sql
 
         def executemany(self, *args, **kwargs):
             """Aikido's wrapped executemany function"""
            for sql in args[0]:
                run_vulnerability_scan(
                    kind="sql_injection",
                    op="psycopg2.Connection.Cursor.executemany",
                    args=(sql, Postgres()),
                )
             if former_cursor_factory and hasattr(former_cursor_factory, "executemany"):
                 return former_cursor_factory.executemany(self, *args, **kwargs)
             return super().executemany(*args, **kwargs)