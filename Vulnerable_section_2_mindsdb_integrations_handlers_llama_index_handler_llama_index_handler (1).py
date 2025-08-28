 
 from mindsdb.integrations.libs.base import BaseMLEngine
 from mindsdb.utilities.config import Config
 
 
 def _validate_prompt_template(prompt_template: str):
             if 'source_url_link' not in args['using']:
                 raise Exception("SimpleWebPageReader requires a `source_url_link` parameter. Refer to LlamaIndex documentation for more details.")  # noqa
 
            reader = SimpleWebPageReader(html_to_text=True).load_data([args['using']['source_url_link']])
 
         else:
             raise Exception(f"Invalid operation mode. Please use one of {self.supported_reader}.")