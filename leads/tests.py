from re import A
from django.test import TestCase
from leads.models import lead, User, Agent
from leads.forms import leadform


class LeadTestcase(TestCase):
    def setUp(self):
        self.val = lead.objects.create(
            first_name="Test_f", last_name="test_l", source="Facebook"
        )
        self.user = User.objects.create(
            first_name="test_user", last_name="test", email="test@test.com"
        )

        self.val.agent = Agent.objects.create(user=self.user)
        self.val.save()

    def test_lead_retrieval(self):
        """Leads are retrieved succesfully"""
        get_lead = lead.objects.get(first_name="Test_f")
        self.assertEqual(get_lead.last_name, "test_l")
        self.assertEqual(get_lead.source, "Facebook")

    def test_agent_retrieval(self):
        """Agents are retrieved succesfully"""
        get_lead = lead.objects.get(first_name="Test_f")
        # print(get_lead.agent.first_name)
        self.assertEqual(get_lead.agent.user.first_name, "test_user")
        self.assertEqual(get_lead.agent.user.email, "test@test.com")


class FormTest(TestCase):
    """Class to validate Form submission."""

    def setUp(self):
        self.user = User.objects.create(
            first_name="test_user", last_name="test", email="test@test.com"
        )
        self.agent = Agent.objects.create(user=self.user)

    def test_form_create_incorrect_Source_value(self):
        """Test case to validate incorrect source submission."""
        form = leadform()
        form.source = 10
        self.assertFalse(form.is_valid())

    def test_form_generate_validate(self):
        # datan = dict({'first_name':'Test_f','last_name':'test_l','source'='Facebook' })
        datan = {
            "first_name": "Test_f",
            "last_name": "test_l",
            "source": "FB",
            "age": 56,
            "email": "test@test.com",
            "contact_no": "9999999",
            "adress": "NJ",
            'contacted': True
        }
        form = leadform(data=datan)
        if form.is_valid():
            form.save()
        get_lead = lead.objects.get(first_name="Test_f")
        self.assertEqual(get_lead.source, "FB")
        self.assertTrue(get_lead.contacted)
