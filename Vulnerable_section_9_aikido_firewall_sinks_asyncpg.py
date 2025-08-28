 import importhook
 from aikido_firewall.vulnerabilities.sql_injection.dialects import Postgres
 from aikido_firewall.background_process.packages import add_wrapped_package
from aikido_firewall.vulnerabilities import run_vulnerability_scan
 from aikido_firewall.helpers.logging import logger
 
 
     former_execute = copy.deepcopy(asyncpg.Connection.execute)
 
     def aikido_new__execute(_self, query, *args, **kwargs):
        run_vulnerability_scan(
             kind="sql_injection",
             op="asyncpg.connection.Connection._execute",
             args=(query, Postgres()),
 
     def aikido_new_executemany(_self, query, *args, **kwargs):
         # This query is just a string, not a list, see docs.
        run_vulnerability_scan(
             kind="sql_injection",
             op="asyncpg.connection.Connection.executemany",
             args=(query, Postgres()),
         )
         return former_executemany(_self, query, *args, **kwargs)
 
     def aikido_new_execute(_self, query, *args, **kwargs):
        run_vulnerability_scan(
             kind="sql_injection",
             op="asyncpg.connection.Connection.execute",
             args=(query, Postgres()),