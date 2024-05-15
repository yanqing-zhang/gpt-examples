import json
from openaix.chat_db_function_scene.db_info import DbInfo
class Functions:
    def get_conn(self):
        db = DbInfo()
        return db.get_conn()

    def get_functions(self, database_schema_string):
        functions = [
            {
                "name": "ask_database",
                "description": "Use this function to answer user questions about music. Output should be a fully formed SQL query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": f"""
                                    SQL query extracting info to answer the user's question.
                                    SQL should be written using this database schema:
                                    {database_schema_string}
                                    The query should be returned in plain text, not in JSON.
                                    """,
                        }
                    },
                    "required": ["query"],
                },
            }
        ]
        return functions

    def ask_database(self,query):
        try:
            results = str(self.get_conn().execute(query).fetchall())
        except Exception as e:
            results = f"query failed with error: {e}"
        return results

    def execute_function_call(self,message):
        """
        入参message的值如下：
        {
            'role': 'assistant',
            'content': None,
            'function_call':
                {
                'name': 'ask_database',
                'arguments': '{"query":"SELECT albums.Title, COUNT(tracks.TrackId) AS NumberOfTracks FROM albums INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId GROUP BY albums.AlbumId ORDER BY NumberOfTracks DESC LIMIT 1;"}'
                }
        }
        :param message:
        :return:
        """
        if message["function_call"]["name"] == "ask_database":
            query = json.loads(message["function_call"]["arguments"])["query"]
            print(f'query:\n{query}')
            results = self.ask_database(query)
        else:
            results = f"Error: function {message['function_call']['name']} does not exist"
        return results