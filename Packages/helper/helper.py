from cerberus import Validator


class Helper:
    def validate(self, payload):
        try:
            schema = {'SENDER_ADDRESS': {'required': True, 'type': 'string', 'minlength': 6, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
                      'SENDER_PASS': {'required': True, 'type': 'string', 'minlength': 1},
                      'RECEIVER_ADDRESS': {'required': True, 'type': 'string', 'minlength': 6, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
                      'SMTP_PORT': {'required': True, 'type': 'string', 'min': 1},
                      }
            check_data = Validator(schema)
            validate = check_data.validate(payload)
            status = None
            message = None
            if(validate == True):
                payload["SMTP_PORT"] = int(payload["SMTP_PORT"])
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
