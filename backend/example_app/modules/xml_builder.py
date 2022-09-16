import datetime


class XMLMessageBuilder:
    def __init__(self, sender_id, reciever_id, coding_scheme, sender_role):
        self.default_sender_id = sender_id
        self.default_reciever_id = reciever_id
        self.default_sender_role = sender_role
        self.default_coding_scheme = coding_scheme
        self.message_generated = None

        self.message_date_from = ''
        self.message_date_to = ''
        self.message_root_date = ''
        self.message_root_id = ''
        self.message = ''

    # Tested and working
    # format datetime object to string
    @staticmethod
    def format_datetime(date_time):
        return date_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Tested and working
    # make id from datetime
    @staticmethod
    def make_id_from_datetime(date_time):
        return date_time.replace(":", "").replace("-", "").replace("T", "").replace("Z", "")

    # Tested and working
    # Set year and month to make message_root_date, message_root_id, date_from and date_to
    def set_period(self, year, month):

        # Find first day of month
        date_from = datetime.datetime(year, month, 1)

        # Find last day of month
        if month == 12:
            date_to = datetime.datetime(
                year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            date_to = datetime.datetime(
                year, month + 1, 1) - datetime.timedelta(days=1)

        # Set message_date_from and message_date_to
        self.message_date_from = date_from.strftime("%Y-%m-%d")
        self.message_date_to = date_to.strftime("%Y-%m-%d")

    # Tested and working
    # Generate timestamp for message root date_now only for testing
    def generate_message_timestamp(self, date_now=None):

        # Generate actual date
        date_now = date_now if date_now else datetime.datetime.now()
        date_formated = self.format_datetime(date_now)

        self.message_generated = date_now
        self.message_root_date = date_formated
        self.message_root_id = self.make_id_from_datetime(date_formated)

    
    # Make message root
    # TODO: Test and fix
    def make_message_root(self, message_type, message_id, message_date, sender_identification, reciever_identification, location_list):
        pass

    # Tested and working
    # Make sender identification for XML message
    def make_sender_identification(self):
        return f'<default:SenderIdentification coding-scheme="{self.default_coding_scheme}" id="{self.default_sender_id}" role="{self.default_sender_role}"/>'

    # Tested and working
    # Make reciever identification for XML message
    def make_reciever_identification(self):
        return f'<default:ReceiverIdentification coding-scheme="{self.default_coding_scheme}" id="{self.default_reciever_id}"/>'

    # Tested and working
    # Make location for XML message
    def make_location(self, unit):
        return f'<default:Location source-id="{unit["idf"]}" ean="{unit["ean"]}" date-to="{self.message_date_to}" date-from="{self.message_date_from}"/>'

    # Tested and working
    # Make location list from units
    def make_location_list(self, units):
        location_list = ''
        for unit in units:
            location_list += self.make_location(unit)
        return location_list



    # TODO: Test and fix
    def make_message_body(self, year, month, units, *args, **kwargs):

        # Set period
        self.set_period(year, month)

        # Generate actual date
        # if **kwargs contains date_now, use it as date_now
        # else use actual date
        date_now = kwargs.get('date_now', None)

        # Generate message root timestamps
        self.generate_message_root_timestamps(date_now=date_now)

        # Generate sender identification
        message_root_date = self.message_root_date
        message_root_id = self.message_root_id
        sender_identification = self.make_sender_identification()
        reciever_identification = self.make_reciever_identification()
        locations = self.make_location_list(units)

        return f'<default:RESREQ xmlns:default="http://www.ote-cr.cz/schema/oze/request" xmlns="http://www.ote-cr.cz/schema/oze/request" date-time="{message_root_date}" dtd-release="1" dtd-version="1" id="{message_root_id}" message-code="PDJ">{sender_identification + reciever_identification + locations}</default:RESREQ>'

    def generate_message():

        pass