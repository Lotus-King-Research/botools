class GPT:

    '''Provides access to several OpenAI endpoints.'''
    
    def __init__(self):
        
        import openai

        self.openai = openai
        self.openai.api_key = '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'
        

    def context_definition_summary(self):

        return 'Condense provided Tibetan word definitions, following Oxford English rules for capitalization, into single English keywords.'

    def _context_definition_summary(self):

        context = '''
            - I will give you definitions of words
            - The definitions are going to be kind of mix of dictionary style and encyclopedic
            - The source will always be the same
            - The words are all from Tibetan
            - the definitions are in English
            - your task is to summarize the definition into single words, one or more
            - do not always use capital letters, but follow oxford english rules for capitalization
        '''

        return context


    def query_completion(self, prompt, context='', model='davinci-003'):

        response = self.openai.Completion.create(
            engine=model,
            prompt=context + '\n' + prompt,
            max_tokens=50)

        summary = response.choices[0].text.strip()
        print(summary)

    def query_chat(self,
              prompt,
              context='', 
              model="gpt-4-0613", 
              max_tokens=100):

        message = [{"role": "user", "content": context + '\n' + prompt}]

        response = self.openai.ChatCompletion.create(
            model=model,
            max_tokens=max_tokens,
            messages = message)

        return response
