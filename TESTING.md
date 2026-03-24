# Testing Guide for Library Management App

## Overview
This document outlines the testing procedures for the Library Management System to ensure all features work correctly.

## Test Cases

### Library Member Tests

#### TC001: Create Valid Member
- **Steps**:
  1. Navigate to Library Member list
  2. Click "New"
  3. Enter: First Name="John", Last Name="Doe", Email="john.doe@example.com"
  4. Set Membership Start Date to today
  5. Set Membership End Date to one year from today
  6. Save
- **Expected**: Member created successfully, full name auto-generated as "John Doe"

#### TC002: Duplicate Email Validation
- **Steps**:
  1. Try to create another member with same email "john.doe@example.com"
- **Expected**: Error message "Email already registered to another member"

#### TC003: Invalid Email Format
- **Steps**:
  1. Create member with email "invalid-email"
- **Expected**: Error message "Please enter a valid email address"

#### TC004: Invalid Membership Dates
- **Steps**:
  1. Set End Date before Start Date
- **Expected**: Error message "Membership End Date must be after Start Date"

### Book Tests

#### TC005: Create Valid Book
- **Steps**:
  1. Navigate to Book list
  2. Click "New"
  3. Enter: Title="Python Guide", Author="John Smith", Total Copies=5, ISBN="1234567890"
  4. Save
- **Expected**: Book created, Available Copies auto-set to 5, Status="Available"

#### TC006: Duplicate ISBN Validation
- **Steps**:
  1. Try to create another book with same ISBN
- **Expected**: Error message "ISBN already exists for another book"

#### TC007: Invalid Copy Count
- **Steps**:
  1. Set Total Copies to 0 or negative
- **Expected**: Error message "Total copies must be at least 1"

### Book Transaction Tests

#### TC008: Issue Book Successfully
- **Steps**:
  1. Create a member and book (if not exists)
  2. Navigate to Book Transaction
  3. Click "New"
  4. Select Type="Issue"
  5. Select Member and Book
  6. Set Transaction Date to today
  7. Save and Submit
- **Expected**: Transaction created, Due Date auto-set to 14 days later, Book available copies decreased by 1

#### TC009: Issue Book When Unavailable
- **Steps**:
  1. Set book available copies to 0
  2. Try to issue the book
- **Expected**: Error message "Book is not available. No copies left in stock."

#### TC010: Return Book
- **Steps**:
  1. Create Issue transaction first
  2. Create new Return transaction for same member and book
  3. Set Return Date
  4. Save and Submit
- **Expected**: Transaction created, Book available copies increased by 1

#### TC011: Return Date Before Transaction Date
- **Steps**:
  1. Set Return Date before Transaction Date
- **Expected**: Error message "Return Date cannot be before Transaction Date"

## Automated Testing

Run the following command to execute doctests and validations:

```bash
bench --site yoursite.localhost console
```

Then run:
```python
# Test member creation
doc = frappe.get_doc({'doctype':'Library Member', 'first_name':'Test', 'last_name':'User', 'email':'test@example.com'})
doc.insert()

# Test book creation
doc = frappe.get_doc({'doctype':'Book', 'title':'Test Book', 'author':'Test Author', 'total_copies':1})
doc.insert()

# Test transaction
doc = frappe.get_doc({'doctype':'Book Transaction', 'transaction_type':'Issue', 'member':'Test User', 'book':'Test Book'})
doc.insert()
doc.submit()
```

## Performance Testing

- Test with 100+ members and books
- Verify list loading times < 2 seconds
- Check database query performance

## Browser Compatibility

Test on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+