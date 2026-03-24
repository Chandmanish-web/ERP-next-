import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):

    def validate(self):
        if not self.book:
            frappe.throw("Please select a Book")

        book = frappe.get_doc("Book", self.book)

        if self.type == "Issue":
            if book.available_quantity <= 0:
                frappe.throw("Book not available")

            book.available_quantity -= 1
            book.save()

        elif self.type == "Return":
            book.available_quantity += 1
            book.save()