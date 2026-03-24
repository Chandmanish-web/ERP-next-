# -*- coding: utf-8 -*-
# Copyright (c) 2024, Library Management Contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import getdate, add_days


class BookTransaction(Document):
	"""DocType for managing book transactions with validation and inventory tracking"""
	
	def before_save(self):
		"""Auto-calculate due date for Issue transactions"""
		# Auto-set due_date to 14 days from transaction_date for Issue transactions
		if self.transaction_type == "Issue" and not self.due_date:
			self.due_date = add_days(self.transaction_date, 14)
		
		# Auto-set status based on transaction type
		if self.transaction_type == "Issue":
			self.status = "Issued"
		elif self.transaction_type == "Return":
			self.status = "Returned"
	
	def validate(self):
		"""Validate transaction data"""
		
		# Validation 1: Member and Book are mandatory
		if not self.member:
			frappe.throw("Please select a Library Member")
		if not self.book:
			frappe.throw("Please select a Book")
		
		# Validation 2: Check if member exists and is active
		member = frappe.get_doc("Library Member", self.member)
		if member.status == "Suspended":
			frappe.throw(f"Member '{member.full_name}' is suspended. Cannot process transaction.")
		
		# Validation 3: Check if book exists
		book = frappe.get_doc("Book", self.book)
		
		# Validation 4: If Issue, verify book is available
		if self.transaction_type == "Issue":
			if book.available_copies <= 0:
				frappe.throw(f"Book '{book.title}' is not available. No copies left in stock.")
			if not self.due_date:
				frappe.throw("Due Date is mandatory for Issue transactions")
		
		# Validation 5: If Return, return_date is mandatory
		if self.transaction_type == "Return":
			if not self.return_date:
				frappe.throw("Return Date is mandatory for Return transactions")
		
		# Validation 6: return_date cannot be before transaction_date
		if self.return_date:
			if getdate(self.return_date) < getdate(self.transaction_date):
				frappe.throw("Return Date cannot be before Transaction Date")
		
		# Validation 7: Transaction date must be set
		if not self.transaction_date:
			frappe.throw("Transaction Date is mandatory")
	
	def on_submit(self):
		"""Update book inventory when transaction is submitted"""
		book = frappe.get_doc("Book", self.book)
		
		if self.transaction_type == "Issue":
			# Decrease available copies
			book.available_copies -= 1
		else:
			# Increase available copies on return
			book.available_copies += 1
		
		book.save()
		frappe.msgprint(f"Inventory updated for book: {book.title}")
