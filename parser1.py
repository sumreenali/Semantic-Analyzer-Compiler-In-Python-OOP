import re
import dataTypeValidation


class Parser1(object):

    def __init__(self, tokens):

        # this will hold all the tokens that have been created by the lexer
        self.tokens = tokens

        # this will hold the token index we are parsing at
        self.token_index = 0

        self.line_number = 0

    def parse(self):
        while self.token_index < len(self.tokens):

            # hold the type of token e.g IDENTIFIER
            token_type = self.tokens[self.token_index][0]

            # hold the value of token e.g var
            token_value = self.tokens[self.token_index][1]

            # this will trigger when a variable declaration token is found
            if re.search(r'^DATATYPE_', token_type):
                self.line_number+=1
                self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])

            # increment token_index through 1 so that we can loop through the token
            self.token_index += 1


    def parse_variable_declaration(self, token_stream):

        tokens_checked = 0
        line_number = self.line_number
        print("Line Number:" + str(line_number))

        for token in range(0, len(token_stream)):

            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            # this will get the variable type e.g.
            if token == 0:
                print('Variable type: ' + token_value)

            if token == 4 and token_type == 'STATEMENT_END':
                print('Statement_end: ' + token_value)
                print()
                break

            elif token == 4 and token_type != 'STATEMENT_END':
                print('Error: Statement terminator is missing at line number:' + str(line_number))
                quit()

            elif token == 1 and token_type == 'IDENTIFIER':
                print('Identifier value: ' + token_value)
            elif token == 1 and token_type != 'IDENTIFIER':
                print("ERROR: Invalid variable name '" + token_value + "at line number:" + str(line_number))
                quit()

            elif token == 2 and token_type == "ASSIGNMENT_OPERATOR":
                print('Assignment operator: ' + token_value)
            elif token == 2 and token_type != "ASSIGNMENT_OPERATOR":
                print("ERROR: Assignment variable value is missing at line number:" + str(line_number))
                quit()

            elif token == 3 and (token_type == 'IDENTIFIER' or re.search(r'_VALUE$', token_type)):
                print('Assignment value:' + token_value)
            elif token == 3 and (token_type != 'IDENTIFIER' or re.search(r'_VALUE$', token_type,flags=1)):
                print(
                    "ERROR: Invalid variable assignment value '" + token_value + "' at line number:" + str(line_number))
                quit()

            tokens_checked += 1

        # increment token index equal to token checked so that we don't check it again
        self.token_index += tokens_checked















