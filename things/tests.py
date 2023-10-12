from django import forms
from django.test import TestCase
from .forms import ThingForm

# Create your tests here.

class ThingFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            'name' : 'Jane Doe',
            'description' : 'Hi, my name is Jane Doe',
            'quantity' : '1',
        }

    def test_valid_thing_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        description_field = form.fields['description'].widget
        self.assertTrue(isinstance(description_field, forms.Textarea))
        self.assertIn('quantity', form.fields)
        quantity_field = form.fields['quantity'].widget
        self.assertTrue(isinstance(quantity_field, forms.NumberInput))

    # Test for valid inputs

    def test_form_uses_model_validation(self):
        self.form_input['name'] = 'James'
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_name_cannot_be_blank(self):
        self.form_input['name'] = ''
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    
    def test_description_cannot_be_more_than_120_characters_long(self):
        self.form_input['description'] = 'x' * 121
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_description_can_be_120_characters_long(self):
        self.form_input['description'] = 'x' * 120
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_description_cannot_be_more_than_120_characters_long(self):
        self.form_input['description'] = 'x' * 121
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_quantity_cannot_be_blank(self):
        self.form_input['quantity'] = ''
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_quantity_cannot_be_negative(self):
        self.form_input['quantity'] = '-1'
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_quantity_can_be_0(self):
        self.form_input['quantity'] = '0'
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_description_cannot_be_more_than_51(self):
        self.form_input['quantity'] = '51'
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_description_can_be_50(self):
        self.form_input['quantity'] = '50'
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())