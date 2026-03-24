### Library Management

A comprehensive Library Management System built on Frappe Framework.

#### Features

- **Library Member Management**: Register members with personal details, membership dates, and status tracking.
- **Book Inventory**: Manage book catalog with title, author, ISBN, total and available copies.
- **Book Transactions**: Handle book issue and return operations with automatic inventory updates and validations.

#### Installation

1. **Prerequisites**: Ensure you have a Frappe bench set up. If not, follow the [Frappe installation guide](https://frappeframework.com/docs/user/en/installation).

2. **Get the App**:
   ```bash
   cd $PATH_TO_YOUR_BENCH
   bench get-app https://github.com/yourusername/library_management.git
   ```

3. **Install on Site**:
   ```bash
   bench --site yoursite.localhost install-app library_management
   bench --site yoursite.localhost migrate
   ```

#### Usage

After installation, access the app through the Frappe Desk:

1. **Create Library Members**:
   - Go to Library Member list
   - Add members with first name, last name, email, and membership dates
   - System validates email uniqueness and date logic

2. **Add Books**:
   - Go to Book list
   - Enter book details: title, author, ISBN, total copies
   - Available copies are automatically set and tracked

3. **Process Transactions**:
   - Go to Book Transaction
   - Select Issue or Return type
   - Choose member and book
   - System validates availability, member status, and updates inventory

#### Doctypes

- **Library Member**: Member registration and management
- **Book**: Book catalog and inventory
- **Book Transaction**: Issue/return operations

#### Validation Rules

- Members: Unique email, valid membership dates
- Books: Unique ISBN, positive copy counts
- Transactions: Availability checks, date validations, automatic inventory updates

#### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

#### License

MIT
