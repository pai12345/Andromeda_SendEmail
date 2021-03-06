from logging import error
from cerberus import Validator


class Helper:
    def get_schema(self, input):
        try:
            switcher = {
                "SMTP_PORT": {'required': True, 'type': 'string', 'min': 1},
                "Payload": {'SenderAddress': {'required': True, 'type': 'string', 'minlength': 6, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
                            'SenderPassword': {'required': True, 'type': 'string', 'minlength': 1},
                            'ReceiverAddress': {'required': True, 'type': 'string', 'minlength': 6, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'}
                            }
            }
            if input in switcher:
                return {input: switcher[input]}
            else:
                return "Invalid"
        except BaseException as error:
            return error

    def validate(self, schema, payload):
        try:
            check_data = Validator(schema)
            validate = check_data.validate(payload)
            status = None
            message = None
            if(validate == True):
                status = "success"
                message = payload
            else:
                status = "error"
                error_data = {i for i in check_data.errors}
                message = f"""Invalid Paramerters found for: '{error_data}'."""
            return {"status": status, "message": message}
        except BaseException as error:
            return {"status": "error", "message": error}


oServe_helper = Helper()
