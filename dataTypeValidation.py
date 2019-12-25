import re


class DataTypeValidation(object):

    def __init__(self, tokens):

        # this will hold all the tokens that have been created by the lexer
        self.tokens = tokens
        # this will hold the token index we are parsing at
        self.token_index = 0
        self.line_number = 0

    def dt_validation(self):
        while self.token_index < len(self.tokens):

            # hold the type of token e.g IDENTIFIER
            token_type = self.tokens[self.token_index][0]

            # hold the value of token e.g var
            token_value = self.tokens[self.token_index][1]

            # this will trigger when a variable declaration token is found
            if re.search(r'^DATATYPE_', token_type):
                self.line_number += 1
                # self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])
                self.check_data_type(self.tokens[self.token_index:len(self.tokens)])

            # increment token_index through 1 so that we can loop through the token
            self.token_index += 1

    def check_data_type(self, token_stream):

        tokens_checked = 0
        line_number = self.line_number

        for token_dt in range(0, len(token_stream)):

            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            if token_dt == 0 and token_type == 'DATATYPE_INT':
                tokens_checked += 3

                if token_stream[tokens_checked][0] == 'INTEGER_VALUE':
                    tokens_checked -= 3


                else:
                    print("Line Number:" + str(line_number))
                    print("Line No:" + str(line_number) + " ERROR: invalid data typeof assignment variable: '"
                          + token_stream[tokens_checked][1] + "' \n The value should be of int data type")
                    tokens_checked -= 3

                   # quit()

            elif token_dt == 0 and token_type == 'DATATYPE_CHAR':
                tokens_checked += 3

                if token_stream[tokens_checked][0] == 'CHAR_VALUE':
                    tokens_checked -= 3
                else:
                    print("Line Number:" + str(line_number))
                    print("Line No:" + str(line_number) + " ERROR: invalid data typeof assignment variable: '"
                          + token_stream[tokens_checked][1] + "' \n The value should be of char data type")
                    tokens_checked -= 3
                   # quit()

            tokens_checked += 1

        # increment token index equal to token checked so that we don't check it again
        self.token_index += tokens_checked















