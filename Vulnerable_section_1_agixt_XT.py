             full_path = os.path.normpath(os.path.join(self.agent_workspace, file_name))
             if not full_path.startswith(self.agent_workspace):
                 raise Exception("Path given not allowed")
            with open(file_path, "wb") as f:
                f.write(requests.get(file_url).content)
         if conversation_name != "" and conversation_name != None:
             c = Conversations(conversation_name=conversation_name, user=self.user_email)
             c.log_interaction(