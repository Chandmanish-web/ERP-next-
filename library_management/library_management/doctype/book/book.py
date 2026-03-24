# -*- coding: utf-8 -*-
# Copyright (c) 2024, Library Management Contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Book(Document):
	"""DocType for managing library books with inventory tracking"""
	
	def before_save(self):
		"""Set available copies on new book creation and update status"""
		# If this is a new book, set available_copies = total_copies
		if self.is_new():
			self.available_copies = self.total_copies
			if not self.status:
				self.status = "Available"
		
		# Ensure available_copies never exceeds total_copies
		if self.available_copies > self.total_copies:
			self.available_copies = self.total_copies
		
		# Update status based on available copies
		if self.available_copies == 0:
			self.status = "Checked Out"
		elif self.available_copies > 0 and self.status == "Checked Out":
			self.status = "Available"
	
	def validate(self):
		"""Validate book data"""
		# Validation 1: Ensure total_copies is positive
		if self.total_copies < 1:
			frappe.throw("Total copies must be at least 1")
		
		# Validation 2: Ensure available_copies is not negative
		if self.available_copies < 0:
			frappe.throw("Available copies cannot be negative")
		
		# Validation 3: Title and Author are mandatory
		if not self.title:
			frappe.throw("Book Title is mandatory")
		if not self.author:
			frappe.throw("Author is mandatory")
		
		# Validation 4: Check ISBN uniqueness if provided
		if self.isbn:
			existing = frappe.db.get_value(
				"Book",
				{"isbn": self.isbn, "name": ["!=", self.name]}
			)
			if existing:
				frappe.throw(f"ISBN '{self.isbn}' already exists for another book")