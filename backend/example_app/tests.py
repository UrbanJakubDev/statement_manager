import datetime
from django.test import TestCase
from example_app.modules.xml_builder import XMLMessageBuilder

# Create your tests here.


class DateTimeTest(TestCase):

    def setUp(self):
        self.builder = XMLMessageBuilder(
            sender_id="8591824556207",
            reciever_id="8591824000007",
            coding_scheme="14",
            sender_role='V')
        self.date_string = "2022-09-07T16:53:13Z"
        self.expected_result_id = "20220907165313"

    # Tests for make_id_from_datetime method
    def test_shoud_return_id_from_date(self):
        result = self.builder.make_id_from_datetime(self.date_string)
        self.assertEqual(result, self.expected_result_id)

    def test_should_not_return_different_id_from_date(self):
        expected_result_id = "20220907165312"
        result = self.builder.make_id_from_datetime(self.date_string)
        self.assertNotEqual(result, expected_result_id)

    def test_should_not_return_none_for_id_from_date(self):
        result = self.builder.make_id_from_datetime(self.date_string)
        self.assertIsNotNone(result)

    def test_should_return_string_for_id_from_date(self):
        result = self.builder.make_id_from_datetime(self.date_string)
        self.assertIsInstance(result, str)

    # Tests for set_period method
    def test_should_set_date_for_xml_builder(self):

        expected_date_from = "2022-08-01"
        expected_date_to = "2022-08-31"

        self.builder.set_period(year=2022, month=8)
        self.assertEqual(self.builder.message_date_from, expected_date_from)
        self.assertEqual(self.builder.message_date_to, expected_date_to)

    # Tests for generate_message_root_timestamps method

    def test_should_generate_timestamps(self):

        # Convert string to datetime object
        date_time = datetime.datetime.strptime("2022-08-01T16:53:13Z", "%Y-%m-%dT%H:%M:%SZ")
        self.builder.generate_message_timestamp(date_now=date_time)

        expected_message_root_date = "2022-08-01T16:53:13Z"
        expected_message_root_id = "20220801165313"

        self.assertEqual(self.builder.message_root_date,expected_message_root_date)
        self.assertEqual(self.builder.message_root_id,expected_message_root_id)


class XMLMessageTest(TestCase):

    def setUp(self):
        self.builder = XMLMessageBuilder(
            sender_id="8591824556207",
            reciever_id="8591824000007",
            coding_scheme="14",
            sender_role='V')

        # Default values for the builder
        self.coding_scheme = '14'
        self.sender_id = '8591824556207'
        self.sender_role = 'V'
        self.reciever_id = '8591824000007'

        # Different values for the builder
        self.sender_id_diff = '8591824556208'
        self.coding_scheme_diff = '15'
        self.sender_role_diff = 'A'
        self.reciever_id_diff = '8591824000008'

        self.unit = {
            "idf": "019259_Z11",
            "ean": "859182400211637793"
        }

        self.units = [
            {
                "idf": "019259_Z11",
                "ean": "859182400211637793"
            },
            {
                "idf": "034687_Z11",
                "ean": "859182400211958560"
            }
        ]

        self.builder.set_period(year=2022, month=8)

    # Tests for make_sender_identification method

    def test_should_make_sender_identification_string(self):
        message = self.builder.make_sender_identification()
        self.assertEqual(
            message,
            f'''<default:SenderIdentification coding-scheme="{self.coding_scheme}" id="{self.sender_id}" role="{self.sender_role}"/>''')

    def test_should_make_sender_identification_with_different_role(self):
        self.builder.default_coding_scheme = self.coding_scheme_diff
        message = self.builder.make_sender_identification()
        self.assertEqual(
            message,
            f'''<default:SenderIdentification coding-scheme="{self.coding_scheme_diff}" id="{self.sender_id}" role="{self.sender_role}"/>''')

    # Tests for make_reciever_identification method
    def test_should_make_reciever_identification_string(self):
        message = self.builder.make_reciever_identification()
        self.assertEqual(
            message, f'<default:ReceiverIdentification coding-scheme="14" id="8591824000007"/>')

    # Tests for make_location method
    def test_should_make_location(self):
        message = self.builder.make_location(self.unit)
        self.assertEqual(
            message, '<default:Location source-id="019259_Z11" ean="859182400211637793" date-to="2022-08-31" date-from="2022-08-01"/>')

    # Tests for make_location list
    def test_should_make_location_list(self):
        message = self.builder.make_location_list(self.units)
        self.assertEqual(
            message, '<default:Location source-id="019259_Z11" ean="859182400211637793" date-to="2022-08-31" date-from="2022-08-01"/><default:Location source-id="034687_Z11" ean="859182400211958560" date-to="2022-08-31" date-from="2022-08-01"/>')
