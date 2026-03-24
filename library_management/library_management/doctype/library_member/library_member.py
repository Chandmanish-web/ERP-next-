# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class LibraryMember(Document):
	"""DocType for managing library members with professional ID generation"""
	
	def before_save(self):
		"""Generate full name and validate membership dates"""
		# Generate full name from first and last name
		if self.first_name and self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}"
		
		# Set default membership start date if not set
		if not self.membership_start_date:
			self.membership_start_date = getdate()
	
	def validate(self):
		"""Validate member data"""
		# Validation 1: Ensure email is in valid format
		if self.email and "@" not in self.email:
			frappe.throw("Please enter a valid email address")
		
		# Validation 2: Ensure membership end date is after start date if provided
		if self.membership_end_date and self.membership_start_date:
			if getdate(self.membership_end_date) < getdate(self.membership_start_date):
				frappe.throw("Membership End Date must be after Start Date")
		
		# Validation 3: Check for duplicate email
		if self.email:
			existing = frappe.db.get_value(
				"Library Member",
				{"email": self.email, "name": ["!=", self.name]}
			)
			if existing:
				frappe.throw(f"Email '{self.email}' is already registered to another member")
		
		# Validation 4: First name and last name are mandatory
		if not self.first_name:
			frappe.throw("First Name is mandatory")
		if not self.last_name:
			frappe.throw("Last Name is mandatory")

