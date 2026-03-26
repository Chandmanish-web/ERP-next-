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

#### UI Enhancements

The Library Management app features a comprehensive, modern web interface with advanced HTML, CSS, and JavaScript functionality:

##### 🌟 **Landing Page (index.html)**
- **Interactive Hero Section**: Animated red star logo with bouncing effects and gradient text
- **Feature Cards**: Hover animations, shimmer effects, and ripple click interactions
- **Statistics Dashboard**: Animated counters with sparkle effects on completion
- **Modal System**: Smooth slide-in/out animations for login and registration forms
- **Advanced Animations**: Bounce, glow, pulse, and rotate keyframes throughout
- **Responsive Design**: Optimized layouts for all screen sizes

##### 📚 **Book Gallery (books.html)**
- **Advanced Search**: Real-time search with debouncing and visual feedback
- **Smart Filtering**: Category-based filtering with animated buttons
- **Book Cards**: 3D hover effects, staggered load animations, and ripple interactions
- **Modal Details**: Full-screen book information modals with smooth transitions
- **Pagination System**: Smart pagination with dots for large page ranges
- **Notification System**: Toast notifications for user actions and feedback
- **Keyboard Shortcuts**: Ctrl+F for search focus, Escape to clear search

##### 👤 **Member Dashboard (dashboard.html)**
- **Tabbed Interface**: Smooth animated tab switching with URL hash support
- **Interactive Book Cards**: Enhanced hover effects and action button animations
- **Confirmation Modals**: Professional confirmation dialogs for critical actions
- **Real-time Updates**: Dynamic statistics and list updates after actions
- **Settings Panel**: Theme switching (Light/Dark/Auto) with localStorage persistence
- **Enhanced Actions**: Return and renew book functionality with feedback
- **Keyboard Navigation**: Number keys (1-4) for quick tab switching

##### 🎨 **Design Features**
- **Red Star Branding**: Consistent red star logo and color scheme throughout
- **Gradient Backgrounds**: Beautiful linear gradients for headers and buttons
- **Animation Library**: Comprehensive CSS animations (fade, slide, bounce, pulse)
- **Interactive Elements**: Ripple effects, hover transformations, and micro-interactions
- **Notification System**: Toast notifications with auto-dismiss and manual close
- **Loading States**: Visual feedback for async operations and form submissions
- **Accessibility**: Keyboard navigation, screen reader support, and focus management

##### ⚡ **JavaScript Enhancements**
- **Debounced Search**: Optimized search performance with 300ms delay
- **Modal Management**: Centralized modal system with backdrop blur
- **Form Validation**: Real-time validation with visual feedback
- **Local Storage**: Theme preferences and user settings persistence
- **Event Handling**: Optimized event listeners with proper cleanup
- **Animation Timing**: Staggered animations for better visual hierarchy

##### 📱 **Responsive Features**
- **Mobile-First Design**: Optimized for mobile devices with touch interactions
- **Flexible Layouts**: Grid systems that adapt to screen sizes
- **Touch Gestures**: Swipe-friendly interfaces and touch-optimized buttons
- **Breakpoint Optimization**: Custom styles for tablets, phones, and desktops

##### 🔧 **Technical Implementation**
- **Vanilla JavaScript**: No external dependencies for core functionality
- **CSS Custom Properties**: Consistent theming with CSS variables
- **Performance Optimized**: Efficient animations and minimal DOM manipulation
- **Cross-browser Compatible**: Modern CSS with fallbacks for older browsers
- **SEO Friendly**: Semantic HTML structure and proper meta tags

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
